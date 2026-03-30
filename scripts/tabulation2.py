#!/usr/bin/env python3
"""
tabulation_mcnemar_sm.py

Computes per-model geometry accuracies, Invariance@3, Consistency@3, and:
 - Bootstrap 95% CIs for accuracies (coord/euclid/vector), Invariance@3, and accuracy gap.
 - McNemar pairwise tests using statsmodels.mcnemar when available, else fallback to exact binomial.

Saves output to runs/analysis/geometry_invariance_summary_with_CIs_and_mcnemar.csv
"""

import math
import random
from pathlib import Path
import pandas as pd

# Try importing statsmodels' mcnemar
try:
    from statsmodels.stats.contingency_tables import mcnemar as sm_mcnemar
    HAS_STATSMODELS = True
except Exception:
    HAS_STATSMODELS = False

# ---------------------------
# Config
# ---------------------------
SCORES_DIR = Path("runs/scores_rep_to_euclid")
OUT_DIR = Path("runs/analysis")
OUT_DIR.mkdir(parents=True, exist_ok=True)

N_BOOTSTRAP = 2000          # number of bootstrap resamples (change if you want faster/longer)
CI_ALPHA = 0.05             # 95% CI

# ---------------------------
# Utility functions
# ---------------------------

def percentile_from_sorted(sorted_vals, q):
    if not sorted_vals:
        return None
    n = len(sorted_vals)
    rank = q * (n - 1)
    low = int(math.floor(rank))
    high = int(math.ceil(rank))
    if low == high:
        return sorted_vals[low]
    w = rank - low
    return sorted_vals[low] * (1 - w) + sorted_vals[high] * w

def compute_ci(samples, alpha=CI_ALPHA):
    if not samples:
        return (None, None)
    s = sorted(samples)
    low = percentile_from_sorted(s, alpha/2)
    high = percentile_from_sorted(s, 1 - alpha/2)
    return (low, high)

def mcnemar_exact_p(b, c):
    """Exact two-sided McNemar p-value using binomial tail (fallback)."""
    n_disc = b + c
    if n_disc == 0:
        return 1.0
    denom = 1 << n_disc  # 2**n_disc
    s = sum(math.comb(n_disc, k) for k in range(0, b + 1))
    p_lower = s / denom
    # p_upper = P(B >= b) computed as 1 - P(B <= b-1)
    s2 = sum(math.comb(n_disc, k) for k in range(0, b))
    p_upper = 1.0 - (s2 / denom)
    p_two = 2.0 * min(p_lower, p_upper)
    if p_two > 1.0:
        p_two = 1.0
    return p_two

def mcnemar_chi2(b, c, continuity=True):
    n = b + c
    if n == 0:
        return 0.0
    diff = abs(b - c)
    if continuity:
        diff = max(0.0, diff - 1.0)
    chi2 = (diff ** 2) / n
    return chi2

def run_mcnemar_with_statsmodels(b, c):
    """
    Build 2x2 contingency table and call statsmodels.mcnemar.
    Our convention: rows = A (0 or 1), cols = B (0 or 1)
      table = [[n00, n01],
               [n10, n11]]
    where:
      n10 = b (A=1,B=0)
      n01 = c (A=0,B=1)
    We'll pass exact=True to get exact test (if supported).
    """
    import numpy as np
    # We do not have n00 and n11 directly, but statsmodels needs the whole table.
    # For McNemar only discordant cells matter; set n00 and n11 to 0 (they won't affect exact p).
    table = np.array([[0, c],
                      [b, 0]])
    try:
        res = sm_mcnemar(table, exact=True)
        pval = float(res.pvalue)
        # res.statistic may not be meaningful for exact; fallback compute chi2
        try:
            chi2 = float(res.statistic)
        except Exception:
            chi2 = mcnemar_chi2(b, c)
    except Exception:
        # as some versions may error for this degenerate table shape; fallback to asymptotic
        res = sm_mcnemar(table, exact=False)
        pval = float(res.pvalue)
        try:
            chi2 = float(res.statistic)
        except Exception:
            chi2 = mcnemar_chi2(b, c)
    return pval, chi2

# ---------------------------
# Load all scores
# ---------------------------
dfs = []
for csv_file in SCORES_DIR.glob("exp1_*.csv"):
    model = csv_file.stem.replace("exp1_", "")
    df = pd.read_csv(csv_file)
    df["model"] = model
    dfs.append(df)

