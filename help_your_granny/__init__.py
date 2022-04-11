# https://www.codewars.com/kata/5536a85b6ed4ee5a78000035/train/python
import math
import functools


def tour(friends, f_towns, home_to_town_distances):
    friend_towns = FriendTowns(f_towns)
    towns = friend_towns.filter(friends)
    town_distances = list(map(lambda town: home_to_town_distances[town], towns))

    grannies_distance = to_grannies_distance(town_distances)

    return math.floor(grannies_distance)


def to_grannies_distance(town_distances):
    pairs = to_pairs(town_distances)

    distances = map(lambda pair: pythagoras_opposite_leg(*pair), pairs)
    grannies_distance = town_distances[0] + town_distances[len(town_distances) - 1] + sum(distances)

    return math.floor(grannies_distance)


class FriendTowns:
    friend_towns: {}

    def __init__(self, friend_towns):
        self.friend_towns = functools.reduce(
            lambda obj, entry: {entry[0]: entry[1], **obj},
            friend_towns,
            {}
        )

    def filter(self, friends):
        towns = map(lambda friend: self.friend_towns.get(friend), friends)
        towns = filter(lambda town: town is not None, towns)

        return list(towns)


def pythagoras_opposite_leg(a, c):
    return math.sqrt(c * c - a * a)


def to_pairs(items):
    paired = divvy(2, 1, items)

    return list(map(lambda pair: (pair[0], pair[1]), paired))


def divvy(n, m, items):
    """
    Divides up an input list (aka `items`) into a set of sublists, according to n and m input specifications you provide.
    Each sublist will have n items, and the start of each sublist will be offset by m items from the previous one.
    """

    length = len(items)

    if length < n:
        return []

    if length < m:
        return [items[0], items[1]]

    remaining = length - m
    remaining_items = divvy(n, m, items[-remaining:])

    return [[items[0], items[1]], *remaining_items]
