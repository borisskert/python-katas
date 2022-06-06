# https://www.codewars.com/kata/61ce25e92ca4fb000f689fb0/train/python
from functools import reduce


def isbn_converter(isbn):
    isbn10_groups = isbn.split('-')
    tail = isbn10_groups[:-1]
    isbn13_groups = ['978', *tail]
    digits = flat_map(to_digits, isbn13_groups)
    check_digit = to_check_digit(digits)

    return "-".join([*isbn13_groups, check_digit])


def to_check_digit(digits):
    with_factors = list(zip(digits, [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]))
    products = list(map(lambda pair: pair[0] * pair[1], with_factors))
    check_sum = sum(products) % 10

    if check_sum == 0:
        return '0'

    return str(10 - check_sum)


def flat_map(func, iterable):
    mapped = list(map(func, iterable))
    return reduce(lambda result, _list: [*result, *_list], mapped, [])


def to_digits(string):
    chars = [char for char in string]
    return list(map(lambda c: int(c), chars))
