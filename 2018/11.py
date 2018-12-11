#!/usr/bin/env python3

import sys

def calculate_power(size, serial):
    power_grid = [[0] * size for _ in range(size)]
    for x in range(1, size + 1):
        for y in range(1, size + 1):
            rack_id = x + 10
            power_level = rack_id * y
            power_level += serial
            power_level *= rack_id
            power_level = int(str(power_level)[-3]) if power_level >= 100 else 0
            power_level -= 5

            power_grid[x - 1][y - 1] = power_level

    return power_grid

def calculate_square(x, y, power_grid, size):
    total = 0

    if x + size < len(power_grid):
        for ix in range(size):
            for iy in range(size):
                total += power_grid[x + ix][y + iy]

    return ((x + 1, y + 1), total)


def find_largest_square(power_grid, min_size, max_size):
    max_square = (0, 0, 0)

    for i in range(min_size, max_size + 1):
        for x in range(len(power_grid) - i + 1):
            for y in range(len(power_grid) - i + 1):
                square = calculate_square(x, y, power_grid, i)
                if square[1] > max_square[1]:
                    max_square = (square[0], square[1], i)

    return max_square

def part1():
    grid = calculate_power(300, 9445)
    print("Part1", find_largest_square(grid, 3, 3))


def part2():
    grid = calculate_power(300, 9445)
    largest = find_largest_square(grid, 13, 16)
    print("Part2", largest)

part1()
part2()
