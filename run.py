import random
import sys
import string
import operator
import os


words_available = ["BEEP", "DART", "CORE", "FROG"]


word = random.choice(words_available)
return word.upper()

max_tries = 6
curret_guess = "_" * len(word)
guessed = False
letters = []
guessed_words = []
print("Welcome to Guess The Word!")

while guessed is False and max_tries > 0:
    return current_guess
    guess = input("Please pick a letter or guess the word!:")
    guess = guess.upper()

    if guess == word:
        guessed = True
    if len(guess) == 1 and guess in word:
        for x in range(0,len(word)):
                letter = word[x]
            if guess == letter:
                    current_guess[x] = guess
        if "_" not in current_guess:
            guessed = True
    else:
            max_tries -= 1

if guessed:
    print("Well")
else:
    print("h")