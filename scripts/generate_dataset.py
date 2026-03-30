import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import os
from dataset_specs.dataset import PROBLEMS

BASE_DIR = "problems/exp1"
REQUIRED_FIELDS = {"id", "category", "coord", "euclid", "vector", "answer"}

def validate_problem(problem: dict):
    missing = REQUIRED_FIELDS - problem.keys()
    if missing:
        raise ValueError(
            f"Problem {problem.get('id', '<unknown>')} missing fields: {missing}"
        )

def write_file(path: str, content):
    # This converts integers/floats to strings so .strip() won't crash
    content_str = str(content) 
    with open(path, "w", encoding="utf-8") as f:
        f.write(content_str.strip() + "\n")


def generate_files():
    count = 0

    for problem in PROBLEMS:
        validate_problem(problem)

        pid = problem["id"]
        category = problem["category"]

        category_dir = os.path.join(BASE_DIR, category)
        os.makedirs(category_dir, exist_ok=True)

        files = {
            f"{pid}_coord.txt": problem["coord"],
            f"{pid}_euclid.txt": problem["euclid"],
            f"{pid}_vector.txt": problem["vector"],
            f"{pid}_answer.txt": problem["answer"],
        }

        for filename, content in files.items():
            path = os.path.join(category_dir, filename)
            write_file(path, content)

        count += 1

    print(f"[DONE] Generated files for {count} problems.")

if __name__ == "__main__":
    generate_files()
