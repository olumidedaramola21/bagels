def get_clues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess and the secret number pair"""
    if guess == secretNum:
        return "You got it"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append("fermi")
        if guess[i] in secretNum:
            # A correct digit is in the wrong place.
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"  # guess has no correct digits at all
    else:
        # Sort the clues into alphabetical order so their original order doesn't give the information away.
        clues.sort()
        # Make a single string fgrom the list of clues
        return " ".join(clues)
