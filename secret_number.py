import random
from main import NUM_DIGITS


def get_secretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list("0123456789")  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


""" Test getSecretNum() function
secret_number = getSecretNum()
print("Generated Secret number: " + secret_number) """
