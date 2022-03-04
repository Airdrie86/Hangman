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


def get_valid_word(words):
    word = random.choice(words_available)
    word = word.upper()

    return word


def game():
    lives = 6
    word = get_valid_word(words_available)
    guessed = list("_" * len(word))
    guess = False
    used_letters = []
    print("Greetings Traveller! The game of Hangman awaits you!")
    print(hangman[6])
    name = input("Please enter your name:\n")
    print(f"Hello {name}! Welcome to Hangman!")
    print(guessed)

    if guess and lives > 0:
        print(max_tries)
    else:
        letter = input(f"Please pick a letter {name} or guess the word:\n").upper()
        print(current_guess)
    # Code for the main game of hangman

        if letter == word:
            guess = True
        if letter in word:
            used_letters.append(letter)
            print(f"Used letters = {used_letters}")
            print('Lucky Guess!!')
        while letter in used_letters:
            print('You have already guessed that letter', letter)
            letter = input('Please guess a letter \n')
            letter = letter.upper()
            
        else:
            used_letters.append(letter)
            print(f"Used letters = {used_letters}")
            lives -= 1
            print('wrong, lives left: ', lives)
            print(hangman[lives])
            if lives == 0:

        

    if guess:
        print(f"well done, the correct word was {word}")
    else:
        print(f"You can do better than that ! The word was {word}")


if __name__ == '__main__':
    game()
