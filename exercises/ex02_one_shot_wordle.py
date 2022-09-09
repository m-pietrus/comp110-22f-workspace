"""EX02 - This is one-shot Wordle! I'll use emojis and f-strings."""

__author__ = "730361113"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

wordle: str = "python"
guess: str = input(f"What is your {len(wordle)}-letter guess? ")
length: str = input("That was not 6 letters! Try again: ")
if len(guess) != len(wordle): 
    print(length)
    

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