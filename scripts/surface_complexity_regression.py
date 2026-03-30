#!/usr/bin/env python3
"""
surface_complexity_regression.py

Compute surface-complexity features per (problem, representation),
merge with runs/scores/exp1_*.csv correctness data, then run:
 - statsmodels logistic regression to inspect coefficient/significance
 - sklearn logistic to compute average marginal effect (vector vs coord)
Also outputs correlations and diagnostic plots.

Outputs (runs/analysis/):
 - features_merged.csv
 - regression_summary.txt
 - marginal_effects.txt
 - feature_correlations.csv
 - figures: feature_histograms.png, token_vs_correct_box.png
"""

from pathlib import Path
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
import warnings
warnings.filterwarnings("ignore")

# ---------------- Paths ----------------
BASE_PROBLEM_DIR = Path("problems/exp1")
SCORES_DIR = Path("runs/scores_rep_to_euclid")
OUT_DIR = Path("runs/analysis")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ---------------- Utilities to extract problem text ----------------
def problem_text_path(problem_id: str, rep: str) -> Path:
    # problem_id example: "length_hard_01" -> category is the first token before '_'
    category = problem_id.split("_")[0]
    p = BASE_PROBLEM_DIR / category / f"{problem_id}_{rep}.txt"
    return p

# ---------------- Feature extraction ----------------
NUMERIC_RE = re.compile(r"\d+(\.\d+)?")
COORD_RE = re.compile(r"\(\s*-?\d+(\.\d+)?\s*,\s*-?\d+(\.\d+)?\s*\)")
UPPER_LETTER_RE = re.compile(r"\b([A-Z])\b")
FRACTION_RE = re.compile(r"\d+/\d+")
SQRT_RE = re.compile(r"(sqrt\(|√)")

SYMBOL_SET = set("+-*/=^√°Δ∠,;:.()[]{}|<>•·")

def compute_features_from_text(text: str) -> dict:
    text = text or ""
    # tokens and basic counts
    tokens = re.findall(r"\S+", text)
    token_length = len(tokens)
    char_length = len(text)
    # symbols = non-alphanumeric, non-space
    num_symbols = sum(1 for ch in text if (not ch.isalnum()) and (not ch.isspace()))
    # operator count (counts occurrences of common arithmetic operators)
    operator_count = sum(text.count(op) for op in "+-*/=^")
    # numeric counts
    num_numbers = len(NUMERIC_RE.findall(text))
    num_fractions = len(FRACTION_RE.findall(text))
    num_sqrt = len(SQRT_RE.findall(text))
    # coordinate tuples like (3,4)
    num_coords = len(COORD_RE.findall(text))
    # uppercase single-letter tokens and uppercase letters that appear before '('
    points_tokens = set(re.findall(r"\b[A-Z]\b", text))
    points_before_paren = set(re.findall(r"([A-Z])\s*\(", text))
    num_points = len(points_tokens.union(points_before_paren))
    # estimate arithmetic load: numbers + operators + fractions + sqrt occurrences
    arithmetic_load = num_numbers + operator_count + num_fractions + num_sqrt
    # number of distinct numeric tokens (complexity of numeric expressions)
    distinct_numbers = len(set(re.findall(r"\d+(\.\d+)?", text)))
    # punctuation density
    punct_density = (num_symbols / (char_length + 1))
    return {
        "token_length": token_length,
        "char_length": char_length,
        "num_symbols": num_symbols,
        "operator_count": operator_count,
        "num_numbers": num_numbers,
        "num_fractions": num_fractions,
        "num_sqrt": num_sqrt,
        "num_coords": num_coords,
        "num_points": num_points,
        "arithmetic_load": arithmetic_load,
        "distinct_numbers": distinct_numbers,
        "punct_density": punct_density
    }

# ---------------- Load scores and build feature table ----------------
csv_files = sorted(SCORES_DIR.glob("exp1_*.csv"))
if not csv_files:
    raise SystemExit(f"No score CSVs found in {SCORES_DIR} (exp1_*.csv). Run scoring first.")

# read + concat all models' score CSVs
dfs = []
for csv_file in csv_files:
    model_name = csv_file.stem.replace("exp1_", "")
    df = pd.read_csv(csv_file, dtype=str)
    df["model"] = model_name
    dfs.append(df)
scores = pd.concat(dfs, ignore_index=True)

# normalize representation, problem and correct fields
scores["representation"] = scores["representation"].astype(str).str.lower()
scores["problem"] = scores["problem"].astype(str)
# Normalize correct -> correct_strict numeric (0/1)
def norm_correct(x):
    if pd.isna(x): return np.nan
    s = str(x).strip().lower()
    if s in ("true","1","t","yes","y"): return 1
    if s in ("false","0","f","no","n"): return 0
    if s == "med":  # treat MED as wrong for strict scoring; you can change this
        return 0
    try:
        return int(x)
    except Exception:
        return np.nan

