def solution(A):
    max_element = max(A)
    indexer = [False]*(max_element+1)

    for element in A:
        if element > 0:
            indexer[element] = True
            # if element == min_:
            #     min_ +=
    index = 0
    for index, value in enumerate(indexer[1:], 1):
        if not value:
            return index
    return index + 1




def test_1():
    A = [1, 3, 6, 4, 1, 2]
    assert solution(A) == 5


def test_2():
    A = [1, 2, 3]
    assert solution(A) == 4


def test_3():
    A = [-1, -3]
    assert solution(A) == 1


def test_4():
    A = [-1, -3, 1]
    assert solution(A) == 2


def test_5():
    A = [-1, -3, 1, 5]
    assert solution(A) == 2


def main():
    pass


if __name__ == '__main__':
    main()