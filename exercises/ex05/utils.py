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


def sub(set: list[int], start: int, end: int) -> list[int]:
    if start < 0:
        start: int = 0
    if end > len(set) - 1:
        end: int = len(set) - 1
    if len(set) == 0 or start > len(set) or end <= 0:
        return []
    while len(set) >= end + 1:
        set.pop(end)
    i: int = 0
    while i < (start - 1):
        set.pop(0)
        i = i + 1
    return set