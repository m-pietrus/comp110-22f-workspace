"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730361113"


class Simpy:
    """A kind of library creator/modfier."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Simpy constructor."""
        self.values = values

    def __repr__(self) -> str:
        """Allows Simpy to return in readable format."""
        return f"Simpy({self.values})"
    
    def fill(self, val: float, amt: int) -> None:
        """Modifies self to be a list of all equal values."""
        output: list[float] = []
        while len(output) < amt:
            output.append(val)
        self.values = output

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Modifies self to be a list of equally spaced values."""
        assert step != 0.0
        output: list[float] = []
        output.append(start)
        new: float = sum([output[len(output) - 1], step])
        while new != stop:
            new: float = sum([output[len(output) - 1], step])
            if new != stop:
                output.append(new)
        self.values = output

    def sum(self) -> float:
        """Allows for python built in sum function to be used on Simpy."""
        return sum(self.values)

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Allows '+' use in Simpy."""
        output: Simpy = Simpy([])
        if isinstance(rhs, float):
            for floats in self.values:
                output.values.append(floats + rhs)        
        else:
            assert len(rhs.values) == len(self.values)
            i: int = 0
            for floats in self.values:
                output.values.append(floats + rhs.values[i])
                i += 1
        return output

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Allows '**' use in Simpy."""
        output: Simpy = Simpy([])
        if isinstance(rhs, float):
            for floats in self.values:
                output.values.append(floats ** rhs)        
        else:
            assert len(rhs.values) == len(self.values)
            i: int = 0
            for floats in self.values:
                output.values.append(floats ** rhs.values[i])
                i += 1
        return output

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Allows '==' use in Simpy."""
        output: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item == rhs:
                    output.append(True)
                else:
                    output.append(False)
        else:
            i: int = 0
            for item in self.values:
                if item == rhs.values[i]:
                    output.append(True)
                else:
                    output.append(False)
                i += 1
        return output

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Allows '>' use in Simpy."""
        output: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item > rhs:
                    output.append(True)
                else:
                    output.append(False)
        else:
            i: int = 0
            for item in self.values:
                if item > rhs.values[i]:
                    output.append(True)
                else:
                    output.append(False)
                i += 1
        return output

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Allows advanced indexing of Simpy."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            output: Simpy = Simpy([])
            i: int = 0
            for item in rhs:
                if item is True:
                    output.values.append(self.values[i])
                i += 1
            return output