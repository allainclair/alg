from solver import solver_1
from const import DROP_PIZZA

from collections import Counter


def check(solution_paths, solution):
    paths = solution.split(DROP_PIZZA)
    assert len(paths) == len(solution_paths)
    for path, solution_path in zip(paths, solution_paths):
        assert Counter(path) == Counter(solution_path)
    return True


def test_solver_1_1():
    locations = [(1, 3), (4, 4)]
    first_path = 'ENNN'
    second_path = 'EEEN'
    sol = [first_path, second_path, '']
    assert check(sol, solver_1(locations))


def test_solver_1_2():
    locations = [
        (0, 0),  # D -> ''
        (1, 3),  # path_1
        (4, 4),  # path_2
        (4, 2),  # path_3
        (4, 2),  # D -> ''
        (0, 1),  # path_4
        (3, 2),  # path_5
        (2, 3),  # path_6
        (4, 1)
        # Last drop -> ''
    ]
    path_1 = 'ENNN'
    path_2 = 'NEEE'
    path_3 = 'SS'
    path_4 = 'SWWWW'
    path_5 = 'EEEN'
    path_6 = 'NW'
    path_7 = 'EESS'
    sol = ['', path_1, path_2, path_3, '', path_4, path_5, path_6, path_7, '']
    solver_sol = solver_1(locations)
    print(solver_sol)
    assert check(sol, solver_sol)
