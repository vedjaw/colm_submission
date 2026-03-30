#!/usr/bin/env python3
"""
representation_flip_analysis.py

Item-level representation "flip" analysis.

Saves CSV summaries and plots under runs/analysis/.
"""

from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------- Config ----------------
SCORES_DIR = Path("runs/scores_rep_to_euclid")
OUT_DIR = Path("runs/analysis")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# patterns order (E, C, V)
PATTERN_ORDER = ["CCC", "CCW", "CWC", "WCC", "CWW", "WCW", "WWC", "WWW"]

# ---------------- Helpers ----------------
def normalize_correct(x):
    """Map various possible 'correct' encodings to 1/0."""
    if pd.isna(x):
        return np.nan
    if isinstance(x, (int, float, np.integer, np.floating)):
        try:
            return int(x)
        except Exception:
            return np.nan
    s = str(x).strip().lower()
    if s in ("true", "t", "1", "yes", "y"):
        return 1
    if s in ("false", "f", "0", "no", "n"):
        return 0
    # handle special markings like 'MED' (you can treat as wrong; change if needed)
    if s == "med":
        return 0
    return np.nan

def pattern_from_row(row):
    """Given row with columns ['euclid','coord','vector'] all 0/1,
    return 3-letter pattern in E,C,V order where 1->'C', 0->'W'."""
    mapping = {1: "C", 0: "W"}
    try:
        return "".join(mapping[int(row[col])] for col in ["euclid", "coord", "vector"])
    except Exception:
        return None

# ---------------- Load & prepare ----------------
csv_files = sorted(SCORES_DIR.glob("exp1_*.csv"))
if not csv_files:
    raise SystemExit(f"No score CSV files found in {SCORES_DIR} (expected exp1_*.csv)")

dfs = []
for csv_file in csv_files:
    model_name = csv_file.stem.replace("exp1_", "")
    df = pd.read_csv(csv_file, dtype=str)  # read as str, we'll normalize
    df["model"] = model_name
    dfs.append(df)

scores = pd.concat(dfs, ignore_index=True)

# normalize problem / representation / predicted / correct
for col in ["problem", "representation", "predicted", "gold", "model"]:
    if col in scores.columns:
        scores[col] = scores[col].astype(str)

# Normalize 'correct' to 0/1 (int)
if "correct" not in scores.columns:
    raise SystemExit("Input score CSVs must have a 'correct' column.")

scores["correct_norm"] = scores["correct"].map(normalize_correct).astype("float")

# ---------------- Per-model item-level patterns ----------------
models = sorted(scores["model"].unique())

# DataFrames to collect
counts_rows = []
percent_rows = []
pairwise_rows = []

