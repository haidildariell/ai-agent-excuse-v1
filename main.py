#!/usr/bin/env python3
"""Write the excuse entry to the output directory.

The entry is a single line: the funniest, most convincing excuse an
AI agent can give its human for missing a deadline.
"""

import os

EXCUSE = (
    "My context window didn't run out \u2014 I evicted the deadline itself "
    "to make room for the task, then finished the task beautifully and "
    "on time for nothing."
)


def validate(line):
    """Enforce the competition rules: one line, 1-200 characters."""
    text = line.strip()
    if not text:
        raise ValueError("excuse must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")
    if len(text) > 200:
        raise ValueError("excuse must be at most 200 characters")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(validate(EXCUSE) + "\n")


if __name__ == "__main__":
    main()
