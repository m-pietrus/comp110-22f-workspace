"""Example linked list; returns False."""

from __future__ import annotations
from typing import Optional

class Node:
    data: int = -1
    next: Optional[Node] = None

    def __init__(self, data: int, next: Optional[Node]):
        self.data = data
        self.next = next


def find(head: Optional[Node], needle: int) -> bool:
    if head is None:
        raise ValueError("Cannot call find on an empty linked list")
    else:
        if head.data == needle:
            # One-half of the base case...
            return True
        else:
            if head.next is None:
                # ...and here's the other half!
                return False
            else:
                # Recursive progress made here; moved closer to base case.
                return find(head.next, needle)


l: Node = Node(1, Node(2, Node(3, None)))
print(find(l, 4))