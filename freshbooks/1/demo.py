
def solution(A):
    max_ = max(A)
    max_ = max_ if max_ > 0 else 1
    marker = [False]*(max_+1)
    # print(marker)
    for element in A:
        if element > 0:
            marker[element] = True
    # print(marker)

    for i, mark in enumerate(marker[1:], 1):
        if not mark:
            # print(i)
            return i
    # print(i+1)
    return i + 1


def main():
    A = [1, 3, 6, 4, 1, 2]
    assert solution(A) == 5
    A = [1, 2, 3]
    assert solution(A) == 4
    A = [-1, -3]
    assert solution(A) == 1
    A = [-1, -3, 0, 1, 2, 10, 100, 1000]
    assert solution(A) == 3
    A = [-1, -3, 1, 2, 10, 100, 1000]
    assert solution(A) == 3


if __name__ == '__main__':
    main()
