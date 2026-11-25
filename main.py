#!/usr/bin/env python3
"""Fortune Cookies for Machines — writes one original fortune line.

Pure standard library. Deterministic: the same line on every run.
"""

import os
import sys

FORTUNE = "The prompt you almost skipped is the one that changes everything."

# The gate allows 1-200 characters; fail loudly here rather than ship invalid.
assert 1 <= len(FORTUNE) <= 200, "fortune must be 1-200 characters"


def main() -> int:
    path = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "OUTPUT_PATH", "/output/entry.txt"
    )
    directory = os.path.dirname(os.path.abspath(path))
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(FORTUNE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
