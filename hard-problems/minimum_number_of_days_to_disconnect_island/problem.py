# https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/
from pprint import pprint


def number_of_lands(grid):
    lands = set()
    n_lands = 0
    for i, line in enumerate(grid):
        for j, cell in enumerate(line):
            land = frozenset()
            if cell:
                print(i, j)
                land |= {(i, j)}
                if i-1 >= 0 and grid[i-1][j]:
                    land |= {(i-1, j)}
                if i+1 < len(grid) and grid[i+1][j]:
                    land |= {(i+1, j)}

                if j-1 >= 0 and grid[i][j-1]:
                    land |= {(i, j-1)}
                if j+1 < len(line) and grid[i][j+1]:
                    land |= {(i, j+1)}
                for l in lands:
                    if l & land:
                        new_land = l | land
                        lands.remove(l)
                        lands.add(new_land)
                        pprint(lands)
                        break
                else:
                    n_lands += 1
                    lands.add(land)
                    print('land', land)
                    print(n_lands)
    print(n_lands)
    return n_lands


def min_days(grid):
    pass


def main():

    # grid = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    # assert number_of_lands(grid) == 1
    # grid = [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
    # assert number_of_lands(grid) == 2
    grid = [[1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 0, 1, 1]]
    assert number_of_lands(grid) == 1

    # grid = [[1, 1, 0, 1, 1],
    #         [1, 1, 0, 1, 1],
    #         [1, 1, 0, 1, 1],
    #         [1, 1, 0, 1, 1]]
    # assert number_of_lands(grid) == 2
    #
    # grid = [[1, 1, 0, 1, 1],
    #         [1, 1, 1, 1, 1],
    #         [1, 1, 0, 1, 1],
    #         [1, 1, 1, 1, 1]]
    # assert number_of_lands(grid) == 1

    # assert min_days(grid) == 2


if __name__ == '__main__':
    main()
