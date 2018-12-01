#!/usr/bin/env python3

import sys

def find_twice(frequencies, last = 0, visited = {}):
    for d in frequencies:
        last = last + d

        if last in visited:
            return last
        else:
            visited[last] = last

    return find_twice(frequencies, last, visited)

lines = sys.stdin.readlines()
frequencies = [int(line) for line in lines]
print(find_twice(frequencies))
