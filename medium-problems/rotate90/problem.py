"""Given a n*n integer square matrix, rotate it by 90 degrees in
anti-clockwise direction. Try doing it without any extra space.
"""


def rotate_90(matrix_in):
    n = len(matrix_in)
    mid = int(n / 2)
    print(mid)
    new_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # print(i, j)
            new_i, new_j = mid + (mid - i), mid + (mid - j)
            print(new_i, new_j, end='   ')
            new_matrix[new_i][new_j] = matrix_in[i][j]
        print()
    return new_matrix


def main():
    matrix_in = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matrix_out = [
        [3, 6, 9],
        [2, 5, 6],
        [1, 4, 7]
    ]

    out = rotate_90(matrix_in)
    print(out)
    assert out == matrix_out


if __name__ == '__main__':
    main()
