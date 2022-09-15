"""A mission to find what it takes to make Wordle."""

__author__= "730361113"

def contains_char(guess: str, letter: str) -> bool:
    """Evaluating the inputed guess and its letters."""

    assert len(letter) == 1
    i: int = 0
    while i < len(guess):
        if letter == guess[i]:
            return True
        else:
            if i < len(guess):
                i = i + 1
        if i >= len(guess):
            return False



def emojified(guess: str, wordle: str) -> str:
    """This will check contains_char function, and replace 
    True or False with its corresponding Emoji."""

    output: str = ""
    idx: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    
    assert len(guess) == len(wordle)
    
    while idx < len(wordle):
        if guess[idx] == wordle[idx]:
            output = output + GREEN_BOX
        else:
            if contains_char(wordle, guess[idx]) == True:
                output = output + YELLOW_BOX
            else:
                output = output + WHITE_BOX             
        idx = idx + 1
    return output