"""Everyday Things, Two Lines: rain explained to a 10-year-old.

Writes the two-line entry to /output/entry.txt.
Line 1 explains rain with one vivid analogy; line 2 says honestly
what the analogy maps and what it leaves out.
"""

import os

ENTRY = (
    "Rain is the sky wringing out a giant sponge, squeezing water over the "
    "streets until the clouds run dry.\n"
    "The sponge fits where the water comes from and why it stops, but it leaves "
    "out that rain can soak the ground for days without anyone squeezing."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
