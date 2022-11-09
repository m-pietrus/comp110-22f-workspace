"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730361113"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Outputs distance as a float value between two points."""
        dist: float = 0
        dist = sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2))
        return dist


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Reassign the object's location attribute."""
        self.location = self.location.add(self.direction)
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        if Cell.is_vulnerable(self):
            return "gray"
        else:
            return "orange"

    def contract_disease(self) -> None:
        """If called, changes a cell to infected."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Asks if a cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
        
    def is_infected(self) -> bool:
        """Asks if a cell is infected."""
        if self.sickness == constants.INFECTED:
            return True
        else:
            return False

    def contact_with(self, other: Cell) -> None:
        """Infects other cells!"""
        if Cell.is_vulnerable(self) and Cell.is_infected(other):
            Cell.contract_disease(self)
        if Cell.is_vulnerable(other) and Cell.is_infected(self):
            Cell.contract_disease(other)


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, initial_infected: int):
        """Initialize the cells with random locations and directions."""
        if initial_infected >= cells or initial_infected <= 0:
            raise ValueError("Invalid number of initial infections.") 
        self.population = []
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        i: int = 0
        while i < initial_infected:
            Cell.contract_disease(self.population[i])
            i += 1
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        Model.check_contacts(self)

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Checks to see if in contact, and if so infects!"""
        i: int = 0
        while i < len(self.population):
            idx: int = 1
            subject: Cell = self.population[i]
            tester: Cell = self.population[idx]
            if subject.is_infected() or tester.is_infected():
                while idx < len(self.population):
                    if Point.distance(subject.location, tester.location) <= constants.CELL_RADIUS:
                        Cell.contact_with(subject, tester)
                    idx += 1
            i += 1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        return False