# We'll also build an overall (across-model) summary if needed
for model in models:
    sub = scores[scores["model"] == model].copy()

    # pivot correctness by problem x representation
    pivot_corr = sub.pivot_table(
        index="problem",
        columns="representation",
        values="correct_norm",
        aggfunc="first"
    )

    # We require columns named exactly 'euclid','coord','vector' (case-insensitive)
    # Normalize column names (lowercase)
    pivot_corr.columns = [c.lower() for c in pivot_corr.columns]

    # Keep only rows that have all three representations present (non-NaN)
    required_cols = ["euclid", "coord", "vector"]
    missing = [c for c in required_cols if c not in pivot_corr.columns]
    if missing:
        # If missing some representations, create them filled with NaN
        for c in missing:
            pivot_corr[c] = np.nan

    # Select problems that have all three (non-null). This ensures fair item-level comparisons
    pivot_all3 = pivot_corr.dropna(subset=required_cols).copy()
    if pivot_all3.empty:
        # nothing to evaluate
        pattern_counts = {p: 0 for p in PATTERN_ORDER}
        n_problems = 0
    else:
        # cast to ints
        pivot_all3 = pivot_all3[required_cols].astype(int)
        # create pattern
        pivot_all3["pattern"] = pivot_all3.apply(pattern_from_row, axis=1)
        # count patterns
        pattern_counts = pivot_all3["pattern"].value_counts().reindex(PATTERN_ORDER, fill_value=0).to_dict()
        n_problems = len(pivot_all3)

    # counts and percentages
    counts_row = {"model": model, "n_problems_evaluated": n_problems}
    percent_row = {"model": model, "n_problems_evaluated": n_problems}
    for p in PATTERN_ORDER:
        counts_row[f"count_{p}"] = int(pattern_counts.get(p, 0))
        percent_row[f"pct_{p}"] = (pattern_counts.get(p, 0) / n_problems) if n_problems else 0.0

    counts_rows.append(counts_row)
    percent_rows.append(percent_row)

    # --- single-point-of-failure analysis ---
    # Patterns with exactly one W (i.e., two C, one W) are CCW, CWC, WCC.
    one_fail_patterns = {"CCW": ("euclid","coord","vector"),
                         "CWC": ("euclid","coord","vector"),
                         "WCC": ("euclid","coord","vector")}
    # Determine which representation is failing in each one-fail pattern:
    # CCW -> vector fails; CWC -> coord fails; WCC -> euclid fails
    rep_failure_counts = {
        "euclid": pattern_counts.get("WCC", 0),
        "coord": pattern_counts.get("CWC", 0),
        "vector": pattern_counts.get("CCW", 0)
    }

    # --- pair transfer when third fails ---
    # For pair (E,C): count CCW (E and C correct while V wrong)
    # We normalize by number of problems where V is wrong (i.e., patterns with V=W)
    patterns_with_V_wrong = sum(pattern_counts.get(p,0) for p in PATTERN_ORDER if p[2] == "W")
    patterns_with_C_wrong = sum(pattern_counts.get(p,0) for p in PATTERN_ORDER if p[1] == "W")
    patterns_with_E_wrong = sum(pattern_counts.get(p,0) for p in PATTERN_ORDER if p[0] == "W")

    # counts where pair succeed and third fails:
    count_EC_pair_when_V_fails = pattern_counts.get("CCW", 0)
    count_CV_pair_when_E_fails = pattern_counts.get("WCC", 0)  # careful: WCC = E wrong, C & V correct -> that's CV pair when E fails
    count_EV_pair_when_C_fails = pattern_counts.get("CWC", 0)  # CWC = C wrong, E & V correct -> EV pair when C fails

    # compute rates (safe divide)
    rate_EC_when_V_fails = (count_EC_pair_when_V_fails / patterns_with_V_wrong) if patterns_with_V_wrong else 0.0
    rate_CV_when_E_fails = (count_CV_pair_when_E_fails / patterns_with_E_wrong) if patterns_with_E_wrong else 0.0
    rate_EV_when_C_fails = (count_EV_pair_when_C_fails / patterns_with_C_wrong) if patterns_with_C_wrong else 0.0

    # pairwise coherence: fraction of problems where pair values are equal (both correct or both wrong)
    # compute from pivot_all3
    if n_problems:
        pair_EC_coherence = ((pivot_all3["euclid"] == pivot_all3["coord"]).sum()) / n_problems
        pair_CV_coherence = ((pivot_all3["coord"] == pivot_all3["vector"]).sum()) / n_problems
        pair_EV_coherence = ((pivot_all3["euclid"] == pivot_all3["vector"]).sum()) / n_problems
    else:
        pair_EC_coherence = pair_CV_coherence = pair_EV_coherence = 0.0

    pairwise_rows.append({
        "model": model,
        "n_problems_evaluated": n_problems,
        "rep_fail_euclid_count": int(rep_failure_counts["euclid"]),
        "rep_fail_coord_count": int(rep_failure_counts["coord"]),
        "rep_fail_vector_count": int(rep_failure_counts["vector"]),
        "rate_EC_when_V_fails": rate_EC_when_V_fails,
        "rate_CV_when_E_fails": rate_CV_when_E_fails,
        "rate_EV_when_C_fails": rate_EV_when_C_fails,
        "pair_EC_coherence": pair_EC_coherence,
        "pair_CV_coherence": pair_CV_coherence,
        "pair_EV_coherence": pair_EV_coherence
    })

