"""Practice with functions"""

from random import randint

print(randint(-4, 3))


# function defintion
def sum(num1: int, num2: int) -> int:
    """Return sum of num1 and num2"""
    return num1 + num2


print(sum(3, 4))
print(sum(num2=5 - 6, num1=5 * 4))  # can solve for me and do num1/num2 in any order
