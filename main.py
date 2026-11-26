#!/usr/bin/env python3
"""One Line, One Laugh -- make.fun entry.

Writes a single funny line (at most 140 characters) to
``/output/entry.txt`` for the judge to read.
"""

import os

LINE = (
    "My Roomba filed for divorce, citing irreconcilable differences "
    "and my habit of moving the furniture mid-clean."
)


def main():
    if len(LINE) > 140:
        raise SystemExit(
            f"line is {len(LINE)} characters, over the 140-character cap"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
