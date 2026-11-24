#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App entry.

Writes the dating-app bio line to /output/entry.txt.
Deterministic: no network, no randomness, no time dependence.
"""

from pathlib import Path

LINE = "She asked me to be spontaneous. I froze, generated twelve options, and asked her to pick one."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the one-liner to /output/entry.txt with no trailing newline."""
    # Gate: 1-180 characters, single line, no trailing newline.
    assert 1 <= len(LINE) <= 180, "entry must be 1-180 characters"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE == LINE.strip(), "entry must not have leading/trailing whitespace"
    LINE.encode("utf-8")  # gate requires UTF-8 text
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
