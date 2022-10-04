"""A directory! For my utils!"""

__author__ = "730361113"


def only_evens(xs: list[int]) -> list[int]:
    """Returns a new list containing only the even numbers from the provided list."""
    i: int = 0
    output: list[int] = []
    while i < len(xs):
        if xs[i] % 2 == 0:
            output.append(xs[i])
        i = i + 1
    return output


def concat(listA: list[int], listB: list[int]) -> list[int]:
    """Combines two seperate into one list!"""
    return listA + listB


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Returns a new list that is a subset of a provided list between two indexes."""
    assert start <= end
    if start < 0:
        start: int = 0
    if end > len(xs):
        end: int = len(xs)
    output: list[int] = []
    while start < end:
        output.append(xs[start])
        start = start + 1
    return output