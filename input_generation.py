from main import NUM_DIGITS


def get_guess():
    """Get a valid guess from player."""

    guess = input("> ")
    while len(guess) == NUM_DIGITS and guess.isdecimal():
        return guess
    print("Invalid guess. Please enter a {}-digit integar number".format(NUM_DIGITS))
