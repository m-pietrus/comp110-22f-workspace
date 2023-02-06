"""Building a list using recursive methods; line 19: return n"""

from __future__ import annotations
from typing import Optional

class Node:
    data: int = -1
    next: Optional[Node] = None


def build(start: int, end: int) -> Optional[Node]:
    """Build a linked list from start to end -1."""
    if start >= end:
        return None
    else:
        n: Node = Node()
        n.data = start
        n.next = build(start + 1, end) # A classic pattern...returns everything before.
        return n


head: Optional[Node] = build(0, 2)