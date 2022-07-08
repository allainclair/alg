def solution(S):
    list_ = list(S)
    counting = set()
    for i, char in enumerate(list_):
        list_copy = list_[:]
        for n in range(0, 10):
            list_copy[i] = str(n)
            number = int(''.join(list_copy))
            if number % 3 == 0:
                counting.add(number)

    return len(counting)


def main():
    # S = '23'
    # assert solution(S) == 7

    S = '0081'
    assert solution(S) == 11

    S = '022'
    assert solution(S) == 9


if __name__ == '__main__':
    main()
