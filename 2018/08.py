#!/usr/bin/env python3

import sys
from collections import namedtuple

Node = namedtuple('Node', ['child_quantity', 'metadata_quantity', 'metadata', 'children'])

def build_node_and_childs(entries):
    n = Node(int(entries.pop(0)), int(entries.pop(0)), [], [])

    for i in range(n.child_quantity):
        n.children.append(build_node_and_childs(entries))

    for i in range(n.metadata_quantity):
        meta = entries.pop(0)
        n.metadata.append(int(meta))

    return n

def sum_metadata(tree):
    return sum([sum_metadata(child) for child in tree.children]) + sum(tree.metadata)

def values(tree):
    if tree.child_quantity == 0:
        return sum(tree.metadata)

    return sum([values(tree.children[c - 1]) for c in tree.metadata if len(tree.children) >= c])

def part1(row):
    tree = build_node_and_childs(row.split())
    print(sum_metadata(tree))

def part2(row):
    tree = build_node_and_childs(row.split())
    print(values(tree))

row = sys.stdin.readlines()[0]

part1(row)
part2(row)
