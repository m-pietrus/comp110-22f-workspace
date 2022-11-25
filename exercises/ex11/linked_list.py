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
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        if head.next is None:
            return head.data
        else:
            return last(head.next)

def value_at(head: Optional[Node], index: int) -> int:
    """Returns data of head at index; raises ValueError if index does not exist."""
    if head is None:
        raise ValueError("Index is out of bounds on the list.")
    else:
        if index == 0:
            return head.data
        else:
            return value_at(head.next, index - 1)

def max(head: Optional[Node]) -> int:
    """Returns the maximum data value in the Linked List; raises ValueError if the Linked List is empty."""
    if head is None:
        raise ValueError("Cannot call max with None.")
    else:
        if head.next is None:
            return head.data
        else:
            if head.data < head.next.data:
                return max(head.next)
            else:
                head.next = head.next.next
                return max(head)

def linkify(items: list[int]) -> Optional[Node]:
    """Returns a Linked List of Nodes with the same values in the same order as the input list."""
    # TODO: Doesn't 'automagically' output as a str
    if len(items) != 1:
        return Node(items[0], linkify(items[1:]))
    else:
        return Node(items[0], None)
    

def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Returns a new Linked List of Nodes where each value in the original is scaled by factor."""
    # TODO: Ah! There's another one in this function!
    if head is None:
        raise ValueError("Index is out of bounds on the list.")
    if head.next is None:
        return Node(head.data * factor, None)
    else:
        return Node(head.data * factor, scale(head.next, factor))