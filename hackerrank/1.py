def segment(x, space):
    end_index = x
    len_ = len(space)
    max_of_all = 0
    for i in range(len_ - x + 1):
        current_segment = set(space[i:end_index])
        min_of_segment = min(current_segment)
        if min_of_segment > max_of_all:
            max_of_all = min_of_segment
        end_index += 1

    return max_of_all


def main():
    test_1()
    test_2()
    test_3()
    test_4()


def test_1():
    x = 1
    space = [1, 2, 3, 1, 2]
    expected_result = 3
    assert segment(x, space) == expected_result


def test_2():
    x = 2
    space = [8, 2, 4, 6]
    expected_result = 4
    assert segment(x, space) == expected_result


def test_3():
    x = 2
    space = [1, 1, 1]
    expected_result = 1
    assert segment(x, space) == expected_result


def test_4():
    x = 3
    space = [2, 5, 4, 6, 8]
    expected_result = 4
    assert segment(x, space) == expected_result


if __name__ == '__main__':
    main()
