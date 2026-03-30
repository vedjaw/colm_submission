import os
import argparse
import requests
from pathlib import Path
import time
import re
import json
import unicodedata

# ---------------- Numeric validation ----------------
NUMERIC_REGEX = re.compile(
    r"""
    -?\d+(\.\d+)?                 # integers / decimals
    | -?\d+/\d+                   # fractions
    | -?sqrt\(\d+\)               # sqrt(13)
    | -?\d+\s*\*\s*sqrt\(\d+\)    # 2*sqrt(5)
    | -?√\d+                      # √13
    | -?\d+\s*\*?\s*(?:pi|π)      # 8*pi, 8π, 8pi, -2*pi
    | -?(?:pi|π)                  # pi, π, -pi
    """,
    re.VERBOSE
)

def normalize_numeric(s: str) -> str:
    """Normalize Unicode and strip invisible whitespace."""
    return unicodedata.normalize("NFKC", s).strip()

def extract_json_answer(text: str):
    """
    Parse model output as JSON and extract reasoning + numeric answer.
    Returns (reasoning, numeric_answer, conversion) if valid.
    """
    # 1. Clean up potential markdown formatting from the LLM
    cleaned_text = text.strip()
    if cleaned_text.startswith("```json"):
        cleaned_text = cleaned_text[7:]
    elif cleaned_text.startswith("```"):
        cleaned_text = cleaned_text[3:]
    if cleaned_text.endswith("```"):
        cleaned_text = cleaned_text[:-3]
    cleaned_text = cleaned_text.strip()

    try:
        # 2. strict=False allows literal unescaped newlines inside strings
        parsed = json.loads(cleaned_text, strict=False)

        conversion = str(parsed.get("euclidean_conversion", "")).strip()
        reasoning = str(parsed.get("reasoning", "")).strip()
        numeric = str(parsed.get("numeric_answer", "")).strip()

    except Exception as e:
        # 3. Print the error so it doesn't fail silently
        print(f"  [DEBUG] JSON Parse Error: {e}")
        print("  [DEBUG] Attempting regex fallback extraction...")
        
        # Salvage numeric_answer and conversion if JSON is malformed
        num_match = re.search(r'"numeric_answer"\s*:\s*"([^"]+)"', cleaned_text)
        conv_match = re.search(r'"euclidean_conversion"\s*:\s*"([^"]+)"', cleaned_text)
        
        if not num_match:
            return None, None, None
            
        numeric = num_match.group(1).strip()
        conversion = conv_match.group(1).strip() if conv_match else "Extraction Failed"
        reasoning = "[Reasoning skipped: Extracted via regex due to malformed JSON]"

    if not numeric:
        return None, None, None

    numeric = normalize_numeric(numeric)

    # 4. Use fullmatch instead of match to ensure the *entire* string is valid
    if NUMERIC_REGEX.fullmatch(numeric):
        return reasoning, numeric, conversion
    else:
        print(f"  [DEBUG] Numeric validation failed for: '{numeric}'")
        return None, None, None


# ---------------- OpenRouter ----------------
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.environ.get("OPENROUTER_API_KEY")

if API_KEY is None:
    raise RuntimeError("OPENROUTER_API_KEY not set")


# ---------------- Model ----------------
MODEL = "Replace with Model Name by matching from OpenRouter"


# ---------------- Paths ----------------
BASE_PROBLEM_DIR = "problems/exp1"
RAW_BASE = "runs/raw_outputs"


# ---------------- Prompt ----------------
PROMPT_TEMPLATE = """You are a geometry expert. Your task is to convert a problem into a pure Euclidean format and then solve it.

You MUST follow ALL rules exactly.

──────────────── RULES ────────────────
1. Output MUST be valid JSON only.
2. Do NOT include markdown formatting, code blocks (like ```json), or extra text.
3. The JSON must contain EXACTLY three keys:
   - "euclidean_conversion"
   - "reasoning"
   - "numeric_answer"

4. "euclidean_conversion":
   - Translate the input problem into a formal, complete Euclidean geometry problem.
   - It must include all numerical values and constraints.
   - It must be self-contained (solvable without seeing the original prompt).
   - Do NOT use coordinate notation (e.g., (x,y)) here; use geometric properties (lengths, angles, etc.).

5. "reasoning":
   - Must clearly explain the mathematical steps to solve the converted problem.
   - May use words, symbols, and equations.
   - MUST NOT contain literal line breaks. If you need multiple lines, use the escaped string "\\n".

6. "numeric_answer":
   - MUST be a string.
   - MUST contain ONLY the final numeric answer.
   - Do NOT include words or units.

7. Allowed formats for "numeric_answer":
   - "5"
   - "3/2"
   - "sqrt(8)"
   - "2*sqrt(5)"
   - "8*pi" or "8π"

8. If any rule is violated, the output is considered WRONG.

──────────────── OUTPUT FORMAT ────────────────
{{
  "euclidean_conversion": "<standalone Euclidean version of the problem>",
  "reasoning": "<clear mathematical reasoning, using \\n for line breaks>",
  "numeric_answer": "<final numeric answer>"
}}

──────────────── PROBLEM ────────────────
{problem}
"""


def sanitize(model_name: str):
    return (
        model_name.replace("/", "_")
        .replace(":", "_")
        .replace(".", "_")
    )


# ---------------- Query ----------------
def query_openrouter(prompt: str, retries=3):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Geometry LLM Eval",
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a precise mathematical solver."},
            {"role": "user", "content": prompt}
        ],
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
            return data["choices"][0]["message"]["content"].strip()

        except Exception as e:
            print(f"[WARN] Request error (attempt {attempt+1}): {e}")
            time.sleep(2)

    return ""


# ---------------- Main ----------------
def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    model_dir = sanitize(MODEL)
    out_dir = Path(RAW_BASE) / model_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    for category in os.listdir(BASE_PROBLEM_DIR):
        cat_dir = Path(BASE_PROBLEM_DIR) / category

        # Ensure we only process if it's a directory
        if not cat_dir.is_dir():
            continue

        for coord_file in cat_dir.glob("*_coord.txt"):
            pid = coord_file.stem.replace("_coord", "")

            for rep in ["coord", "euclid", "vector"]:
                prob_path = cat_dir / f"{pid}_{rep}.txt"
                if not prob_path.exists():
                    continue

                prompt = PROMPT_TEMPLATE.format(
                    problem=prob_path.read_text(encoding="utf-8")
                )

                print(f"[RUNNING] {MODEL} | {pid} | {rep}")

                output = query_openrouter(prompt)
                
                # Unpack all 3 variables here
                reasoning, numeric, conversion = extract_json_answer(output)

                if numeric:
                    print(f"  ✔ VALID OUTPUT | Answer: {numeric}")
                else:
                    print("  ✘ INVALID OUTPUT")

                # Save full JSON output (conversion + reasoning + numeric answer)
                (out_dir / f"{pid}_{rep}.txt").write_text(
                    output, encoding="utf-8"
                )


if __name__ == "__main__":
    main()