from main import NUM_DIGITS


def display_instructions():
    """Display game instructions to the player."""
    instructions = """Bagels, a deductive logic game.
         I am thinking of a {}-digit number with no repeated digits.
         Try to guess what its is. Here are some clues:
         When I say:          That means:
         Pico                 One digit is correct but in the wrong position.
         Fermi                One digit is correct and in the right position.
         Bagels               No digits is correct

         For example, if the secret number was 248 and your guess was 843, the
       clues would be Fermi Pico.""".format(
        NUM_DIGITS
    )
    print(instructions)
