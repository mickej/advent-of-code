#!/usr/bin/env python3

import sys, operator, time

def large_enough(seq):
    return len(seq) > 3

def multiple_of(num, multiple=23):
    return num % multiple == 0

def next_index(current_index, marbles):
    if len(marbles) == current_index + 1:
        return 1
    else:
        return current_index + 2

def back_index(current_index, marbles):
    if current_index - 7 >= 0:
        return current_index - 7
    else:
        c = current_index - 7
        return len(marbles) - abs(c)

def play(players, last_marble_point):
    marbles = [0]
    current_index = 0
    current_player = 0

    score = {}
    for p in range(1, players + 1):
        score[p] = 0

    for i in range(1, last_marble_point + 1):
        current_player = current_player + 1 if current_player < players else 1

        if multiple_of(i):
            current_index = back_index(current_index, marbles)
            score[current_player] = score[current_player] + i
            score[current_player] = score[current_player] + marbles[current_index]
            del marbles[current_index]
        else:
            current_index = next_index(current_index, marbles)
            marbles.insert(current_index, i)


    print(max(score.items(), key=operator.itemgetter(1)))
    return marbles

play(473, 70904)
play(473, 70904 * 100)
