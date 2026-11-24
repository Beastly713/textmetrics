import argparse
import json


def analyze_text(text: str) -> dict[str, int]:
    return {
        "words": len(text.split()),
        "characters": len(text),
        "lines": len(text.splitlines()),
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="TextMetrics - CLI Text Analyzer"
    )
    parser.add_argument("text", help="Text to analyze")
    args = parser.parse_args()

    print(json.dumps(analyze_text(args.text), indent=2))