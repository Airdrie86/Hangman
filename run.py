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


    while len(word) > 0 and lives > 0 and guess == False:
        letter = input(f'Please pick a letter or guess the word, {name}! \n')
        letter = letter.upper()
       
        if letter in word:
            for i in range(len(word)):
                alpha = word[i]
                if letter == alpha:
                    guessed[i] = letter
            if '_' not in guessed:
                guess = True
            print(f"Lucky guess {name}!")
            print(guessed)
            print(f"Used letters = {used_letters}")
            print(hangman[lives])

        elif letter in used_letters:
            print('You have already guessed that letter', letter)
            letter = input('Please guess a letter \n')
            letter = letter.upper()

        else:
            used_letters.append(letter)
            print(f"Used letters = {used_letters}")
            lives -= 1
            print('wrong, lives left: ', lives)
            print(hangman[lives])
            print(guessed)
            if lives == 0:
                break

        if letter == word:
            guess = True
            if len(word) == len(guessed):
                break
        

    if guess:
        print(f"You can do better than that ! The word was {word}")
    else:
        print(f"well done, the correct word was {word}")


if __name__ == '__main__':
    game()
