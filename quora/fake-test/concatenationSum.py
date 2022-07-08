import itertools


def main():
    test_1()


def concatenationSum(a):
    p = itertools.product(a, a)
    sum_ = 0
    for a, b in p:
        sum_ += int(str(a) + str(b))
    return sum_


def test_1():
    a = [10, 2]
    result = concatenationSum(a)
    # print()
    # print(result)
    assert result == 1344

    a = [1, 2, 3]
    result = concatenationSum(a)
    assert result == 198


if __name__ == '__main__':
    main()
