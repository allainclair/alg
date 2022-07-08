from argparser import (
    check_coordinates,
    coordinates,
    grid_dimension,
    _get_coord,
)


def test_grid_dimension_ok():
    assert grid_dimension('5x5') == (5, 5)
    assert grid_dimension('10x5') == (10, 5)


def test_coordinates_ok():
    assert coordinates('(1, 3) (4, 4)') == [(1, 3), (4, 4)]
    assert coordinates('(1, 3) (4, 4) (50, 64)') == [(1, 3), (4, 4), (50, 64)]


def test__get_coord_ok():
    assert _get_coord('(4, 4)') == (4, 4)
    assert _get_coord('(45, 4)') == (45, 4)
    assert _get_coord('(45, 100)') == (45, 100)


def test_check_coordinates():
    pass

