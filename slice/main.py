#!/usr/bin/env python3
import sys

from argparser import (
    grid_dimension as parse_grid_dimension,
    coordinates as parse_coordinates,
)
from solver import solver_1


def main():
    grid_dimension, *coords = sys.argv[1:]
    coords = ''.join(coords)
    max_x, max_y = parse_grid_dimension(grid_dimension)
    target_coords = parse_coordinates(coords)

    print('grid_dimension:', max_x, max_y)
    print(target_coords)

    print(solver_1(target_coords))


if __name__ == '__main__':
    main()
