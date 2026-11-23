#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes the funniest one-line excuse a robot vacuum can give for
missing a spot, in the vacuum's own deadpan voice, to /output/entry.txt.
Deterministic: the same single line on every run.
"""

import os

ENTRY = (
    "Sensor log 07:42: the dust bunny under the sofa is load-bearing "
    "furniture, so I left it holding up the house."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
