#!/usr/bin/env python3

import sys, re, functools

regex = r"Step (.) must be finished before step (.) can begin."

def finished_order(row):
    return re.findall(regex, row)[0]

def next_step(steps, l):
    return [s for s in steps if all(b != s for (_, b) in l)]

def topological(steps, lines):
    order = ''
    while steps:
        cand = list(next_step(steps, lines))
        cand.sort()

        n = cand[0]
        order += n
        steps.remove(n)
        lines = [(a, b) for (a, b) in lines if a != n]

    return order

rows = sys.stdin.readlines()

lines = list(map(finished_order, rows))

steps = set([s[0] for s in lines] + [s[1] for s in lines])
print(topological(steps, lines))