if not dfs:
    raise RuntimeError(f"No score CSVs found in {SCORES_DIR} (expected files exp1_*.csv)")

scores = pd.concat(dfs, ignore_index=True)

# Normalize correctness column to ints 0/1
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

models = sorted(scores["model"].unique())

rows = []
for model in models:
    sub = scores[scores["model"] == model].copy()

    # pivot correctness per problem
    pivot_corr = sub.pivot_table(
        index="problem",
        columns="representation",
        values="correct_strict",
        aggfunc="first"
    )

    pivot_corr = pivot_corr.dropna(subset=["coord", "euclid", "vector"])
    if pivot_corr.shape[0] == 0:
        n_problems = 0
    else:
        n_problems = pivot_corr.shape[0]
    pivot_corr = pivot_corr.astype(int) if n_problems > 0 else pivot_corr

    # pivot predicted answers (for consistency)
    pivot_pred = sub.pivot_table(
        index="problem",
        columns="representation",
        values="predicted",
        aggfunc="first"
    ).dropna(subset=["coord", "euclid", "vector"])

    # Base estimates
    coord_acc = pivot_corr["coord"].mean() if n_problems > 0 else 0.0
    euclid_acc = pivot_corr["euclid"].mean() if n_problems > 0 else 0.0
    vector_acc = pivot_corr["vector"].mean() if n_problems > 0 else 0.0

    # Invariance@3
    if n_problems > 0:
        pivot_corr["correct_all3"] = ((pivot_corr["coord"] == 1) & (pivot_corr["euclid"] == 1) & (pivot_corr["vector"] == 1)).astype(int)
        invariance3 = pivot_corr["correct_all3"].mean()
    else:
        invariance3 = 0.0

    # Consistency@3
    if not pivot_pred.empty:
        pivot_pred["consistent"] = ((pivot_pred["coord"] == pivot_pred["euclid"]) & (pivot_pred["coord"] == pivot_pred["vector"])).astype(int)
        consistency3 = pivot_pred["consistent"].mean()
    else:
        consistency3 = 0.0
    inconsistency_rate = 1.0 - consistency3

    best_perf_geom = max([("coord", coord_acc), ("euclid", euclid_acc), ("vector", vector_acc)], key=lambda x: x[1])[0]
    accuracy_gap = max(coord_acc, euclid_acc, vector_acc) - min(coord_acc, euclid_acc, vector_acc)

    # ---------------------------
    # Bootstrapping (resample problems)
    # ---------------------------
    coord_samples = []
    euclid_samples = []
    vector_samples = []
    invariance_samples = []
    gap_samples = []

    problem_ids = list(pivot_corr.index)
    if len(problem_ids) == 0:
        coord_ci = (0.0, 0.0); euclid_ci = (0.0, 0.0); vector_ci = (0.0, 0.0)
        invariance_ci = (0.0, 0.0); gap_ci = (0.0, 0.0)
    else:
        rng = random.Random(12345)
        for _ in range(N_BOOTSTRAP):
            sample_ids = [rng.choice(problem_ids) for _ in range(len(problem_ids))]
            sampled = pivot_corr.loc[sample_ids]
            coord_samples.append(sampled["coord"].mean())
            euclid_samples.append(sampled["euclid"].mean())
            vector_samples.append(sampled["vector"].mean())
            invariance_samples.append(sampled["correct_all3"].mean())
            gap_samples.append(sampled[["coord","euclid","vector"]].max(axis=1).mean() - sampled[["coord","euclid","vector"]].min(axis=1).mean())

        coord_ci = compute_ci(coord_samples)
        euclid_ci = compute_ci(euclid_samples)
        vector_ci = compute_ci(vector_samples)
        invariance_ci = compute_ci(invariance_samples)
        gap_ci = compute_ci(gap_samples)

    # ---------------------------
    # McNemar pairwise tests
    # ---------------------------
    def pair_mcnemar(col_a, col_b):
        both = pivot_corr[[col_a, col_b]].dropna()
        b = int(((both[col_a] == 1) & (both[col_b] == 0)).sum())
        c = int(((both[col_a] == 0) & (both[col_b] == 1)).sum())
        if HAS_STATSMODELS:
            try:
                pval, chi2 = run_mcnemar_with_statsmodels(b, c)
            except Exception:
                pval = mcnemar_exact_p(b, c)
                chi2 = mcnemar_chi2(b, c)
        else:
            pval = mcnemar_exact_p(b, c)
            chi2 = mcnemar_chi2(b, c)
        return b, c, pval, chi2

    b1, c1, p_ce, chi2_ce = pair_mcnemar("coord", "euclid")
    b2, c2, p_cv, chi2_cv = pair_mcnemar("coord", "vector")
    b3, c3, p_ev, chi2_ev = pair_mcnemar("euclid", "vector")

    row = {
        "model": model,
        "coord": round(coord_acc, 4),
        "coord_ci_low": round(coord_ci[0], 4) if coord_ci[0] is not None else None,
        "coord_ci_high": round(coord_ci[1], 4) if coord_ci[1] is not None else None,
        "euclid": round(euclid_acc, 4),
        "euclid_ci_low": round(euclid_ci[0], 4) if euclid_ci[0] is not None else None,
        "euclid_ci_high": round(euclid_ci[1], 4) if euclid_ci[1] is not None else None,
        "vector": round(vector_acc, 4),
        "vector_ci_low": round(vector_ci[0], 4) if vector_ci[0] is not None else None,
        "vector_ci_high": round(vector_ci[1], 4) if vector_ci[1] is not None else None,
        "best_performing_geometry": best_perf_geom,
        "accuracy_gap": round(accuracy_gap, 4),
        "gap_ci_low": round(gap_ci[0], 4) if gap_ci[0] is not None else None,
        "gap_ci_high": round(gap_ci[1], 4) if gap_ci[1] is not None else None,
        "percent_diff": round(accuracy_gap * 100, 2),
        "Invariance@3": round(invariance3, 4),
        "invariance3_ci_low": round(invariance_ci[0], 4) if invariance_ci[0] is not None else None,
        "invariance3_ci_high": round(invariance_ci[1], 4) if invariance_ci[1] is not None else None,
        "Consistency@3": round(consistency3, 4),
        "Inconsistency_rate": round(inconsistency_rate, 4),
        "mc_p_coord_euclid": p_ce,
        "mc_chi2_coord_euclid": round(chi2_ce, 4),
        "mc_p_coord_vector": p_cv,
        "mc_chi2_coord_vector": round(chi2_cv, 4),
        "mc_p_euclid_vector": p_ev,
        "mc_chi2_euclid_vector": round(chi2_ev, 4),
        "mcnemar_b_coord_euclid": b1,
        "mcnemar_c_coord_euclid": c1,
        "mcnemar_b_coord_vector": b2,
        "mcnemar_c_coord_vector": c2,
        "mcnemar_b_euclid_vector": b3,
        "mcnemar_c_euclid_vector": c3,
        "n_problems_evaluated": n_problems
    }
    rows.append(row)

