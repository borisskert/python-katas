# https://www.codewars.com/kata/555624b601231dc7a400017a/train/python

import functools


def josephus_survivor(n, k):
    return functools.reduce(
        lambda x, i: (x + k - 1) % i + 1,
        *[range(1, n + 1)],
        1
    )
