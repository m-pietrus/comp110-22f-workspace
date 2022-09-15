"""EX02 - This is one-shot Wordle! I'll use emojis and f-strings."""

__author__ = "730361113"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

wordle: str = "teeths"
guess: str = input(f"What is your {len(wordle)}-letter guess? ")
while len(guess) != len(wordle): 
    guess: str = input(f"That was not {len(wordle)} letters! Try again: ")

i: int = 0
output: str = ""


while i < len(wordle):
    if guess[i] == wordle[i]:
        output = output + GREEN_BOX
    else:
        exist: bool = False
        alt: int = 0
        while exist != True and alt < len(wordle):
            if guess[i] == wordle[alt]:
                exist: bool = True
            alt = alt + 1
        if exist == True:
            output = output + YELLOW_BOX
        else:
            output = output + WHITE_BOX
    i = i + 1
print(output)

if wordle == guess:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")