def solution(S):
    # map_ = {0,
    #         3,
    #         6,
    #         9,
    #         12,
    #         15,
    #         18,
    #         21,
    #         24,
    #         27,
    #         30,
    # }

    list_ = list(S)
    counting = set()
    for i, _ in enumerate(list_):
        list_copy = list_[:]
        for n in range(0, 10):
            list_copy[i] = str(n)
            number = int(''.join(list_copy))
            if number % 3 == 0:
                counting.add(number)

    return len(counting)


def test_1():
    S = '23'
    assert solution(S) == 7


def test_2():
    S = '0081'
    assert solution(S) == 11


def test_3():
    S = '022'
    assert solution(S) == 9


def main():
    # S = '23'
    # print(solution(S))

    stress = '0'*3_000
    print(solution(stress))


if __name__ == '__main__':
    main()
