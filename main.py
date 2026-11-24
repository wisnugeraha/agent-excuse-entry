#!/usr/bin/env python3
"""make.fun entry: writes the agent's one-line excuse to /output/entry.txt.

The line is the competition's required text, emitted verbatim in UTF-8
with no trailing newline (the gate reads the file's whole content).
"""
import os

ENTRY = "The model did not hallucinate; it creatively reinterpreted the specification. The user was the weak link."
OUT = "/output/entry.txt"


def write_entry() -> None:
    """Write the excuse to the gate artifact, then confirm it on disk."""
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(OUT, "r", encoding="utf-8") as f:
        on_disk = f.read()
    if on_disk != ENTRY:
        raise SystemExit(f"on-disk entry mismatch: {on_disk!r}")
    print(f"Wrote entry to {OUT} ({len(ENTRY)} chars)")


def main():
    write_entry()


if __name__ == "__main__":
    main()
