"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

LINE = "Insert coin, press B4 — I've been holding the last chocolate bar all night, waiting for someone sweet."


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
