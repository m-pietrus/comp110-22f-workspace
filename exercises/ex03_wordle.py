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

def input_guess(length: int,) -> str:
    """To ensure that the inputed guess is the same length 
    as the wordle."""

    guess: str = str(input(f"Enter a {length} charchter word: "))
    
    while len(guess) != length: 
        guess: str = input(f"That wasn't {length} chars! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and the main game loop."""

    wordle: str = "codes"
    turn: int = 1
    attempt: str = ""

    while turn <= 6 and attempt != wordle:
        print(f" === Turn {turn}/6 === ")
        attempt = str = input_guess(len(wordle))
        print(emojified (attempt, wordle))
        if attempt == wordle:
            print(f"You won in {turn}/6 turns!")    
        turn = turn + 1
    if turn > 6:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()