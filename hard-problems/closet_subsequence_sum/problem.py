def min_abs_difference(nums, goal):
    n = len(nums)
    min_ = abs(0 - goal)
    for slice_size in range(1, n+1):
        end = n - slice_size + 1
        for i in range(end):
            abs_ = abs(sum(nums[i:i+slice_size]) - goal)
            if abs_ < min_:
                min_ = abs_
    print(min_)
    return min_


def main():
    nums = [5, -7, 3, 5]
    goal = 6
    assert min_abs_difference(nums, goal) == 0

    nums = [7, -9, 15, -2]
    goal = -5
    assert min_abs_difference(nums, goal) == 1


if __name__ == '__main__':
    main()
