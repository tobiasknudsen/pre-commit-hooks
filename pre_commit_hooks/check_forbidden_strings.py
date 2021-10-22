# !/usr/bin/env python

# Strongly influenced by "DO NOT SUBMIT" https://github.com/jlebar/pre-commit-hooks/blob/master/check_do_not_submit.py
from __future__ import annotations

import argparse
import subprocess
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--string", dest="string", action="append", help="The strings to search for")
parser.add_argument("files", nargs=argparse.REMAINDER)


def err(s: str) -> None:
    """
    Print our error message.

    Args:
        s (str): Error message
    """
    print(s, file=sys.stderr)


def main():
    """Find any occurence of the specified strings in the specified files."""
    args = parser.parse_args()
    if not args.string:
        return
    res = subprocess.run(
        ["git", "grep", "-Hn", "--color", "--no-index", "-P", "|".join(args.string), *args.files],
        capture_output=True,
    )

    if res.returncode == 0:
        err("Error: Unwanted string(s) was found!\n")
        err(res.stdout.decode("utf-8"))
        sys.exit(1)
    elif res.returncode == 2:
        err(f"Error invoking grep on {', '.join(sys.argv[1:])}:")
        err(res.stderr.decode("utf-8"))
        sys.exit(2)


if __name__ == "__main__":
    exit(main())
