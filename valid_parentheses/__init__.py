# https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python

import functools


def valid_parentheses(string):
    parentheses = [char for char in string]
    balance = functools.reduce(count, parentheses, 0)

    return balance == 0


def count(balance, char):
    if balance < 0:
        return balance

    if char == '(':
        return balance + 1

    if char == ')':
        return balance - 1

    return balance
