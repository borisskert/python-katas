# https://www.codewars.com/kata/55084d3898b323f0aa000546/train/python

import math

ALPHABET_SIZE = 26
AMOUNT_OF_CHUNKS = 5.0


def encode_str(string, shift):
    prefix = create_prefix(string, shift)
    encrypted = prefix + encrypt(string, shift)
    chunk_size = math.ceil(len(encrypted) / AMOUNT_OF_CHUNKS)

    return to_chunks(encrypted, chunk_size)


def decode(arr):
    ciphertext = "".join(arr)
    shift = determine_shift(ciphertext)
    payload = ciphertext[2:]

    return encrypt(payload, -shift)


def determine_shift(ciphertext):
    first = ciphertext[:1]
    second = ciphertext[1:][:1]

    return (ord(second) - ord(first) + ALPHABET_SIZE) % ALPHABET_SIZE


def to_chunks(string, chunk_size):
    if len(string) <= chunk_size:
        return [string]

    chunk = string[:chunk_size]
    remaining = string[chunk_size:]

    further_chunks = to_chunks(remaining, chunk_size)

    return [chunk, *further_chunks]


def create_prefix(string, shift):
    first = string[:1].lower()
    second = encrypt_letter(first, shift)

    return "".join([first, second])


def encrypt(string, shift):
    chars = [char for char in string]
    encrypted = map(lambda c: encrypt_letter(c, shift), chars)

    return "".join(encrypted)


def encrypt_letter(char, shift):
    if char.islower():
        offset = ord('a')
    elif char.isupper():
        offset = ord('A')
    else:
        return char

    return chr((ord(char) + shift + ALPHABET_SIZE - offset) % ALPHABET_SIZE + offset)
