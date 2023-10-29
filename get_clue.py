def get_clues(guess, secret_num):
    """Returns a string with the pico, fermi, bagels clues for a guess and the secret number pair"""
    if guess == secret_num:
        return "You got it"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # A correct digit is in the correct place.
            clues.append("fermi")
        elif guess[i] in secret_num:
            # A correct digit is in the wrong place.
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"  # guess has no correct digits at all
    else:
        # Sort the clues into alphabetical order so their original order doesn't give the information away.
        clues.sort()
        # Make a single string fgrom the list of clues
        return " ".join(clues)


b = get_clues("012", "102")
print(b)
