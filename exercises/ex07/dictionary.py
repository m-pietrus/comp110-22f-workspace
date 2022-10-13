"""EX07 - Dictionary for an exercise."""

__author__ = "730361113"


def invert(key_first: dict[str, str]) -> dict[str, str]:
    """Makes the key the value and the value the key."""
    value_first: dict[str, str] = {}
    for key in key_first:
        val = key_first[key]
        value_first[val] = key
    if len(key_first) != len(value_first):
        raise KeyError("Each value in the new dictionary must be unique.") 
    return dict(value_first)


def favorite_color(dictionary: dict[str, str]) -> str:
    """Returns the most popular color in a dictionary."""
    color: str = ""
    # TODO: Watch lecture!
    return color


def count(values: list[str]) -> dict[str, int]:
    """Returns how many instances of a str there are in a list."""
    frequency: dict = {}
    # TODO: Watch lecture!
    return frequency