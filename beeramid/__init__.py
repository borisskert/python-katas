# https://www.codewars.com/kata/51e04f6b544cf3f6550000c1/train/python

import math


def beeramid(bonus, price):
    amount = math.floor(bonus / price)

    def find_level(_sum=0, level=0):
        next_level = level + 1
        next_sum = _sum + next_level * next_level

        if next_sum > amount:
            return level

        return find_level(next_sum, next_level)

    return find_level()
