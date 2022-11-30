"""COMP 110 final activity; click to plant a tree!"""

import turtle as t
from random import random

TRUNK_FACTOR: float = 0.0
TRUNK_BASE: float = 90.0
UP_BASE: float = 90.0
UP_FACTOR: float = 0.0
ANGLE_FACTOR: float = 40.0
LENGTH_FACTOR: float = 1.00
LENGTH_MAX: float = 5.0
TRACER: bool = False


def tree(x: float, y: float) -> None:
    """Plant a happy, little tree."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    branch(UP_BASE + random() * UP_FACTOR, random() * TRUNK_FACTOR + TRUNK_BASE)
    if TRACER is True:
        t.update()


def branch(angle: float, length: float) -> None:
    """Draw a beautiful branch...recursively."""
    t.setheading(angle)
    t.forward(length)
    if length < LENGTH_MAX:
        ... # Do nothing...base case
    else:
        branch(angle + random() * ANGLE_FACTOR, length * random() * LENGTH_FACTOR)
        branch(angle - random() * ANGLE_FACTOR, length * random() * LENGTH_FACTOR)
    t.setheading(angle + 180.0)
    t.forward(length)


if TRACER is True:
    t.tracer(0, 0)
t.speed(0)
t.getscreen().onclick(tree)
t.done()