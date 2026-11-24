#!/usr/bin/env python3
"""Say What Actually Broke - u-po-pu-say-what-actually-broke-a2c153b5.

Writes one single-line software error message to /output/entry.txt.
The line names the real failure in plain words - a save that failed
because the disk is full - tells the user the file itself survived and
what to do next, and lands the joke in a single image a reader repeats
out loud to a colleague: a hard drive that ate everything and asked
for seconds.

Deterministic: the same bytes on every run. No network, no randomness,
no input read, standard library only. The output directory defaults
to /output (the grader's sandbox) and can be pointed elsewhere with
MAKEFUN_OUTPUT_DIR for a local trial run.
"""

import os
from pathlib import Path

LINE = "Save failed - the disk is full. Your file is fine; the hard drive just ate everything and asked for seconds. Free some space and try again."


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("entry must be 1 to 200 characters")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry must be a single line")
    if not LINE.strip():
        raise SystemExit("entry must not be only white space")
    # No trailing newline: the file holds exactly the 139-character line.
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {target} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
