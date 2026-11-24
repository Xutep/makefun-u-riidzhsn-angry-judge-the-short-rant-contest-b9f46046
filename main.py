#!/usr/bin/env python3
"""Angry Judge entry: write one short rant to /output/entry.txt.

Deterministic by construction: the text is a fixed string, there is no
input, no clock, no randomness, no network and no environment read, so
every run writes byte-identical output.
"""

import os

MAX_CHARS = 400  # the contest gate: /output/entry.txt must be 1-400 chars

RANT = (
    "The self-checkout machine has decided I am a criminal. "
    "I scanned one baguette and it screamed UNEXPECTED ITEM IN THE "
    "BAGGING AREA, like I had smuggled a grand piano. "
    "Then a human watches me re-scan everything, slowly, "
    "while the queue judges my entire character. "
    "I came here to avoid people. "
    "Now six strangers know I buy oat milk."
)


def main() -> None:
    if not 1 <= len(RANT) <= MAX_CHARS or not RANT.strip():
        raise ValueError("rant must be 1-400 non-whitespace characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(RANT)


if __name__ == "__main__":
    main()
