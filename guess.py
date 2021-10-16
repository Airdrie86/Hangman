import random
import string
import operator



words_available = ["BEEP", "DART", "CORE", "FROG"]


word = random.choice(words_available)
word = word.upper()

max_tries = 6
current_guess = list("_" * len(word))

guessed = False
used_letters = []
guessed_words = []
print("Welcome to Guess The Word!")

while not guessed and max_tries > 0:
    print(current_guess)
    guess = input("Please pick a letter or guess the word:").upper()

    if guess == word:
        guessed = True
    if len(guess) == 1 and guess in word:
        print("you guessed right")
        for x in range(0,len(word)):
            letter = word[x]
            if guess == letter:
                current_guess[x] = guess
        if "_" not in current_guess:
            guessed = True
    else:
        used_letters.append(guess)
        print(f"Used letters = {used_letters}")
        max_tries -= 1
        print(f"Tries left = {max_tries}")
        
    
if guessed:
    print(f"well done, the correct word was {word}")
else:
    print(f"yo no good the word was {word}")
