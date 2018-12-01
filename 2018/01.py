#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

frequencies = [int(line) for line in lines]
freq = sum(d for d in frequencies)
print(freq)
