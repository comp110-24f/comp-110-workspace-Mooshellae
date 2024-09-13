def name(name: str) -> str:
    print("hi")

    return name


def other(other: str) -> str:
    return other + name(name=other)


print(other(other="hello"))
