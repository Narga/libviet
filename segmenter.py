# -*- coding: utf-8 -*-

# import string
from __future__ import unicode_literals
from io import open


def char_in_word(char):
    return char.isalnum() or char == "-"


def to_unigrams(sentence):
    """
    Break a sentence into a list of unigrams.
    """
    unigrams = []
    current_uni = ""
    for char in sentence:
        if char_in_word(char):
            current_uni += char
        else:
            unigrams.append(current_uni)
            current_uni = ""

            # For now just skip all punctuations
            # if char not in string.whitespace:
            #     unigrams.append(char)

    return unigrams


def to_ngrams(unigrams, n):
    """
    Convert a list of unigrams into a list of n-grams.
    """
    ngrams = []

    for i in range(len(unigrams) - (n - 1)):
        ngrams.append(" ".join([unigrams[k] for k in range(i, i + n) ]))

    return ngrams


def to_bigrams(unigrams):
    return to_ngrams(unigrams, 2)


def to_trigram(unigrams):
    return to_ngrams(unigrams, 3)


def segmentize(sent, dictionary):
    """
    Break a sentence into a list of words.
    """
    uni = to_unigrams(sent)
    bi = to_bigrams(uni)
    tri = to_trigram(uni)

    len_uni = len(uni)
    len_bi = len(bi)
    len_tri = len(tri)

    segments = []

    i = 0
    # Very simple state machine.
    # TODO Think about training and backtracking.
    while i < len_uni:
        if i < len_tri and tri[i].lower() in dictionary:
            segments.append(tri[i])
            i += 3
        elif i < len_bi and bi[i].lower() in dictionary:
            segments.append(bi[i])
            i += 2
        else:
            segments.append(uni[i])
            i += 1

    return segments


def main():
    sent1 = "con mèo điên rất hâm anh ạ."
    sent2 = "Có mặt trong top 10 hầu hết đều là những công ty đa quốc gia và gây được tiếng tăm mạnh mẽ trên toàn cầu."

    dictionary = set(open("vn_words/Viet74K.txt").read().split("\n"))

    print(", ".join(segmentize(sent1, dictionary)))
    print(", ".join(segmentize(sent2, dictionary)))


if __name__ == "__main__":
    main()
