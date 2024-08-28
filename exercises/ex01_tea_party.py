"""Planning a Tea Party"""

__author__ = "730664663"


# main always the top, usually returns None and prints result (returns None)
# if I save, will automatically reformat for easier reading
# \n for new line every time
# always make sure to convert to string so they're all the same type
def main_planner(guests: int) -> None:
    """entrypoint of program, combines functions below"""
    print("A Cozy Tea Party for " + str(guests) + " People")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_count=tea_bags(guests), treat_count=treats(guests))))


def tea_bags(people: int) -> int:
    """calculates how many tea bags are needed"""
    return 2 * people


# besides signature, should not have the type in the function body, only parameter
def treats(people: int) -> int:
    """calculates how many treats are needed"""
    return int(1.5 * tea_bags(people=people))


# use keyword argument to indicate what people is equal to


def cost(tea_count: int, treat_count: int) -> float:
    """calculates the cost of the tea bags and treats"""
    return tea_count * 0.5 + treat_count * 0.75


# always goes below all code after all functions and parameters are defined
if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
