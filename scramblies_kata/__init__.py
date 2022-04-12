# https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python

import functools


def scramble(s1, s2):
    counters = functools.reduce(increase, [char for char in s1], {})
    counters = functools.reduce(decrease, [char for char in s2], counters)

    return all(map(lambda i: i >= 0, counters.values()))


def increase(counters, char):
    count = counters.get(char) or 0
    counters[char] = count + 1

    return counters


def decrease(counters, char):
    count = counters.get(char) or 0
    counters[char] = count - 1

    return counters
