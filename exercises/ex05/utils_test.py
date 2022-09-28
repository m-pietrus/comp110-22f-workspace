"""I suppose this is the file where I will write code that can test."""

__author__ = "730361113"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_edge() -> None:
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_use1() -> None:
    xs: list[int] = [11, 13, 15, 17]
    assert only_evens(xs) == []
    

def test_only_evens_use2() -> None:    
    xs: list[int] = [0, 1, 2, 3, 4, 5, 6, 7]
    assert only_evens(xs) == [0, 2, 4, 6]


def test_concat_edge() -> None:
    listA: list[int] = []
    listB: list[int] = []
    assert concat(listA, listB) == []
    
    
def test_concat_use1() -> None: 
    listA: list[int] = [0, 1, 2, 3]
    listB: list[int] = [3, 2, 1, 0]
    assert concat(listA, listB) == [0, 1, 2, 3, 3, 2, 1, 0]


def test_concat_use2() -> None: 
    listA: list[int] = []
    listB: list[int] = [97, 98, 99, 100]
    assert concat(listA, listB) == [97, 98, 99, 100]


def test_sub_edge() -> None:
    xs: list[int] = [1]
    start: int = 0
    end: int = 1
    assert sub(xs, start, end) == []


def test_sub_use1() -> None:
    xs: list[int] = [0, 1, 2, 3, 4, 5, 6, 7]
    start: int = 3
    end: int = 6
    assert sub(xs, start, end) == [2, 3, 4, 5]


def test_sub_use2() -> None:
    xs: list[int] = [0, 1, 2, 3, 4, 5]
    start: int = -3
    end: int = 9
    assert sub(xs, start, end) == [0, 1, 2, 3, 4]