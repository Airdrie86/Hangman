import random
import sys
import operator
import os
from words import words_available


def random_word():
    """
    This is where we choose a random word from our words list
    """
    word = random.choice(words_available)
    return word.upper()


def game(word):
    """
    This will hold the main game fuctions
    """
    max_tries = 6
    guess = "_" * len(word)
  