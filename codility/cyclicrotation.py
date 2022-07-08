# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/


def solution(A, K):
    if not A:
        return A

    len_ = len(A)
    result = [None]*len_
    for i, element in enumerate(A):
        new_index = get_new_index(i, K, len_)
        result[new_index] = element
    return result


def get_new_index(current_index, k, len_):
    sum_ = current_index + k
    new_pos = sum_ % len_
    return new_pos


def test_new_index_1():
    assert get_new_index(0, 1, 10) == 1


def test_new_index_2():
    assert get_new_index(9, 1, 10) == 0


def test_new_index_3():
    assert get_new_index(9, 3, 10) == 2


def test_new_index_4():
    assert get_new_index(7, 3, 10) == 0


def test_1():
    A = []
    K = 3
    assert solution(A, K) == []


def test_2():
    A = [1]
    K = 3
    assert solution(A, K) == [1]

def test_10():
    A = [3, 8, 9, 7, 6]
    K = 3
    assert solution(A, K) == [9, 7, 6, 3, 8]


def test_20():
    A = [0, 0, 0]
    K = 1
    assert solution(A, K) == [0, 0, 0]


def test_30():
    A = [1, 2, 3, 4]
    K = 4
    assert solution(A, K) == [1, 2, 3, 4]


def main():
    test_new_index_1()
    test_new_index_2()
    test_new_index_3()
    test_new_index_4()
    # test_1()


if __name__ == '__main__':
    main()
