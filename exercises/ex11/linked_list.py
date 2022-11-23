"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730361113"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List; raises a ValueError if the list is empty."""
    # TODO: Finish! Just a skeleton here.
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        return None

def value_at(head: Optional[Node], index: int) -> int:
    """Returns data of head at index; raises ValueError if index does not exist."""
    place_holder: int = 0
    # TODO: Clean up the bones.
    # Hint 0: In recursive case, modify args to bring recursive call close to hint 2.
    #         Start by diagramming what this means for a call to value_at with a list 
    #         of two or more nodes and an intial index of 1.
    # Hint 1: An edge case occurs with the list is empty.
    #         raise IndexError("Index is out of bounds on the list.")
    # Hint 2: A second base case occurs when the index is 0. 
    #         Return the data of the current Node being processed on the list here. 
    return place_holder

def max(head: Optional[Node]) -> int:
    """Returns the maximum data value in the Linked List; raises ValueError if the Linked List is empty."""
    place_holder: int = 0
    # TODO: I can see the cobwebs already...
    # Example usage:
    #   >>> max(Node(10, Node(20, Node(30, None))))
    #   30
    #   >>> max(None)
    #   ValueError: Cannot call max with None.
    return place_holder

def linkify(items: list[int]) -> Optional[Node]:
    """Returns a Linked List of Nodes with the same values in the same order as the input list."""
    # TODO: skelton slice subscribtion 
    # Example usage:
    #   >>> linkify([1, 2, 3])
    #   1 -> 2 -> 3 -> None
    # TODO: attempt at adding along assessment application
    return None

def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Returns a new Linked List of Nodes where each value in the original is scaled by factor."""
    # TODO: exterminate all arachnids
    # Example usage:
    #   >>> scale(linkify([1, 2, 3]), 2)
    #   2 -> 4 -> 6 -> None
    return None