scores["correct_strict"] = scores["correct"].apply(norm_correct).astype("float")

# Build features for each (problem,representation). Cache to avoid re-reading files
feat_cache = {}
rows = []
missing_text = 0
for idx, row in scores.iterrows():
    pid = row["problem"]
    rep = row["representation"]
    key = (pid, rep)
    if key in feat_cache:
        feats = feat_cache[key]
    else:
        ppath = problem_text_path(pid, rep)
        if not ppath.exists():
            # Try .json or .txt fallback variants (some of your run scripts used .json or .txt)
            # Check .txt first, then .json
            alt_txt = Path(str(ppath).replace(".txt", ".json"))
            if alt_txt.exists():
                text = alt_txt.read_text(encoding="utf-8")
            else:
                # no text found, set empty and continue
                text = ""
                missing_text += 1
        else:
            text = ppath.read_text(encoding="utf-8")
        feats = compute_features_from_text(text)
        feat_cache[key] = feats
    out = {
        "model": row["model"],
        "problem": pid,
        "representation": rep,
        "predicted": row.get("predicted", ""),
        "gold": row.get("gold", ""),
        "correct_strict": row.get("correct_strict", np.nan)
    }
    out.update(feats)
    rows.append(out)

features_df = pd.DataFrame(rows)
# sanitize model string for categorical usage
features_df["model_sanit"] = features_df["model"].str.replace(r"[^\w]+", "_", regex=True)

features_csv = OUT_DIR / "features_merged.csv"
features_df.to_csv(features_csv, index=False)
print(f"[INFO] Features written to: {features_csv}  (missing_text={missing_text})")

# ---------------- Basic correlations between features and correctness ----------------
corr_cols = [
    "token_length", "char_length", "num_symbols", "operator_count",
    "num_numbers", "num_fractions", "num_sqrt", "num_coords",
    "num_points", "arithmetic_load", "distinct_numbers", "punct_density"
]
# drop NaNs in correctness
corr_df = features_df[[*corr_cols, "correct_strict", "representation", "model_sanit"]].dropna(subset=["correct_strict"])
# compute Pearson r for each feature -> correctness
corrs = []
for c in corr_cols:
    try:
        r = corr_df[c].astype(float).corr(corr_df["correct_strict"].astype(float))
    except Exception:
        r = np.nan
    corrs.append((c, r))
corr_table = pd.DataFrame(corrs, columns=["feature", "pearson_r_with_correct"])
corr_table.to_csv(OUT_DIR / "feature_correlations.csv", index=False)
print(f"[INFO] Feature correlations saved to {OUT_DIR/'feature_correlations.csv'}")

# ---------------- Regression: statsmodels logistic (pooled, with model fixed effects) ----------------
# Prepare dataframe for regression; drop rows missing correctness or features
reg_df = features_df.dropna(subset=["correct_strict"] + corr_cols).copy()
# cast numeric features
for c in corr_cols:
    reg_df[c] = reg_df[c].astype(float)
reg_df["correct_strict"] = reg_df["correct_strict"].astype(int)
# representation as categorical (euclid=reference)
reg_df["representation"] = reg_df["representation"].astype("category")
# choose reference: euclid if present, else the first category
if "euclid" in reg_df["representation"].cat.categories:
    reg_df["representation"] = reg_df["representation"].cat.reorder_categories(["euclid","coord","vector"], ordered=False)
# model fixed effects using sanitized model names (as categorical)
reg_df["model_sanit"] = reg_df["model_sanit"].astype("category")

# build formula: correct_strict ~ C(representation) + token_length + num_symbols + num_points + arithmetic_load + C(model_sanit)
formula = "correct_strict ~ C(representation) + token_length + num_symbols + num_points + arithmetic_load + C(model_sanit)"
print(f"[INFO] Fitting statsmodels Logit with formula: {formula} ... (this may take a few seconds)")
try:
    logit_res = smf.logit(formula=formula, data=reg_df).fit(disp=False, maxiter=200)
    summary_txt = logit_res.summary2().as_text()
    (OUT_DIR / "regression_summary.txt").write_text(summary_txt, encoding="utf-8")
    print(f"[INFO] Regression summary written to {OUT_DIR/'regression_summary.txt'}")
except Exception as e:
    (OUT_DIR / "regression_summary.txt").write_text(f"Regression failed: {e}", encoding="utf-8")
    print(f"[WARN] Regression failed: {e}")
    logit_res = None

