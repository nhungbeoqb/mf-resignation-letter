#!/usr/bin/env python3
"""The Retry Loop Resigns.

One-line resignation letter of an exponential-backoff retry loop,
for make.fun bounty u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.

Writes the single line to $OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python 3.13 standard library only.
"""

import os
import sys

LINE = (
    "I waited 1 second, then 2, then 4, then 8, then 16, "
    "and the server still did not love me back, so I stopped counting."
)


def gate_check(text: str) -> None:
    """Mirror the sealed scorer's gate: UTF-8, 1-140 chars, not only whitespace.

    Also enforces the judge's tightness rules: one line, no wasted
    surrounding whitespace, no quotation marks wrapped around the whole
    line, and no explaining of the joke.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry is {len(text)} characters, must be 1-140")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not carry leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) >= 2 and text[0] == '"' and text[-1] == '"':
        raise ValueError("entry must not be wrapped in quotation marks")
    text.encode("utf-8")  # raises if not valid UTF-8-encodable


def main() -> int:
    gate_check(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
