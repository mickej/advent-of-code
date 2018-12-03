#!/usr/bin/env python3

import sys
import numpy as np

def fill_matrix(matrix, row):
    a = row.split(" @ ")
    id = a[0][1:]
    b = a[1].split(": ")
    start = list(map(int, b[0].split(",")))
    size = list(map(int, b[1].split("x")))

    for x in range(start[1], start[1] + size[1]):
        for y in range(start[0], start[0] + size[0]):
            if matrix[x, y] == 0:
                matrix[x, y] = id
            else:
                matrix[x, y] = -1

    return matrix

def create_matrix(rows):
    matrix = np.zeros((1000, 1000))
    for r in rows:
        matrix = fill_matrix(matrix, r)

    return matrix

rows = sys.stdin.readlines()

matrix = create_matrix(rows)
unique, counts = np.unique(matrix, return_counts=True)
print(dict(zip(unique, counts))[-1])