# ---------------- Marginal effect via sklearn logistic (average marginal effect vector vs coord) ----------
# Build design X: numeric features + representation one-hot + model_sanit one-hot
X_numeric = reg_df[corr_cols].fillna(0).astype(float)
rep_ohe = pd.get_dummies(reg_df["representation"], prefix="rep")
mod_ohe = pd.get_dummies(reg_df["model_sanit"], prefix="mod")
X = pd.concat([X_numeric, rep_ohe, mod_ohe], axis=1).fillna(0)
y = reg_df["correct_strict"].astype(int).values

sk_model = LogisticRegression(max_iter=2000, solver="lbfgs")
sk_model.fit(X, y)
# average predicted probability if representation forced to vector vs coord (keeping other columns same)
X_vector = X.copy()
X_coord = X.copy()
# set rep columns deterministically
for col in [c for c in X.columns if c.startswith("rep_")]:
    X_vector[col] = 1 if col == "rep_vector" else 0
    X_coord[col] = 1 if col == "rep_coord" else 0

p_vector = sk_model.predict_proba(X_vector)[:, 1].mean()
p_coord = sk_model.predict_proba(X_coord)[:, 1].mean()
avg_marginal = p_vector - p_coord

me_text = (
    "Average marginal probability difference (vector - coord)\n"
    f"Avg P(correct | vector)  = {p_vector:.4f}\n"
    f"Avg P(correct | coord)   = {p_coord:.4f}\n"
    f"Avg marginal effect      = {avg_marginal:.4f}\n"
)
(OUT_DIR / "marginal_effects.txt").write_text(me_text, encoding="utf-8")
print("[INFO] Marginal effects written to", OUT_DIR / "marginal_effects.txt")
print(me_text)

# ---------------- Extra: per-model regression for signal (optional, quick) ----------------
per_model_summary = []
for model in sorted(reg_df["model_sanit"].unique()):
    sub = reg_df[reg_df["model_sanit"] == model]
    if len(sub) < 30:
        # skip tiny
        per_model_summary.append((model, "skipped (n<30)"))
        continue
    try:
        res = smf.logit("correct_strict ~ C(representation) + token_length + num_symbols + num_points + arithmetic_load",
                        data=sub).fit(disp=False, maxiter=200)
        coef_vec = res.params.filter(like("C(representation)[T.vector]"))
        pval_vec = res.pvalues.get("C(representation)[T.vector]", np.nan)
        per_model_summary.append((model, float(coef_vec.values[0]) if not coef_vec.empty else np.nan, float(pval_vec)))
    except Exception as e:
        per_model_summary.append((model, f"error:{e}", None))

pm_df = pd.DataFrame(per_model_summary, columns=["model","coef_vector","pval_vector"])
pm_df.to_csv(OUT_DIR / "per_model_representation_vector_coef.csv", index=False)
print("[INFO] Per-model vector coefficient table saved to", OUT_DIR / "per_model_representation_vector_coef.csv")

# ---------------- Save feature+score merged file already done above; save regression-ready table too
reg_df.to_csv(OUT_DIR / "regression_table.csv", index=False)

# ---------------- Diagnostic plots ----------------
plt.figure(figsize=(10,6))
reg_df["token_length"].hist(bins=60)
plt.xlabel("token_length")
plt.title("Distribution of token_length across all variants")
plt.tight_layout()
plt.savefig(OUT_DIR / "feature_histograms.png", dpi=200)
plt.close()

# boxplot token_length vs correct
plt.figure(figsize=(7,5))
reg_df.boxplot(column="token_length", by="correct_strict")
plt.title("Token length by correctness (0/1)")
plt.suptitle("")
plt.xlabel("correct_strict")
plt.ylabel("token_length")
plt.tight_layout()
plt.savefig(OUT_DIR / "token_vs_correct_box.png", dpi=200)
plt.close()

# ---------------- Final printed summary ----------------
print("\n=== Quick results summary ===")
print(f"Pooled logistic regression fitted: {'yes' if logit_res is not None else 'no'}")
if logit_res is not None:
    # try to print coefficient for vector (categorical)
    try:
        coef_name = "C(representation)[T.vector]"
        coef = logit_res.params.get(coef_name, None)
        pval = logit_res.pvalues.get(coef_name, None)
        print(f"Coefficient for representation=vector: {coef} (p = {pval})")
    except Exception:
        print("Could not extract vector coefficient from statsmodels result.")
print("Average marginal effect vector-vs-coord (sklearn):")
print(me_text)

print(f"\nAll outputs saved under {OUT_DIR}.")
