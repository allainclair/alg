# https://leetcode.com/problems/convert-1d-array-into-2d-array/


def construct2d_array(original, m, n):
    if len(original) != m*n:
        return []
    new = []
    for i in range(m):
        new.append(original[i*n:i*n+n])
    return new


def test_0():
    original = []
    assert construct2d_array(original, -1, -1) == []


def test_1():
    original = [1, 2, 3]
    m = 1
    n = 3
    assert construct2d_array(original, m, n) == [[1, 2, 3]]


def test_2():
    original = [1, 2]
    m = 1
    n = 1
    assert construct2d_array(original, m, n) == []

# if __name__ == '__main__':
#     main()
