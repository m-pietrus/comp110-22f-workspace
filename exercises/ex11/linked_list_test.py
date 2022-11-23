"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last

__author__ = "730361113"

# To run your tests, run
# python -m pytest exercises/ex11/linked_list_test.py

# TODO: Write at least 2 tests for each function in exercises.ex11.linked_list
#       Reminder: Change funtion names and rediscover tests as added
#                 Test functions must have unique names and must begin with 'test_'


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    # TODO: Ah! Another skeleton.
    with pytest.raises(ValueError):
        last(None)

    
def test_last_non_empty() -> None:
    # TODO: Guys I'm scared.
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3

