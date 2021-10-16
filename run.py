import random
import string
import operator
from words import words_available

# The visuals for hangman(produced from stack overflow)
hangman = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
]


word = random.choice(words_available)
word = word.upper()
max_tries = 6
current_guess = list("_" * len(word))
guessed = False
used_letters = []
guessed_words = []
# Introducing the game to the user
print("Greetings Traveller! The game of Hangman awaits you!")
print(hangman[0])
name = input("Please enter your name:\n")
print(f"Hello {name}! Welcome to Hangman!")
# Randomly choosing a word for the game
while not guessed and max_tries > 0:
    print(current_guess)
    guess = input(f"Please pick a letter {name} or guess the word:\n").upper()
# Code for the main game of hangman
    if guess == word:
        guessed = True
    if len(guess) == 1 and guess in word:
        print(f"Lucky guess {name}!")
        for x in range(0, len(word)):
            letter = word[x]
            if guess == letter:
                current_guess[x] = guess
        if "_" not in current_guess:
            guessed = True
    else:
        used_letters.append(guess)
        print(f"Used letters = {used_letters}")
        max_tries -= 1
        print(hangman[max_tries])
        print(f"Tries left = {max_tries}")
# Confirms to user if they have manged to correctly guess the word or not 
if guessed:
    print(f"well done {name}, the correct word was {word}")
else:
    print(f"You can do better than that {name}! The word was {word}")