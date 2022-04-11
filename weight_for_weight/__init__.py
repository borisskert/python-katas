# https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python

import functools


def order_weight(strng):
    return Weights.create_from(strng) \
        .sorted() \
        .to_string()


class Weights:
    weights: []

    def __init__(self, weights):
        self.weights = weights

    def sorted(self):
        sorted_weights = sorted(self.weights)
        return Weights(sorted_weights)

    def to_string(self):
        strings = map(lambda w: w.to_string(), self.weights)
        return ' '.join(strings)

    @staticmethod
    def create_from(strng):
        numbers = strng.split(' ')
        weights = map(lambda number: Weight(number), numbers)

        return Weights(weights)


class Weight:
    def __init__(self, raw):
        self.raw = raw
        self.cross_sum = to_cross_sum(raw)

    def __lt__(self, other):
        if self.cross_sum == other.cross_sum:
            return self.raw < other.raw

        return self.cross_sum < other.cross_sum

    def __eq__(self, other):
        return self.raw == other.raw

    def to_string(self):
        return self.raw


def to_cross_sum(raw):
    digits = map(lambda c: ord(c) - ord('0'), [char for char in raw])
    return functools.reduce(lambda a, b: a + b, digits, 0)
