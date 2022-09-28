"""A directory! For my utils!"""

__author__ = "730361113"


def only_evens(xs: list[int]) -> list[int]:
    i: int = 0
    output: list[int] = []
    while i < len(xs):
        if len(xs) >= 1 and xs[i] % 2 != 0:
            output.append(xs[i])
        else:
            i = i + 1
    return output

def concat(listA: list[int], listB: list[int]) -> list[int]:
    return listA + listB


def sub(xs: list[int], start: int, end: int) -> list[int]:
    if start < 0:
        start: int = 0
    if end > len(xs) - 1:
        end: int = len(xs) - 1
    if len(xs) == 0 or start > len(xs) or end <= 0:
        return []
    while len(xs) >= end + 1:
        xs.pop(end)
    i: int = 0
    while i < (start - 1):
        xs.pop(0)
        i = i + 1
    return set