import json
import csv
import argparse
from pathlib import Path


def sanitize(model_name: str):
    return (
        model_name.replace("/", "_")
        .replace(":", "_")
        .replace(".", "_")
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    args = parser.parse_args()

    model_dir = sanitize(args.model)

    PARSED_DIR = Path("runs/parsed_answers") / model_dir
    PROBLEM_DIR = Path("problems/exp1")   # 🔥 for gold answers
    OUT_FILE = Path("runs/scores") / f"exp1_{model_dir}.csv"
    SKIP_FILE = Path("runs/scores") / f"exp1_{model_dir}_skipped.csv"

    rows = []
    skipped = []

    seen = set()  # 🔥 prevent duplicates

    files = sorted(
        [f for f in PARSED_DIR.iterdir() if f.is_file() and f.name != "parse_failures.csv"]
    )

    for f in files:
        base = f.stem
        parts = base.split("_")

        if len(parts) < 2:
            skipped.append({"filename": f.name, "reason": "bad_filename_format"})
            continue

        representation = parts[-1]
        problem_id = "_".join(parts[:-1])
        category = problem_id.split("_")[0]

        key = (problem_id, representation)

        # 🔥 avoid duplicates
        if key in seen:
            continue
        seen.add(key)

        # ---------------- Load prediction ----------------
        try:
            parsed = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            skipped.append({"filename": f.name, "reason": "invalid_parsed_json"})
            continue

        pred = str(parsed.get("predicted_answer", "")).strip()

        # ---------------- Load gold ----------------
        gold_path = PROBLEM_DIR / category / f"{problem_id}_answer.txt"

        if not gold_path.exists():
            skipped.append({"filename": f.name, "reason": "missing_gold"})
            gold = ""
        else:
            gold = gold_path.read_text(encoding="utf-8").strip()

        # ---------------- Add row ----------------
        rows.append({
            "problem": problem_id,
            "category": category,
            "representation": representation,
            "predicted": pred,
            "gold": gold,
            "correct": ""   # keep empty (as you want)
        })

    # ---------------- Write CSV ----------------
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "problem",
                "category",
                "representation",
                "predicted",
                "gold",
                "correct"
            ]
        )
        writer.writeheader()
        writer.writerows(rows)

    # ---------------- Write skip log ----------------
    with open(SKIP_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["filename", "reason"]
        )
        writer.writeheader()
        writer.writerows(skipped)

    print(f"[DONE] Prepared sheet for {args.model} → {OUT_FILE}")
    print(f"  Rows written: {len(rows)}")
    print(f"  Skipped files: {len(skipped)}")
    print(f"  Skip log: {SKIP_FILE}")


if __name__ == "__main__":
    main()