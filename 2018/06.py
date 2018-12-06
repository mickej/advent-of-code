#!/usr/bin/env python3

import sys, operator
import numpy as np

SIZE = 500
TOTAL_DISTANCE = 10000

rows = sys.stdin.readlines()

def build_coordinates_with_ids(rows):
    coordinates = {}
    for i, r in enumerate(rows):
        coordinate = r[:-1].split(", ")
        coordinate = (int(coordinate[0]), int(coordinate[1]))
        coordinates[i + 1] = coordinate

    return coordinates

def calculate_distance(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def find_closests(coordinates, x, y):
    closest = ([], sys.maxsize)
    for coordinate_key in coordinates:
        coordinate = coordinates[coordinate_key]
        distance = calculate_distance(x, coordinate[0], y, coordinate[1])
        if distance == closest[1]:
            closest[0].append(coordinate_key)
        elif distance < closest[1]:
            closest = ([coordinate_key], distance)

    return closest

def build_matrix(coordinates):
    matrix = np.zeros((SIZE, SIZE))
    for r in range(SIZE):
        for c in range(SIZE):
            closests = find_closests(coordinates, c, r)
            if len(closests[0]) > 1:
                matrix[r, c] = -1
            elif len(closests[0]) == 1:
                matrix[r, c] = closests[0][0]

    return matrix

def matrix_stats(matrix):
    unique, counts = np.unique(matrix, return_counts=True)
    return dict(zip(unique, counts))

def remove_infinite(stats, matrix):
    for r in range(SIZE):
        stats.pop(matrix[0, r], None)
        stats.pop(matrix[SIZE - 1, r], None)
        stats.pop(matrix[r, 0], None)
        stats.pop(matrix[r, SIZE - 1], None)

    return stats

def find_largest_area(coordinates, matrix):
    stats = remove_infinite(matrix_stats(matrix), matrix)
    stats.pop(-1, None)
    return max(stats.items(), key=operator.itemgetter(1))

def region_with_distance(coordinates):
    m = np.zeros((SIZE, SIZE))
    for r in range(SIZE):
        for c in range(SIZE):
            if sum([calculate_distance(c, coordinates[coord][0], r, coordinates[coord][1]) for coord in coordinates]) < TOTAL_DISTANCE:
                m[r, c] = 1

    return m

def part1():
    coordinates = build_coordinates_with_ids(rows)
    matrix = build_matrix(coordinates)
    print("Part1", find_largest_area(coordinates, matrix))

def part2():
    m = region_with_distance(build_coordinates_with_ids(rows))
    print("Part2", matrix_stats(m))


part1()
part2()
