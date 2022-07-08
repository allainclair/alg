# https://leetcode.com/problems/jump-game-vi/
from icecream import ic


def main():
    pass


def jump_and_cut(numbers, dp, max_score):
    max_number = numbers[0] + max_score
    for i, number in enumerate(numbers):
        if number + max_score > max_number:
            max_number = number

    return max_number


def max_result(nums, k):
    dp = [float('-inf')]*len(nums)
    dp[0] = nums[0]
    # print()
    for i, number in enumerate(nums):
        k_numbers = nums[i+1:k+i+1]
        # ic(k_numbers, dp[i], i)
        keep_original = dp[i]  # Keep a copy.
        for j, k_number in enumerate(k_numbers):
            jump_score = keep_original + k_number
            # ic(jump_score)
            if jump_score > dp[i]:
                dp[i] = jump_score
            if jump_score > dp[i+j+1]:
                dp[i+j+1] = jump_score
    #     ic(k_numbers, dp[i], i)
    #     ic(dp)
    #     ic('-------')
    # ic(dp)
    return dp[-1]


# def test_jump_and_cut():
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#     k = 5
#     expected_numbers = [6, 7, 8, 9, 10]
#     assert jump_and_cut(numbers, k) == (expected_numbers, 5)
#
#     k = 4
#     numbers = expected_numbers
#     expected_numbers = [10]
#     assert jump_and_cut(numbers, k) == (expected_numbers, 9)
#
#     k = 6
#     numbers = [50, 60, 25, 40, 100, 20, 101]
#     expected_numbers = [20, 101]
#     assert jump_and_cut(numbers, k) == (expected_numbers, 100)


def test_basic():
    nums = [1]
    k = 0
    assert max_result(nums, k) == 1
    k = 1
    assert max_result(nums, k) == 1
    k = 2
    assert max_result(nums, k) == 1


def test_1():
    nums = [1, -1, -2, 4, -7, 3]
    k = 2
    assert max_result(nums, k) == 7


def test_2():
    nums = [10, -5, -2, 4, 0, 3]
    k = 3
    assert max_result(nums, k) == 17


def test_3():
    nums = [1, -5, -20, 4, -1, 3, -6, -3]
    k = 2
    assert max_result(nums, k) == 0


def test_4():
    nums = [100, -1, -100, -1, 100]
    k = 2
    assert max_result(nums, k) == 198


if __name__ == '__main__':
    main()
