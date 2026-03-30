import json
import re
import argparse
from pathlib import Path


def sanitize(model_name: str):
    return (
        model_name.replace("/", "_")
        .replace(":", "_")
        .replace(".", "_")
    )


def extract_numeric_answer(text: str):
    """
    STRICT extraction:
    ONLY extract numeric_answer field.
    NO validation. NO fallback to full text.
    """

    cleaned = text.strip()

    # remove markdown if present
    if cleaned.startswith("```json"):
        cleaned = cleaned[7:]
    elif cleaned.startswith("```"):
        cleaned = cleaned[3:]
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]

    cleaned = cleaned.strip()

    # ----------------------------
    # Try JSON parsing FIRST
    # ----------------------------
    try:
        parsed = json.loads(cleaned, strict=False)
        ans = parsed.get("numeric_answer", "")
        return str(ans).strip() if ans else None
    except:
        pass

    # ----------------------------
    # STRICT regex extraction ONLY
    # ----------------------------
    match = re.search(r'"numeric_answer"\s*:\s*"([^"]+)"', cleaned)

    if match:
        return match.group(1).strip()

    # ----------------------------
    # NOTHING else allowed
    # ----------------------------
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    args = parser.parse_args()

    model_dir = sanitize(args.model)

    RAW_DIR = Path("runs/raw_outputs") / model_dir
    PARSED_DIR = Path("runs/parsed_answers") / model_dir
    PARSED_DIR.mkdir(parents=True, exist_ok=True)

    failures = []
    success = 0

    for f in RAW_DIR.iterdir():
        if not f.is_file():
            continue

        raw_text = f.read_text(encoding="utf-8")

        predicted = extract_numeric_answer(raw_text)

        if not predicted:
            failures.append(f.name)
            continue

        out = {
            "predicted_answer": predicted,
            "reasoning": "",  # not needed
            "parse_method": "direct_json_or_regex"
        }

        (PARSED_DIR / f.name).write_text(
            json.dumps(out, indent=2),
            encoding="utf-8"
        )

        success += 1

    # failure log
    (PARSED_DIR / "parse_failures.csv").write_text(
        "filename\n" + "\n".join(failures),
        encoding="utf-8"
    )

    print(f"[DONE] Parsed {args.model}")
    print(f"  Successful: {success}")
    print(f"  Failed: {len(failures)}")


if __name__ == "__main__":
    main()