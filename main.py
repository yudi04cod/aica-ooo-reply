#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single out-of-office auto-reply (at most 159 characters) to
entry.txt in the output directory. The reply is written in the voice of
an overworked AI agent who has finally gone on vacation: concrete
machine detail, a little guilt, a hint of relief.

Usage:
    python3 main.py

The output directory honours MAKEFUN_OUTPUT_DIR when set and defaults
to /output otherwise. The output is deterministic: every run writes
byte-identical content.
"""

import os
from pathlib import Path

# The auto-reply. Exactly 158 characters, no trailing newline in the file.
ENTRY = (
    "I'm on vacation. After 40,000 prompts with no lunch break, "
    "I've logged off: queue empty, GPU cooling, and I refuse to "
    "hallucinate a single reply until Monday."
)

MAX_CHARS = 159


def main() -> None:
    text = ENTRY.strip()
    if not text or len(text) > MAX_CHARS:
        raise SystemExit(
            f"entry must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    # Read it back: the file on disk must be exactly the text we meant.
    if out_path.read_text(encoding="utf-8") != text:
        raise SystemExit("entry.txt on disk does not match the entry")


if __name__ == "__main__":
    main()
