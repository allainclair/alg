def main():
    test_1()


def alternatingSort(a):
    b = []
    i, j = 0, -1
    prev = float('-inf')
    for k, _ in enumerate(a):
        if k % 2 == 0:
            b.append(a[i])
            if prev >= a[i]:
                return False
            prev = a[i]
            i += 1
        else:
            b.append(a[j])
            if prev >= a[j]:
                return False
            prev = a[j]
            j -= 1
    return True


def test_1():
    # a = [1, 3, 5, 6, 4, 2]
    # result = alternatingSort(a)
    # print()
    # print(result)
    # assert result
    #
    # a = [1, 4, 5, 6, 3]
    # result = alternatingSort(a)
    # print()
    # print(result)
    # assert not result

    a = [-92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48]
    result = alternatingSort(a)
    assert not result


if __name__ == '__main__':
    main()
