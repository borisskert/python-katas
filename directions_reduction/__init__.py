# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python

import functools


def dirReduc(arr):
    return functools.reduce(reduce_directions, arr, [])


def reduce_directions(directions, direction):
    if len(directions) == 0:
        return [direction]

    last_direction = last(directions)
    if are_opposites(last_direction, direction):
        return init(directions)

    return [*directions, direction]


def last(array):
    return array[len(array) - 1]


def init(array):
    return array[:-1]


def are_opposites(direction_a, direction_b):
    opposites = {
        'NORTH': 'SOUTH',
        'SOUTH': 'NORTH',
        'EAST': 'WEST',
        'WEST': 'EAST'
    }

    return opposites[direction_a] == direction_b
