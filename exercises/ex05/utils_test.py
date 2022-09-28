"""I suppose this is the file where I will write code that can test."""

__author__ = "730361113"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens() -> None:
    edge: list[int] = []
    use1: list[int] = [0, 2, 4, 6,]
    use2: list[int] = [0, 1, 2, 3, 4, 5, 6, 7]
    assert only_evens(edge) == []
    assert only_evens(use1) == []
    assert only_evens(use2) == [0, 2, 4, 6]


def test_concat() -> None:
    edgeA: list[int] = []
    edgeB: list[int] = []
    assert concat(edgeA, edgeB) == []
    use1A: list[int] = [0, 1, 2, 3]
    use1B: list[int] = [3, 2, 1, 0]
    assert concat(use1A, use1B) == [0, 1, 2, 3, 3, 2, 1, 0]
    use2A: list[int] = []
    use2B: list[int] = [97, 98, 99, 100]
    assert concat(edgeA, edgeB) == []
    assert concat(use1A, use1B) == [0, 1, 2, 3, 3, 2, 1, 0]
    assert concat(use2A, use2B) == use2B


def test_sub() -> None:
    # edge case
    edgeset: list[int] = [1]
    edgestart: int = 0
    edgeend: int = 1
    assert sub(edgeset, edgestart, edgeend) == []
    # use case 1
    use1set: list[int] = [0, 1, 2, 3, 4, 5, 6, 7]
    use1start: int = 3
    use1end: int = 6
    assert sub(use1set, use1start, use1end) == [2, 3, 4, 5]
    # use case 2
    use2set: list[int] = [0, 1, 2, 3, 4, 5]
    use2start: int = -3
    use2end: int = 9
    assert sub(use2set, use2start, use2end) == [0, 1, 2, 3, 4]