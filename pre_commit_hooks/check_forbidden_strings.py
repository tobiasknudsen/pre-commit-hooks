# !/usr/bin/env python

# Strongly influenced by "DO NOT SUBMIT" https://github.com/jlebar/pre-commit-hooks/blob/master/check_do_not_submit.py
from __future__ import annotations
import argparse
import os
import subprocess
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--strings", dest="strings", type=str, nargs="+", help="Strings to search for")
parser.add_argument("files", nargs=argparse.REMAINDER)

def err(s: str) -> None:
    print(s, file=sys.stderr)

def main():
    args = parser.parse_args()
    if len(sys.argv[1:]):
        strings = ",".join(args.strings).split(",")
        res = subprocess.run(
            ["git", "grep", "-Hn", "--no-index", "-E", "|".join(strings), *args.files],
            capture_output=True,
        )

        if res.returncode == 0:
            err("Error: Unwanted string(s) was found!")
            err(res.stdout.decode("utf-8"))
            sys.exit(1)
        elif res.returncode == 2:
            err(f"Error invoking grep on {', '.join(sys.argv[1:])}:")
            err(res.stderr.decode("utf-8"))
            sys.exit(2)

if __name__ == "__main__":
    exit(main())