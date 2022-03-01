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
    """ game doc string placeholder """
    word = get_valid_word(words_available)
    max_tries = 6
    current_guess = list("_" * len(word))
    guessed = False
    guess = input
    used_letters = []
    guessed_words = []
    # Introducing the game to the user
    print("Greetings Traveller! The game of Hangman awaits you!")
    print(hangman[6])
    name = input("Please enter your name:\n")
    print(f"Hello {name}! Welcome to Hangman!")
    print(current_guess)
    # Randomly choosing a word for the game
    if guessed and max_tries > 0:
        print(max_tries)
    else:
        guess = input(f"Please pick a letter {name} or guess the word:\n").upper()
        print(current_guess)
    # Code for the main game of hangman
    if guess == word:
        guessed = True
    elif len(guess) == 1 and guess in word:
        print(f"Lucky guess {name}!")
        for i in range(0, len(word)):
            letter = word[i]
            if guess == letter:
                current_guess[i] = guess
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


if __name__ == '__main__':
    game()


# def example():
#     """ test """
#     lives = 6
#     word = 'test'
#     guessed = []

#     while True:
#         letter = input('PLease guess a letter \n')

#         if letter in word:
#             guessed.append(letter)
#             print('correct')
#             if len(word) == len(guessed): break
#         else:
#             lives -= 1
#             print('wrong, lives left: ', lives)
#             if lives == 0: break


#     if lives == 0:
#         print('Lost')
#     else:
#         print('Won')


# if __name__ == '__main__':
#     example()