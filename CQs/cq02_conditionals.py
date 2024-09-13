"""CQ02 Conditionals Practice"""

__author__ = "730664663"


def guess_a_number() -> None:  # based on user input
    """User guesses a secret number"""
    secret: int = 7
    x: int = int(input("Guess a number: "))  # make sure this is an integer
    print("Your guess was", x)  # the comma includes a space
    if x == secret:
        print("You got it!")
    elif x < secret:
        print("Your guess was too low! The secret number is", secret)
    else:
        print("Your guess was too high! The secret number is", secret)
    return None


if __name__ == "__main__":
    guess_a_number()
