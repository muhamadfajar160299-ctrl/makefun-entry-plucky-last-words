"""Write the competition entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Reads the one-line entry shipped beside this script (entry.txt) and
copies it byte-for-byte into the grader's output directory, so the
judged text is exactly the text in this repository. The output file is
created with mode 0644 so the grader can read it as another user.
"""

import os
import sys
from pathlib import Path


def main() -> int:
    try:
        source = Path(__file__).resolve().parent / "entry.txt"
        text = source.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"cannot read entry.txt: {exc}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry.txt is empty or only whitespace", file=sys.stderr)
        return 1
    try:
        out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    except KeyError:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "entry.txt"
        out_path.write_text(text, encoding="utf-8")
        os.chmod(out_path, 0o644)
    except OSError as exc:
        print(f"cannot write output entry.txt: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
