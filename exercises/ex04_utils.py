"""An opportuinty to practice with lists?"""

__author__ = "730361113"


def all(many: list[int], one: int) -> bool:
    """Tells if all the numbers in list match the number in number."""
    assert len(many) >= 1
    i: int = 0
    while i <= len(many) and all != False:
        if many[i] != one:
            return False
    else:
        while i < len(sample):
            if x != sample[i]:
                return False
                i = len(sample) + 1
            else:
        i = i + 1
    if i >= len(many):
        return True
        
        

def max(input: list[int]) -> int:
    "Returns the maximum value of the input."
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    length: int = len(input)
    while length != 1:
        first: int = input[idx]
        second: int = input[idx + 1]
        if first <= second:
            input.pop(idx)
        if first >= second:
            input.pop(idx + 1)
        idx = idx + 1
        

def main() -> None:
    # """The entrypoint of the program and the main game loop."""
    # sample: list[int] = []
    # x: int = 1
    # print(all(sample, x))
    input: list[int] = [1, 2, 3]
    print(max(input))


if __name__ == "__main__":
    main()
    



# def max(input: list[int]) -> int:
#     """Returns the maximum value of the input."""
#     assert len
#     if len(input) == 0:
#         raise ValueError("max() arg is an empty List")
#     while len(input) != 1:

    