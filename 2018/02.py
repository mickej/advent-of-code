#!/usr/bin/env python3

import sys

def diffed_indices(first, second):
    return [i for i, c in enumerate(first) if c != second[i]]

def is_secret(first, second):
    return len(diffed_indices(first, second)) == 1

def to_secret(first, second):
    diffs = diffed_indices(first, second)
    return first[:diffs[0]] + first[(diffs[0] + 1):]

def find_secret(rows):
    secret = [r1 for r1 in rows for r2 in rows if is_secret(r1, r2)]
    return to_secret(secret[0], secret[1])

rows = sys.stdin.readlines()
print(find_secret(rows))
