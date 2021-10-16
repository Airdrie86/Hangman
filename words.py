import random


words_available = ["BEEP", "DART", "CORE", "FROG", "HEAT", "MOLD", "WORK",
 "AVAIL", "CAMEL", "EARTH", "GIANT", "KARMA", "MOULD", "NINJA", 
 "ANTHEM", "BREATH", "CRAYON", "ZODIAC", "TRAVEL", 
 "AIRPORT", "BOILING", "CLUSTER", "UPTIGHT", "TOURISM"]


def get_word():
    """
    Gets a random word from my words_available
    and return the word
    with the word in uppercase.
    """
    word = random.choice(words_available)
    word = word.upper()
    return word


def game(word):
    """
    The functions of playong the game
    """
    current_guess = "_" * len(word)
