#!/usr/bin/env python3

import sys, re
from collections import namedtuple
from operator import attrgetter
import itertools

regex = r"position=<(.+[0-9]+), (.[0-9]+)> velocity=<(.[0-9]+), (.[0-9]+)>"
Point = namedtuple('Point', ['x', 'y', 'vx', 'vy'])

def to_point(row):
    p = re.findall(regex, row)[0]
    return Point(int(p[0]), int(p[1]), int(p[2]), int(p[3]))

def read_points(rows):
    return list(map(to_point, rows))

def move_points(points):
    new_points = []
    for p in points:
        new_points.append(Point(p.x + p.vx, p.y + p.vy, p.vx, p.vy))
    return new_points

def print_points(points):
    points = sorted(points, key=attrgetter('y', 'x'))
    min_x = min(points, key=attrgetter('x'))
    max_x = max(points, key=attrgetter('x'))
    min_y = min(points, key=attrgetter('y'))
    max_y = max(points, key=attrgetter('y'))

    width = abs(max_x.x - min_x.x) + 1
    height = abs(max_y.y - min_y.y) + 1

    if height > 15:
        return

    for model, group in itertools.groupby(points, lambda x : x.y):
        row = ['.'] * width
        for point in group:
            row[point.x - min_x.x] = "#"

        print(''.join(row))

def move_and_print(points, start, end):
    for i in range(end):
        points = move_points(points)
        if i >= start:
            print("Second:", i + 1)
            print_points(points)

def part1(points):
    move_and_print(points, 10238, 10240)


rows = sys.stdin.readlines()

points = read_points(rows)
part1(points)
