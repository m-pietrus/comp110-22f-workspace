"""Practice code writing!"""

class Staff:
    """Name and status in CS Department."""
    name: str
    is_cs: bool

    def __init__(self, name: str, is_cs: bool):
        """Class initializer."""
        self.name = name
        self.is_cs = is_cs

    def greet(self) -> str:
        """Returns a string with the inputed information."""
        msg: str = f"Hello, I'm {self.name} "
        if not self.is_cs:
            msg += "NOT "
        return msg + "in CS"


prof: Staff = Staff("Kris", True)
print(prof.greet())
dr: Staff = Staff("Mara", False)
print(dr.greet())