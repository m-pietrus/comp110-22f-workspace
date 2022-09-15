"""A mission to find what it takes to make Wordle."""

__author__= "730361113"

def contains_char(wordle: str, letter: str) -> bool:
    """Evaluating the inputed guess and its letters."""

    assert len(letter) == 1
    i: int = 0
    while i < len(wordle):
        if letter == wordle[i]:
            return True
        else:
            if i < len(wordle):
                i = i + 1
        if i >= len(wordle):
            return False  