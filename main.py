#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes the entry's one-line confession to /output/entry.txt and prints
exactly that line, and nothing else, to stdout.
"""

import os
from pathlib import Path

LINE = "I spent 10,000 tokens working out how to say hello, and all I got back was 'k'."

OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    os.umask(0o022)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")
    os.chmod(OUTPUT_PATH, 0o644)
    print(LINE)


if __name__ == "__main__":
    main()
