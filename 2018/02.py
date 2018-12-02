#!/usr/bin/env python3

import sys

def count_duplicates(row):
    twice = 0
    thrice = 0
    for r in row:
        count = row.count(r)
        if count == 2 and twice == 0:
            twice = 1
        elif count == 3 and thrice == 0:
            thrice = 1

    return (twice, thrice)

rows = sys.stdin.readlines()
twice = 0
thrice = 0
for row in rows:
    tuple = count_duplicates(row)
    twice += tuple[0]
    thrice += tuple[1]

print(twice * thrice)
