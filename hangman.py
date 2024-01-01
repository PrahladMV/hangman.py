""" This is a python program that I made for building the Hangman game.
This game uses a list of words, randomly selects one, and 
allows the player to guess letters until they either guess 
the word or run out of attempts. This program includes a
user interface, input validation, and more details on the game's
progress. Additionally, it provides a function to play the game again after the current game ends. """

import random

def choose_word():
    words = ["python", "hangman", "programming", "challenge", "computer", "game", "learning", "coding"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def display_hangman(attempts):
    hangman_graphics = [
        """
         -----
         |   |
             |
             |
             |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
             |
             |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        --------
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        --------
        """
    ]
    return hangman_graphics[attempts]

def hangman():
    print("Welcome to Hangman!")

    while True:
        secret_word = choose_word()
        guessed_letters = []
        max_attempts = 6
        attempts = 0

        while True:
            print(display_hangman(attempts))
            print("\n" + display_word(secret_word, guessed_letters))
            guess = input("Guess a letter: ").lower()

            if guess.isalpha() and len(guess) == 1:
                if guess in guessed_letters:
                    print("You've already guessed that letter. Try again.")
                elif guess in secret_word:
                    print("Good guess!")
                    guessed_letters.append(guess)
                else:
                    print("Incorrect guess.")
                    attempts += 1
                    guessed_letters.append(guess)
            else:
                print("Invalid input. Please enter a single letter.")

            if "_" not in display_word(secret_word, guessed_letters):
                print("\nCongratulations! You guessed the word: " + secret_word)
                break

            if attempts == max_attempts:
                print(display_hangman(attempts))
                print("\nSorry, you ran out of attempts. The word was: " + secret_word)
                break

            print("Attempts left: " + str(max_attempts - attempts))

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    hangman()
