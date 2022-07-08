def main():
    test_1()


def mutateTheArray(n, a):
    prev_list = [0] + a[:-1]
    mid_list = a
    post_list = a[1:] + [0]
    return [i + j + k for i, j, k in zip(prev_list, mid_list, post_list)]


def test_1():
    a = [4, 0, 1, -2, 3]
    result = mutateTheArray(len(a), a)
    print()
    print(result)
    assert result == [4, 5, -1, 2, 1]


if __name__ == '__main__':
    main()
