import random

NUM_DIGITS = 3


def get_secret_num():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list("0123456789")  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secret_num = ""
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


""" Test get_secret_num() function
secret_number = get_secret_num()
print("Generated Secret number: " + secret_number) """
