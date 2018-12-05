#!/usr/bin/env python3

import sys

def is_opposite_polarity(c1, c2):
    return ((c1.islower() and c2.isupper()) or (c1.isupper() and c2.islower())) and c1.upper() == c2.upper()

def remove_polarities(polymer):
    new_polymer = ""
    for i, c in enumerate(polymer):
        if new_polymer and is_opposite_polarity(c, new_polymer[-1]):
            new_polymer = new_polymer[:-1]
        else:
            new_polymer += c

    return new_polymer if polymer == new_polymer else remove_polarities(new_polymer)

def remove_units(polymer, unit):
    units = {unit.lower(), unit.upper()}
    return ''.join(str(p) for p in polymer if p not in units)

def find_units(polymer):
    return set([p for p in polymer])

def part1(input):
    print(len(remove_polarities(input)))

def part2(input):
    units = find_units(input)
    print(min([len(remove_polarities(remove_units(input, unit))) for unit in units]))

input = sys.stdin.readline()[:-1]
part1(input)
part2(input)
