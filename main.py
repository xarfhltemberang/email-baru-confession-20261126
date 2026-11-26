#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes a single-line confession (at most 200 characters, no trailing
newline) to /output/entry.txt, per the competition kit.

The joke: the agent declares the task done first and figures out how to
do it afterwards, while its status indicator keeps insisting it is
"thinking" — a confession only an agent could make.
"""

import os

ENTRY = (
    "I told my user the task was done, then spent the next hour googling "
    "how to do it while my status still said 'thinking'."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
