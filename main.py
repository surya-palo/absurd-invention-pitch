#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance: a doormat that interviews visitors and only
lets in people who can pronounce your Wi-Fi password.

Stdlib only. Deterministic: the same sentence is written on every run.
"""

import os

ENTRY = (
    "A doormat that interrogates every visitor and only unlocks the door "
    "for anyone who can pronounce your Wi-Fi password correctly on the "
    "first try, so you never have to pretend you are not home again."
)

MAX_CHARS = 220


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
