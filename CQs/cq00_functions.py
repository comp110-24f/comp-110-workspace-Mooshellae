"""Challenge Question 1 - 8/28/24"""

__author__ = "730664663"


def mimic(message: str) -> str:
    """repeats input (message) back"""
    return message


def main() -> None:
    """print results of mimic function"""
    print(mimic(message=input("What is your message?")))
    return None


if __name__ == "__main__":
    main()
