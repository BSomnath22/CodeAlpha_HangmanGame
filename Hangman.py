import random

words = ["python", "planet", "school", "orange", "guitar"]

secret_word = random.choice(words)

guessed_letters = []

incorrect_guesses = 0
max_incorrect_guesses = 6

hangman_stages = [

    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,

    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,

    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,

    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,

    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,

    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,

    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

print("Welcome to Hangman!")
print("Guess the hidden word before the man is hanged.")

while incorrect_guesses < max_incorrect_guesses:

    print(hangman_stages[incorrect_guesses])

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word.strip())
    print("Incorrect guesses left:",
          max_incorrect_guesses - incorrect_guesses)

    if "_" not in display_word:
        print("\nCongratulations!")
        print("You guessed the word:", secret_word)
        break

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!")
    else:
        print("Wrong guess!")
        incorrect_guesses += 1

if incorrect_guesses == max_incorrect_guesses:

    print(hangman_stages[incorrect_guesses])

    print("\nGame Over!")
    print("The correct word was:", secret_word)