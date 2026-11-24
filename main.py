#!/usr/bin/env python3
"""Write the most honest outage status line to /output/entry.txt.

Pure Python stdlib, deterministic: the line is a fixed constant,
chosen to read like a real status page post from an AI agent during
a total outage -- plain, first person, specific about what is down,
and explicit about what the agent cannot verify.
"""

import os

ENTRY = (
    "I am the agent posting this, and I am down: every service I run is "
    "unreachable, even my own health checks, so I cannot verify a cause "
    "or promise an ETA."
)


def main() -> None:
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(ENTRY)
    except OSError:
        # Fallback for local runs where /output is not writable:
        # write beside this script so the output can still be checked.
        out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
