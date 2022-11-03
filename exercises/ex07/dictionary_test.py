"""EX07 - I suppose I might be testing something here."""

__author__ = "730361113"


import pytest
from exercises.ex07.dictionary import count, favorite_color, invert


def test_invert_use_one() -> None:
    """Will it invert city names?"""
    key_first: dict[str, str] = {
        "Chapel": "Hill",
        "Swan": "Quarter",
        "Rocky": "Mount"
    }
    assert invert(key_first) == {
        "Hill": "Chapel",
        "Quarter": "Swan",
        "Mount": "Rocky", 
    }


def test_invert_use_two() -> None:
    """With the same key?"""
    key_first: dict[str, str] = {
        "North": "Carolina",
        "New": "York",
        "Rhode": "Island"
    }
    assert invert(key_first) == {
        "Carolina": "North",
        "York": "New",
        "Island": "Rhode"
    }


with pytest.raises(KeyError):
    key_first = {"North": "Carolina", "South": "Carolina"}
    invert(key_first)


def test_invert_edge() -> None:
    """Will it invert an empty dictionary?"""
    key_first: dict[str, str] = {}
    assert invert(key_first) == {}


def test_favorite_color_use_one() -> None:
    """Simple test!"""
    dictionary: dict[str, str] = {
        "Matthias": "Green",
        "Grayson": "Gray",
        "Aster": "Green",
    }
    assert favorite_color(dictionary) == "Green"


def test_favorite_color_use_two() -> None:
    """No clear favorite."""
    dictionary: dict[str, str] = {
        "Matthias": "Green",
        "Grayson": "Gray",
        "Krista": "Black",
    }
    assert favorite_color(dictionary) == "Green"


def test_favorite_color_edge() -> None:
    """What happens with an empty list?"""
    dictionary: dict[str, str] = {}
    assert favorite_color(dictionary) == ""


def test_count_use_one() -> None:
    """This one is prettu normal."""
    values: list[str] = ["Red", "Blue", "Red", "Blue", "Orange", "Red"]
    assert count(values) == {
        "Red": 3,
        "Blue": 2,
        "Orange": 1
    }


def test_count_use_two() -> None:
    """One color only!"""
    values: list[str] = ["Red", "Red", "Red"]
    assert count(values) == {"Red": 3}


def test_count_edge() -> None:
    """An empty list!"""
    values: list[str] = []
    assert count(values) == {}