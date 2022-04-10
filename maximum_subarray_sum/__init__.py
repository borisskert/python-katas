# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python

import functools


def max_sequence(arr):
    _, maximum = functools.reduce(find, arr, (0, 0))
    return maximum


def find(sums, value):
    current_sum, maximum = sums

    current_sum = max([0, current_sum + value])
    maximum = max([maximum, current_sum])

    return current_sum, maximum