# ---------------------------
# Final DataFrame and save
# ---------------------------
final_df = pd.DataFrame(rows)

# reorder and keep existing columns
cols = [
    "model",
    "coord", "coord_ci_low", "coord_ci_high",
    "euclid", "euclid_ci_low", "euclid_ci_high",
    "vector", "vector_ci_low", "vector_ci_high",
    "best_performing_geometry",
    "accuracy_gap", "gap_ci_low", "gap_ci_high", "percent_diff",
    "Invariance@3", "invariance3_ci_low", "invariance3_ci_high",
    "Consistency@3", "Inconsistency_rate",
    "mc_p_coord_euclid", "mc_chi2_coord_euclid",
    "mc_p_coord_vector", "mc_chi2_coord_vector",
    "mc_p_euclid_vector", "mc_chi2_euclid_vector",
    "mcnemar_b_coord_euclid", "mcnemar_c_coord_euclid",
    "mcnemar_b_coord_vector", "mcnemar_c_coord_vector",
    "mcnemar_b_euclid_vector", "mcnemar_c_euclid_vector",
    "n_problems_evaluated"
]
cols = [c for c in cols if c in final_df.columns]
final_df = final_df[cols]

out_path = OUT_DIR / "geometry_invariance_summary_with_CIs_and_mcnemar.csv"
final_df.to_csv(out_path, index=False)

print("\n=== Geometry Invariance Summary (saved) ===")
pd.set_option("display.max_columns", 200)
print(final_df.to_string(index=False))
print(f"\nSaved to {out_path}")

if HAS_STATSMODELS:
    print("\nNote: statsmodels detected and used for McNemar exact test (preferred).")
else:
    print("\nNote: statsmodels NOT installed — used internal exact/chi2 fallback. To use statsmodels install it with: pip install statsmodels")
