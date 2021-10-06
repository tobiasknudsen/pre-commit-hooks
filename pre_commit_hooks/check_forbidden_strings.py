# !/usr/bin/env python

# Strongly influenced by "DO NOT SUBMIT" https://github.com/jlebar/pre-commit-hooks/blob/master/check_do_not_submit.py

from __future__ import annotations

import os
import subprocess
import sys


def err(s: str) -> None:
    print(s, file=sys.stderr)

if len(sys.argv[1:]):
    res = subprocess.run(
        ["git", "grep", "-Hn", "--no-index", "-E", "|".join(sys.argv[1:])],
        capture_output=True,
    )

    if res.returncode == 0:
        err('Error: Unwanted string(s) was found!')
        err(res.stdout.decode("utf-8"))
        sys.exit(1)
    elif res.returncode == 2:
        err(f"Error invoking grep on {', '.join(sys.argv[1:])}:")
        err(res.stderr.decode("utf-8"))
        sys.exit(2)