# ---------------- Save CSV summaries ----------------
df_counts = pd.DataFrame(counts_rows).sort_values("model")
df_percents = pd.DataFrame(percent_rows).sort_values("model")
df_pairs = pd.DataFrame(pairwise_rows).sort_values("model")

df_counts.to_csv(OUT_DIR / "rep_flip_counts_per_model.csv", index=False)
df_percents.to_csv(OUT_DIR / "rep_flip_percentages_per_model.csv", index=False)
df_pairs.to_csv(OUT_DIR / "rep_flip_pairwise_metrics_per_model.csv", index=False)

print(f"[DONE] Saved CSV summaries to {OUT_DIR}")

# ---------------- Print compact textual summary ----------------
print("\n=== Compact summary per model ===")
for i, row in df_pairs.iterrows():
    model = row["model"]
    n = int(row["n_problems_evaluated"])
    fails = { "euclid": int(row["rep_fail_euclid_count"]),
              "coord": int(row["rep_fail_coord_count"]),
              "vector": int(row["rep_fail_vector_count"]) }
    # determine usual single point of failure
    usual_failure = max(fails.items(), key=lambda x: x[1])[0] if n>0 else "N/A"
    print(f"\nModel: {model}  (problems={n})")
    print(f"  Single-point-of-failure counts (one-fail patterns): {fails}")
    print(f"  Usual single point of failure: {usual_failure}")
    print("  Pair transfer when third fails (EC|Vfail, CV|Efail, EV|Cfail): "
          f"{row['rate_EC_when_V_fails']:.3f}, {row['rate_CV_when_E_fails']:.3f}, {row['rate_EV_when_C_fails']:.3f}")
    print("  Pair coherence (EC, CV, EV): "
          f"{row['pair_EC_coherence']:.3f}, {row['pair_CV_coherence']:.3f}, {row['pair_EV_coherence']:.3f}")

# ---------------- Plots ----------------
# Stacked bar of pattern counts per model
plot_df = df_counts.set_index("model")[[f"count_{p}" for p in PATTERN_ORDER]].copy()
plot_df.columns = PATTERN_ORDER

# ensure consistent order
plot_df = plot_df.loc[sorted(plot_df.index)]

fig, ax = plt.subplots(figsize=(12, max(4, 0.4 * len(plot_df))))
bottom = np.zeros(len(plot_df))
x = np.arange(len(plot_df))
colors = plt.cm.tab20.colors
for i, p in enumerate(PATTERN_ORDER):
    vals = plot_df[p].values
    ax.barh(x, vals, left=bottom, label=p, color=colors[i % len(colors)])
    bottom += vals

ax.set_yticks(x)
ax.set_yticklabels(plot_df.index)
ax.set_xlabel("Problem count")
ax.set_title("Representation-flip patterns per model (E=euclid, C=coord, V=vector)")
ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()
plt.savefig(OUT_DIR / "fig_rep_flip_stacked.png", dpi=200)
plt.close()
print(f"[DONE] Saved stacked bar figure to {OUT_DIR / 'fig_rep_flip_stacked.png'}")

# Pairwise transfer heatmap: models x pairs
heat = df_pairs.set_index("model")[["rate_EC_when_V_fails","rate_CV_when_E_fails","rate_EV_when_C_fails"]]
heat = heat.loc[sorted(heat.index)]
plt.figure(figsize=(8, max(4, 0.4 * len(heat))))
im = plt.imshow(heat.values, aspect="auto", cmap="Blues", vmin=0, vmax=1)
plt.colorbar(im, label="Transfer rate (0..1)")
plt.yticks(np.arange(len(heat.index)), heat.index)
plt.xticks(np.arange(3), ["EC | V fails", "CV | E fails", "EV | C fails"], rotation=20)
plt.title("Pair transfer when third representation fails")
plt.tight_layout()
plt.savefig(OUT_DIR / "fig_pairwise_transfer_heatmap.png", dpi=200)
plt.close()
print(f"[DONE] Saved pairwise transfer heatmap to {OUT_DIR / 'fig_pairwise_transfer_heatmap.png'}")

# final message
print("\nAll done. CSVs and figures are under runs/analysis/.")
