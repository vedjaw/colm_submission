import pandas as pd
from pathlib import Path

# ===============================
# Load all score CSVs
# ===============================
SCORES_DIR = Path("runs/scores_rep_to_euclid")

dfs = []
for csv_file in SCORES_DIR.glob("exp1_*.csv"):
    model = csv_file.stem.replace("exp1_", "")
    df = pd.read_csv(csv_file)
    df["model"] = model
    dfs.append(df)

scores = pd.concat(dfs, ignore_index=True)

# ===============================
# Normalize correctness labels (STRICT)
# ===============================
def _norm_correct(x):
    if pd.isna(x):
        return None
    s = str(x).strip().lower()
    if s in ("true", "yes", "y", "1"):
        return 1
    if s in ("false", "no", "n", "0"):
        return 0
    return None

scores["correct_strict"] = scores["correct"].apply(_norm_correct)

# ===============================
# Accuracy by representation (core table)
# ===============================
rep_accuracy = (
    scores
    .groupby(["model", "representation"])["correct_strict"]
    .mean()
    .round(2)
    .reset_index()
    .pivot(index="model", columns="representation", values="correct_strict")
    .reset_index()
)

# Ensure column order
rep_cols = ["coord", "euclid", "vector"]
rep_accuracy = rep_accuracy[["model"] + rep_cols]

# ===============================
# Geometry sensitivity calculations
# ===============================
rep_accuracy["best_performing_geometry"] = rep_accuracy[rep_cols].idxmax(axis=1)

best_vals = rep_accuracy[rep_cols].max(axis=1)
worst_vals = rep_accuracy[rep_cols].min(axis=1)

# Avoid divide-by-zero
rep_accuracy["accuracy_diff"] = (best_vals - worst_vals).round(4)
rep_accuracy["percent_diff"] = ((best_vals - worst_vals) * 100).round(2)

# ===============================
# Invariance@3 (Correct on all 3 geometries)
# ===============================
pivot_correct = scores.pivot_table(
    index=["model", "problem"],
    columns="representation",
    values="correct_strict",
    aggfunc="first"
).dropna()

pivot_correct["correct_all3"] = (
    (pivot_correct["coord"] == 1) &
    (pivot_correct["euclid"] == 1) &
    (pivot_correct["vector"] == 1)
).astype(int)

invariance3 = (
    pivot_correct.groupby("model")["correct_all3"]
    .mean()
    .reset_index()
    .rename(columns={"correct_all3": "Invariance@3"})
)

# ===============================
# Consistency@3 (answers identical)
# ===============================
pivot_pred = scores.pivot_table(
    index=["model", "problem"],
    columns="representation",
    values="predicted",
    aggfunc="first"
).dropna()

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

consistency3["Inconsistency_rate"] = (1 - consistency3["Consistency@3"]).round(3)

# ===============================
# Merge everything into final table
# ===============================
final_table = rep_accuracy.merge(invariance3, on="model", how="left")
final_table = final_table.merge(consistency3, on="model", how="left")

# Round
final_table[["Invariance@3", "Consistency@3", "Inconsistency_rate"]] = final_table[
    ["Invariance@3", "Consistency@3", "Inconsistency_rate"]
].round(3)

# ===============================
# Final output
# ===============================
final_table = final_table[
    [
        "model",
        "coord",
        "euclid",
        "vector",
        "best_performing_geometry",
        "accuracy_diff",
        "percent_diff",
        "Invariance@3",
        "Consistency@3",
        "Inconsistency_rate"
    ]
]

print("\n=== Geometry Robustness + Invariance Summary (Final) ===")
print(final_table)

# ===============================
# Save output
# ===============================
OUT_DIR = Path("runs/analysis")
OUT_DIR.mkdir(parents=True, exist_ok=True)

final_table.to_csv(
    OUT_DIR / "geometry_invariance_summary.csv",
    index=False
)

print(f"\n[DONE] Saved to runs/analysis/geometry_invariance_summary.csv")
