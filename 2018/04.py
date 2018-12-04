#!/usr/bin/env python3

import sys, operator

def guards_slept(rows):
    slept = {}
    for time, row in rows:
        if "Guard " in row:
            current_id = int(row.split()[1][1:])
            if current_id not in slept:
                slept[current_id] = {}
        elif "falls asleep" in row:
            fell_asleep = int(time[-2:])
        elif "wakes up" in row:
            woke_up = int(time[-2:])
            for i in range(fell_asleep, woke_up):
                slept[current_id][i] = slept[current_id].get(i, 0) + 1

    return slept

def find_sleepiest_guard(guards):
    minutes_slept = [(id, sum(guards[id].values())) for id in guards]
    guard_id = max(minutes_slept, key=operator.itemgetter(1))[0]
    return (guard_id, guards[guard_id])

def find_sleepiest_minute(minutes):
    return (0, 0) if not minutes.items() else max(minutes.items(), key=operator.itemgetter(1))

def find_minute(minutes_sleeping):
    return max(minutes_sleeping.items(), key=operator.itemgetter(1))[0]

def find_most_frequent_minute(guards):
    frequent_minute = [(id, find_sleepiest_minute(guards[id])) for id in guards]
    return max(frequent_minute, key= lambda x: x[1][1])

def strategy1(guards):
    guard = find_sleepiest_guard(guards)
    return guard[0] * find_sleepiest_minute(guard[1])[0]

def strategy2(guards):
    guard = find_most_frequent_minute(guards)
    return guard[0] * guard[1][0]

rows = sorted(sys.stdin.readlines())
rows = list(map(lambda r: (r[1:17], r[19:]), rows))
guards = guards_slept(rows)
print("Strategy1", strategy1(guards))
print("Strategy2", strategy2(guards))
