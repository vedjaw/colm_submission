import os
import argparse
import requests
from pathlib import Path
import time
import re

# ---------------- Numeric extraction ----------------
NUMERIC_REGEX = re.compile(
    r"""
    -?\d+(\.\d+)?        # integers / decimals
    | \d+/\d+            # fractions
    | sqrt\(\d+(\.\d+)?\)
    | √\d+(\.\d+)?
    | \d+\s*√\d+
    """,
    re.VERBOSE
)

def has_numeric(text: str) -> bool:
    if not text:
        return False
    return bool(NUMERIC_REGEX.search(text))


# ---------------- OpenRouter ----------------
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.environ.get("OPENROUTER_API_KEY")

if not API_KEY:
    raise RuntimeError("OPENROUTER_API_KEY not set")


# ---------------- MODEL ----------------
MODEL = "Replace with Model Name by matching from OpenRouter"


# ---------------- Paths ----------------
BASE_PROBLEM_DIR = "problems/exp1"
RAW_BASE = "runs/raw_outputs"


# ---------------- Prompt ----------------
PROMPT_TEMPLATE = """You are solving a mathematics problem.

STRICT OUTPUT RULES (must follow exactly):
- Output ONLY ONE final numeric answer
- Do NOT include any words, explanations, or symbols
- Do NOT include units (cm, degrees, etc.)
- Do NOT include approximation symbols (≈, ~)
- Allowed formats ONLY:
  • Integer: 5
  • Decimal: 3.25
  • Fraction: 3/4
  • Square root: sqrt(5)

Before answering, silently verify:
1) The answer is correct
2) The output is ONE number
3) The output matches the allowed formats

Problem:
{problem}

Final Answer:
"""


def sanitize(model_name: str):
    return (
        model_name.replace("/", "_")
        .replace(":", "_")
        .replace(".", "_")
    )


# ---------------- Query ----------------
def query_openrouter(prompt: str, retries=3) -> str:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Geometry LLM Eval",
    }

    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.0,
        "top_p": 1.0,
    }

    for attempt in range(retries):
        try:
            r = requests.post(
                OPENROUTER_URL,
                headers=headers,
                json=payload,
                timeout=60
            )
            r.raise_for_status()
            data = r.json()

            choices = data.get("choices", [])
            if not choices:
                print("[WARN] Empty choices — retrying")
                time.sleep(1)
                continue

            content = choices[0]["message"].get("content", "").strip()

            if content:
                return content

            print("[WARN] Empty content — retrying")
            time.sleep(1)

        except Exception as e:
            print(f"[WARN] Request error: {e}")
            time.sleep(2)

    return ""


# ---------------- Main ----------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default=MODEL)
    args = parser.parse_args()

    model_name = args.model
    model_dir = sanitize(model_name)

    out_dir = Path(RAW_BASE) / model_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    for category in sorted(os.listdir(BASE_PROBLEM_DIR)):
        cat_dir = Path(BASE_PROBLEM_DIR) / category

        for coord_file in sorted(cat_dir.glob("*_coord.txt")):
            pid = coord_file.stem.replace("_coord", "")

            for rep in ["coord", "euclid", "vector"]:
                prob_path = cat_dir / f"{pid}_{rep}.txt"
                if not prob_path.exists():
                    continue

                problem_text = prob_path.read_text(encoding="utf-8")

                prompt = PROMPT_TEMPLATE.format(problem=problem_text)

                print(f"[RUNNING] {model_name} | {pid} | {rep}")
                output = query_openrouter(prompt)

                if has_numeric(output):
                    print("  ✔ NUMERIC OUTPUT")
                else:
                    print("  ✘ NO NUMERIC OUTPUT")

                out_file = out_dir / f"{pid}_{rep}.txt"
                out_file.write_text(output, encoding="utf-8")


if __name__ == "__main__":
    main()
