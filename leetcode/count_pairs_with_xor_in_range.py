# https://leetcode.com/problems/count-pairs-with-xor-in-a-range/


def count_pairs(nums, low, high):
    sum_ = 0
    for i, num1 in enumerate(nums[:-1]):
        for num2 in nums[i+1:]:
            if low <= num1 ^ num2 <= high:
                sum_ += 1
    return sum_


def main():
    nums = [1, 4, 2, 7]
    low = 2
    high = 6
    assert count_pairs(nums, low, high) == 6

    nums = [9, 8, 4, 2, 1]
    low = 5
    high = 14
    assert count_pairs(nums, low, high) == 8


if __name__ == '__main__':
    main()
