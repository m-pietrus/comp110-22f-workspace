"""Was my final exam code correct?"""

class Repeater:
    """Class definition."""
    max: int
    step: int
    n: int = 0
    first: bool = True

    def __init__(self, max: int, step: int):
        """Class constructor."""
        self.max = max
        self.step = step

    def next(self) -> int:
        """Does the thing."""
        if self.first is True:
            self.first = False
        else:
            sum: int = self.n + self.step
            if sum < self.max:
                self.n = sum
            else:
                self.n = sum - self.max
        return self.n

a: Repeater = Repeater(9, 2)
print(a.next())
print(a.next())
print(a.next())
print(a.next())
print(a.next())
print(a.next())
print(a.next())
print(a.next())