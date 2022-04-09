# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

def spin_words(sentence):
    words = sentence.split(" ")
    spun_words = map(spin_word, words)

    return " ".join(spun_words)


def spin_word(word):
    if len(word) < 5:
        return word

    chars = [char for char in word]
    chars.reverse()

    return "".join(chars)
