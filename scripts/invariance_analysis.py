import pandas as pd
from pathlib import Path

SCORES_DIR = Path("runs/scores_rep_to_euclid")

# ===============================
# Load all model CSVs
# ===============================
dfs = []
for csv_file in SCORES_DIR.glob("exp1_*.csv"):
    model = csv_file.stem.replace("exp1_", "")
    df = pd.read_csv(csv_file)
    df["model"] = model
    dfs.append(df)

scores = pd.concat(dfs, ignore_index=True)

# Normalize correctness
def _norm_correct(x):
    if pd.isna(x):
        return None
    s = str(x).strip().lower()
    if s in ("true", "yes", "y", "1"):
        return 1
    if s in ("false", "no", "n", "0"):
        return 0
    return None

scores["correct"] = scores["correct"].apply(_norm_correct)

# ===============================
# 1) Invariance@3 (Correct for all 3 geometries)
# ===============================
# pivot correctness per problem
pivot_correct = scores.pivot_table(
    index=["model", "problem"],
    columns="representation",
    values="correct",
    aggfunc="first"
)

# keep only problems with all 3 representations
pivot_correct = pivot_correct.dropna()

# correct in all 3 geometries
pivot_correct["correct_all3"] = (
    (pivot_correct["coord"] == 1) &
    (pivot_correct["euclid"] == 1) &
    (pivot_correct["vector"] == 1)
).astype(int)

# invariance@3 per model
invariance3 = (
    pivot_correct.groupby("model")["correct_all3"]
    .mean()
    .reset_index()
    .rename(columns={"correct_all3": "Invariance@3"})
)

# ===============================
# 2) Consistency@3 (answers identical)
# ===============================
pivot_pred = scores.pivot_table(
    index=["model", "problem"],
    columns="representation",
    values="predicted",
    aggfunc="first"
).dropna()

# identical answers?
pivot_pred["consistent"] = (
    (pivot_pred["coord"] == pivot_pred["euclid"]) &
    (pivot_pred["coord"] == pivot_pred["vector"])
).astype(int)

consistency3 = (
    pivot_pred.groupby("model")["consistent"]
    .mean()
    .reset_index()
    .rename(columns={"consistent": "Consistency@3"})
)

# ===============================
# 3) Inconsistency rate
# ===============================
consistency3["Inconsistency_rate"] = 1 - consistency3["Consistency@3"]

# ===============================
# Merge all results
# ===============================
final = invariance3.merge(consistency3, on="model")

# Round
final[["Invariance@3", "Consistency@3", "Inconsistency_rate"]] = final[
    ["Invariance@3", "Consistency@3", "Inconsistency_rate"]
].round(3)

print("\n=== Invariance & Consistency Summary ===")
print(final)

# Save
OUT_DIR = Path("runs/analysis")
OUT_DIR.mkdir(parents=True, exist_ok=True)
final.to_csv(OUT_DIR / "invariance_consistency_summary.csv", index=False)

# ===============================
# By problem family (category)
# ===============================
pivot_correct_cat = scores.pivot_table(
    index=["model", "category", "problem"],
    columns="representation",
    values="correct",
    aggfunc="first"
).dropna()

pivot_correct_cat["correct_all3"] = (
    (pivot_correct_cat["coord"] == 1) &
    (pivot_correct_cat["euclid"] == 1) &
    (pivot_correct_cat["vector"] == 1)
).astype(int)

invariance3_cat = (
    pivot_correct_cat.groupby(["model", "category"])["correct_all3"]
    .mean()
    .reset_index()
)

invariance3_cat.to_csv(
    OUT_DIR / "invariance_by_category.csv", index=False
)

print("\n[DONE] Saved:")
print(" - invariance_consistency_summary.csv")
print(" - invariance_by_category.csv")
