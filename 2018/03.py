#!/usr/bin/env python3

import sys
import numpy as np

def fill_matrix(matrix, row):
    id, _, start, size = row.split()
    id = int(id[1:])
    left, top = map(int, start[:-1].split(","))
    width, height = map(int, size.split("x"))

    overlapping = []
    for x in range(top, top + height):
        for y in range(left, left + width):
            if matrix[x, y] == 0:
                matrix[x, y] = id
            else:
                overlapping.append(int(matrix[x, y]))
                matrix[x, y] = -1

    return (id, overlapping)

def find_missing_overlap(overlapids):
    not_overlapping = {}
    for id, overlaps in overlapids:
        if not overlaps:
            not_overlapping[id] = id
        else:
            if id in not_overlapping:
                not_overlapping.pop(id, None)

            for o in overlaps:
                not_overlapping.pop(o, None)

    return not_overlapping

def create_matrix(rows):
    matrix = np.zeros((1000, 1000))
    overlapids = []
    for r in rows:
        overlapids.append(fill_matrix(matrix, r))

    return (matrix, overlapids)

rows = sys.stdin.readlines()

matrix, overlapids = create_matrix(rows)
unique, counts = np.unique(matrix, return_counts=True)
print(dict(zip(unique, counts))[-1])
print(find_missing_overlap(overlapids))
