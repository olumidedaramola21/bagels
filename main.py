"""A deductive logic game where you must guess a number based on clues."""

from instructions import display_instructions
from secret_number import get_secret_num
from input_generation import get_guess
from get_clue import get_clues

NUM_DIGITS = 3
MAX_GUESSES = 10

display_instructions()


def main():
    while True:  # Main game loop.
        # This stores the secret number the player needs to guess:
        secret_num = get_secret_num()
        print("I have thought up a number.")
        print(" You have {} guesses to get it.".format(MAX_GUESSES))

        for numGuesses in range(1, MAX_GUESSES + 1):
            print("Guess: {}".format(numGuesses))
            guess = get_guess()
            clues = get_clues(guess, secret_num)
            print(clues)

            if guess == secret_num:
                break  # They're correct, so break out of this loop.
            if numGuesses == MAX_GUESSES:
                print("You ran out of guesses.")
                print("The answer was {}.".format(secret_num))

        # Ask player if they want to play again.
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing!")


# #
# # # If the program is run (instead of imported), run the game:
# if __name__ == "__main__":
#     main()
main()
