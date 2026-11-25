#!/usr/bin/env python3
"""The Houseplant Out-of-Office (make.fun).

Writes the entry -- one funny out-of-office auto-reply a houseplant would send --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "I'm out of office, out of water, and out of patience — I'll reply once someone remembers I exist. Probably never."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
