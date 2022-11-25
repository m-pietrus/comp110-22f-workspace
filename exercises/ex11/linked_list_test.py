"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, is_equal, last, value_at, max, linkify, scale

__author__ = "730361113"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty Linked List should return its last data value."""
    linked_list: Node = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Value_at of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_value_at_non_empty() -> None:
    """Value_at of a non-empty Linked List shouls return the value at requested index."""
    linked_list: Node = Node(1, Node(2, Node(3, None)))
    index: int = 1
    assert value_at(linked_list, index) == 2


def test_max_empty() -> None:
    """Max of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_max_non_empty() -> None:
    """Max of a non-empty Linked List should return the maximum data value."""
    linked_list: Node = Node(20, Node(10, Node(30, None)))
    assert max(linked_list) == 30

def test_linkify_evens() -> None:
    """Linkify of a list of even ints should return a Linked List of the same values."""
    assert is_equal(linkify([2, 4, 6]), Node(2, Node(4, Node(6, None))))


def test_linkify_count() -> None:
    """Linkify of a list of odd ints should return a Linked List of the same values."""
    assert is_equal(linkify([1, 3, 5]), Node(1, Node(3, Node(5, None))))


def test_scale_empty() -> None:
    """Scale of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        scale(None, 2)


def test_scale_non_empty() -> None:
    """Scale of a non-empty Linked List should return a Linked List of values each scaled by factor."""
    assert is_equal(scale(Node(1, Node(2, Node(3, None))), 2), Node(2, Node(4, Node(6, None))))