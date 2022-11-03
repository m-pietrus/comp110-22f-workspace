"""EX01 - Chardle (First steps towards Wordle.)"""

__author__ = "730361113"

word: str = input("Enter a 5-charachter word.")
if len(word) == 5:
    letter: str = input("Enter a single charachter.")
    if len(letter) == 1:
        print("Searching for " + letter + " in " + word)
        match: int = 0
        if letter == word[0]:
            print(letter + " found at index 0")
            match = match + 1
        if letter == word[1]:
            print(letter + " found at index 1")
            match = match + 1
        if letter == word[2]:
            print(letter + " found at index 2")
            match = match + 1
        if letter == word[3]:
            print(letter + " found at index 3")
            match = match + 1
        if letter == word[4]:
            print(letter + " found at index 4")
            match = match + 1
        if match == 0:
            print("No instances of " + letter + " found in " + word)
        if match == 1:
            print("1 instance of " + letter + " found in " + word)
        if match == 2:
            print("2 instances of " + letter + " found in " + word)
        if match == 3:
            print("3 instances of " + letter + " found in " + word)  
        if match == 4:
            print("4 instances of " + letter + " found in " + word)  
        if match == 5:
            print("5 instances of " + letter + " found in " + word)                
    else:
        print("Error: Charachter must be a single charachter.")
        quit()
else:
    print("Error: Word must contain 5 charachters ")
    exit()