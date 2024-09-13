"""Practice with conditionals"""


def less_than_10(num: int) -> None:
    """Tell me if a number is less than 10."""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("small number")
    else:
        print("big number")
    print("have a nice day")


# less_than_10(5)


def should_i_eat(hungry: bool) -> None:
    """tells me whether or not to eat based on hunger"""
    if hungry:
        print("eat")
    else:
        print("don't eat")  # else block
    print("im proud of you")  #


# print(should_i_eat(True))


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


# print(check_first_letter(word="happy", letter="h"))


def get_weather_report() -> str:
    """Display weather instructions."""
    weather = input("What is the weather? ")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather

    # get_weather_report()

    # def get_ticket_price() -> int:
    age: int = int(input("What is your age?"))
    if age <= 12:
        price: int = 5
    elif age <= 60:
        price: int = 10
    return price


def get_ticket_price() -> int:
    age: int = int(input("What is your age?"))
    if (age <= 12) or (age > 60):
        price: int = 5
    else:
        price: int = 10
    return price


# print(get_ticket_price())

age: int = 10
18 = age
print(age)
