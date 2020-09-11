# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = """
stephguirand
Help from youtube videos,
stack overflow, google search, Tutors.
"""


# YOUR HELPER FUNCTION GOES HERE
def find_matches(new_word, words):
    """ Find matches for word by filtering """
    word_matches = filter(lambda word: len(word) == len(new_word), words)
    for index in range(len(new_word)):
        if new_word[index] != ' ':
            word_matches = [
                word for word in word_matches if word[index] == new_word[index]
            ]
    return word_matches


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = input(
        'Please enter a word to solve.\nUse spaces to signify unknown letters:'
    ).lower()

    # YOUR ADDITIONAL CODE HERE

    new_word = find_matches(test_word, words)

    for word in new_word:
        print(word)


if __name__ == '__main__':
    main()
