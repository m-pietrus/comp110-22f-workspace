"""An opportuinty to practice with lists?"""

__author__ = "730361113"


def all(sample: list[int], x: int) -> bool:
    """Tells if all the numbers in a sample match the provided number."""
    i: int = 0
    if len(sample) == 0:
        return False
    else:
        while i < len(sample):
            if x != sample[i]:
                return False
                i = len(sample) + 1
            else:
                i = i + 1
        return True


def max(input: list[int]) -> int:
    """Returns the maximum value."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    while len(input) != 1:
        if input[0] < input[1]:
            input.pop(0)
        else:
            input.pop(1)
    return input[0]


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """This will tell me if two lists are the same!"""
    if (len(list1) or len(list2)) == 0:
        return True
    if len(list1) == len(list2):
        i: int = 0
        while len(list1) >= i or len(list2) >= i:
            if list1[i] == list2[i]:
                i = i + 1
            else:
                return False
            if i == len(list1):
                return True
    return False