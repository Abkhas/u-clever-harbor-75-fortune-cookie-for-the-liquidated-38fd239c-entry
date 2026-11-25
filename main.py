#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader (make.fun).

The program emits exactly one fortune-cookie line for a crypto trader
who was just liquidated: an oracular promise that turns on the loss.
It writes that line to entry.txt inside the output directory the
grader provides, and nothing else. Standard library only.
"""

import os
import sys

LINE = (
    "Your future holds great wealth — it is currently held by the "
    "exchange, pending your apology."
)

MAX_WORDS = 20
MAX_CHARS = 160


def output_dir():
    """Where the entry goes: the grader's env dir, /output, or local out/."""
    given = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if given:
        return given
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.getcwd(), "out")


def run():
    text = LINE
    if not text.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"entry is {len(text)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    if len(text.split()) > MAX_WORDS:
        print(
            f"entry is {len(text.split())} words, over the "
            f"{MAX_WORDS} limit",
            file=sys.stderr,
        )
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1

    folder = output_dir()
    os.makedirs(folder, exist_ok=True)
    with open(
        os.path.join(folder, "entry.txt"), "w", encoding="utf-8", newline="\n"
    ) as handle:
        handle.write(text + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(run())
