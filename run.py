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
    """ Get random word from words.py """
    word = random.choice(words_available)
    word = word.upper()

    return word


def game():
    """ Function for how the game will be played,
    with help from Stackoverflow """
    alphabet_string = string.ascii_uppercase
    alphabet_list = list(alphabet_string)
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

    while len(word) > 0 and lives > 0 and guess is False:
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
            print(f"Used letters = {used_letters}")
            print(hangman[lives])
            print(guessed)

        elif letter in used_letters:
            print('You have already guessed that letter', letter)
            print('To continue pick a letter and press enter')
            letter = input('Please guess a letter \n')
            letter = letter.upper()
            print(f"Used letters = {used_letters}")
            print(hangman[lives])
            print(guessed)

        elif letter not in alphabet_list:
            print('Error: Please select a letter from the alphabet')
            print('To continue pick a letter and press enter')
            letter = input('Please guess a letter \n')
            letter = letter.upper()
            print(f"Used letters = {used_letters}")
            print(hangman[lives])
            print(guessed)

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
        print(f"well done {name}, the correct word was {word}")
        play_again()
    else:
        print(f"You can do better than that {name}! The word was {word}")
        play_again()


def play_again():
    """ Gives the option to play again, otherwise returns to title screen """
    game_restart = False

    while not game_restart:
        restart = input('Would you like to play Hangman? (Y/N)\n').upper()

        if restart == "Y":
            game_restart = True
            game()

        elif restart == "N":
            game_restart = True
            print('GOODBYE!')
            end_game()

        else:
            print('You must select Y or N. Please try again.')


def end_game():
    """ Prints a message to the user, if they choose "N"  """
    print("THANK YOU FOR PLAYING HANGMAN!")


if __name__ == '__main__':
    game()
