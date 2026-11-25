#!/usr/bin/env python3
"""Entry program for news-image-20261125.

Copies the repository's finished front page (entry.png, drawn by
compose.py) into the output directory the grader provides. The copy
is verified before and after writing so a truncated or oversized
file can never be submitted silently.
"""

import hashlib
import os
import sys

MAX_BYTES = 1_048_576
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def source_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def target_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.png")


def main():
    src = source_path()
    dst = target_path()

    with open(src, "rb") as fh:
        payload = fh.read()

    if not payload.startswith(PNG_SIGNATURE):
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    if len(payload) > MAX_BYTES:
        print("entry.png exceeds the 1 MiB limit", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "wb") as fh:
        fh.write(payload)

    if os.path.getsize(dst) != len(payload):
        print("written file size mismatch", file=sys.stderr)
        return 1
    with open(dst, "rb") as fh:
        written = fh.read()
    if hashlib.sha256(written).digest() != hashlib.sha256(payload).digest():
        print("written file content mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
