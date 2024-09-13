"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730664663"


def input_word() -> str:  # since there is a return value, must have return in function
    """user inputs a word, fn checks if it's 5 characters"""
    word: str = str(
        input("Enter a 5-character word: ")
    )  # must turn type of input into a string to compare to word
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()  # will leave whatever function is executing immediately, helpful to address errors


def input_letter() -> str:
    """User inputs a letter"""
    letter: str = str(input("Enter a single character: "))
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:
    """Checks if the letter is in the word, if so, how many instances"""
    count = 0  # initialize at 0
    print("Searching for", letter, "in", word)  # comma instead of + can be used
    if letter == word[0]:  # since conditions aren't mutually exclusive, not if-else
        count = count + 1  # running count of each instance of the letter
        print(letter, "found at index", 0)
    if letter == word[1]:
        count = count + 1
        print(letter, "found at index", 1)
    if letter == word[2]:
        count = count + 1
        print(letter, "found at index", 2)
    if letter == word[3]:
        count = count + 1
        print(letter, "found at index", 3)
    if letter == word[4]:
        count = count + 1
        print(letter, "found at index", 4)
    if count == 0:  # will run after all the other if statements evaluated
        print("No Instances of", letter, "found in", word)
    else:  # count amounts are mutually exclusive
        print(count, "instances of", letter, "found in", word)


def main() -> None:  # entry point and calls functions
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":  # makes running program as a module and for reuse
    main()
