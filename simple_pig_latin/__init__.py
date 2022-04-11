# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

def pig_it(text):
    words = text.split(" ")
    spun_words = map(pig, words)

    return " ".join(spun_words)


def pig(word):
    chars = [char for char in word]

    head = chars[0]

    if head in '!?':
        return word

    tail = chars[1:]

    return "".join([*tail, head, *"ay"])
