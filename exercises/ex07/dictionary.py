"""EX07 - Dictionary for an exercise."""

__author__ = "730361113"


def invert(key_first: dict[str, str]) -> dict[str, str]:
    """Makes the key the value and the value the key."""
    value_first: dict[str, str] = {}
    for key in key_first:
        value = key_first[key]
        value_first[value] = key
    if len(key_first) != len(value_first):
        raise KeyError
    return dict(value_first)


def favorite_color(dictionary: dict[str, str]) -> str:
    """Returns the most popular color in a dictionary."""
    color: str = ""
    color_list: dict[str, int] = {}
    for key in dictionary:
        color = dictionary[key]
        if color in color_list:
            color_list[color] += 1
        else:
            color_list[color] = 1
    max_color: str = ""
    for key in color_list:
        if max_color not in color_list or color_list[max_color] < color_list[key]:
            max_color = key
    return max_color


def count(values: list[str]) -> dict[str, int]:
    """Returns how many instances of a str there are in a list."""
    frequency: dict[str, int] = {}
    i: int = 0
    while i < len(values):
        if values[i] in frequency:
            frequency[values[i]] += 1
        else:
            frequency[values[i]] = 1
        i += 1
    return frequency