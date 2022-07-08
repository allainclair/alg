# https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/


def solution(A):
    count = 0
    comparing = 0
    for center_1, radius_1 in enumerate(A[:-1]):
        left_1 = center_1 - radius_1
        right_1 = center_1 + radius_1
        # print(left_1, right_1)
        for center_2, radius_2 in enumerate(A[center_1+1:], center_1+1):
            comparing += 1
            left_2 = center_2 - radius_2
            right_2 = center_2 + radius_2

            val_1 = left_1 <= left_2 <= right_1
            val_2 = left_1 <= right_2 <= right_1

            val_3 = left_2 <= left_1 <= right_2
            val_4 = left_2 <= right_1 <= right_2

            cond = val_1 or val_2 or val_3 or val_4
            if cond:
                count += 1
                if count > 10000000:
                    return -1

    return count


def test_1():
    A = [1, 5, 2, 1, 4, 0]
    assert solution(A) == 11

