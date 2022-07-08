# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

import time

def main():
    test_1()


def day_to_flower(day):
    return not bool(day)


def update_bloom_day(bloom_day):
    bloom_day_copy = bloom_day[:]
    min_ = bloom_day_copy[0]
    min_bloom_day_indices = [0]
    for i, bloom_day in enumerate(bloom_day_copy[1:]):
        if bloom_day < min_ and bloom_day != 0:
            min_bloom_day_indices = {i}
            min_ = bloom_day
        elif bloom_day == min_:
            min_bloom_day_indices.add(i)

    for min_bloom_day_index in min_bloom_day_indices:
        bloom_day_copy[min_bloom_day_index] = 0

    return min_, bloom_day_copy


def check_adjacency(flowers, m, k):
    adjacency = bouquet = 0
    for flower in flowers:
        if flower:
            adjacency += 1
            if adjacency == k:
                bouquet += 1
                adjacency = 0
                if bouquet >= m:
                    return True
        else:
            adjacency = 0
    return False


def min_days_to_flower(bloom_day, m, k):
    n_flowers = m * k
    if len(bloom_day) < n_flowers:
        return -1

    # Update flowers
    flowers = [day_to_flower(day) for day in bloom_day]

    # Check adjacency
    min_ = -1
    while not check_adjacency(flowers, m, k):
        time.sleep(1)
        min_, bloom_day = update_bloom_day(bloom_day)
        flowers = [day_to_flower(day) for day in bloom_day]
        print('min_', min_)
        print('bloom_day', bloom_day)
        print('flowers', flowers)
    return min_


def test_impossible():
    m = 3
    k = 2
    bloom_day = [1, 10, 3, 10, 2]
    assert min_days_to_flower(bloom_day, m, k) == -1


def test_0():
    m = 1
    k = 1
    bloom_day = [1]
    print()
    assert min_days_to_flower(bloom_day, m, k) == 1


def test_1():
    m = 3
    k = 1
    bloom_day = [1, 10, 3, 10, 2]
    print()
    assert min_days_to_flower(bloom_day, m, k) == 3


def test_map_flowers():
    assert day_to_flower(0)
    assert not day_to_flower(1)
    assert not day_to_flower(2)
    assert not day_to_flower(3)


def test_check_adjacency():
    m = 1
    k = 1
    flowers = [True]
    assert check_adjacency(flowers, m, k)

    m = 1
    k = 1
    flowers = [False]
    assert not check_adjacency(flowers, m, k)

    m = 2
    k = 2
    flowers = [True, False, False, True, True, False, True, True]
    assert check_adjacency(flowers, m, k)

    m = 2
    k = 2
    flowers = [True, False, False, False, True, False, True, True]
    assert not check_adjacency(flowers, m, k)

    m = 1
    k = 3
    flowers = [True, False, True, True, True, False, True, True]
    assert check_adjacency(flowers, m, k)

    m = 2
    k = 4
    flowers = [True, True, True, True, False, False, True, True, True, False, True, True, True, True]
    assert check_adjacency(flowers, m, k)


if __name__ == '__main__':
    main()
