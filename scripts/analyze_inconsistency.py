import os
import csv
from collections import defaultdict

SCORES_DIR = "runs/scores_rep_to_euclid"

def analyze_scores(scores_file):
    # problem_id -> list of correctness values
    results = defaultdict(list)

    with open(scores_file, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            pid = row["problem"]
            correct = row["correct"].strip().lower() in ("true", "yes", "y", "1")
            results[pid].append(correct)

    total = len(results)
    all_correct = 0
    all_wrong = 0
    inconsistent = 0

    for pid, vals in results.items():
        if all(vals):
            all_correct += 1
        elif not any(vals):
            all_wrong += 1
        else:
            inconsistent += 1

    inconsistency_rate = inconsistent / total if total > 0 else 0.0

    return {
        "total_problems": total,
        "all_correct": all_correct,
        "all_wrong": all_wrong,
        "inconsistent": inconsistent,
        "inconsistency_rate": inconsistency_rate,
    }


def main():
    print("=== Inconsistency Analysis Across Models ===\n")

    for filename in sorted(os.listdir(SCORES_DIR)):
        if not filename.endswith(".csv"):
            continue

        scores_path = os.path.join(SCORES_DIR, filename)
        stats = analyze_scores(scores_path)

        model_name = filename.replace("exp1_", "").replace(".csv", "")

        print(f"Model: {model_name}")
        print(f"  Total problems: {stats['total_problems']}")
        print(f"  All representations correct: {stats['all_correct']}")
        print(f"  All representations wrong:   {stats['all_wrong']}")
        print(f"  Inconsistent across reps:    {stats['inconsistent']}")
        print(f"  Inconsistency rate:          {stats['inconsistency_rate']:.3f}")
        print("-" * 50)


if __name__ == "__main__":
    main()
