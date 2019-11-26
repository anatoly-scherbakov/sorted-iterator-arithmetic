from sorted_iterators import subtract_sorted_iterators


def test_no_match_1():
    difference = list(subtract_sorted_iterators(
        iter([1, 2, 3]),
        iter([4, 5, 6])
    ))

    assert difference == [1, 2, 3]


def test_no_match_2():
    difference = list(subtract_sorted_iterators(
        iter([4, 5, 6]),
        iter([1, 2, 3])
    ))

    assert difference == [4, 5, 6]


def test_no_match_3():
    difference = list(subtract_sorted_iterators(
        iter([1, 3, 5]),
        iter([2, 4, 6])
    ))

    assert difference == [1, 3, 5]


def test_no_match_4():
    difference = list(subtract_sorted_iterators(
        iter([0, 1, 3, 5]),
        iter([2, 4, 6])
    ))

    assert difference == [0, 1, 3, 5]


def test_no_match_5():
    difference = list(subtract_sorted_iterators(
        iter([]),
        iter([2, 4, 6])
    ))

    assert difference == []


def test_match_1():
    difference = list(subtract_sorted_iterators(
        iter([1, 2, 3]),
        iter([1, 2, 4])
    ))

    assert difference == [3]


def test_match_2():
    difference = list(subtract_sorted_iterators(
        iter([2, 4, 8]),
        iter([0, 1, 2, 3, 4, 10])
    ))

    assert difference == [8]
