"""
Find the kth largest element in an unsorted array. Note that it is
the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""


def main():
    tests()


def partition(list_, low, high):
    i = low - 1
    pivot = list_[high]  # pivot

    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if list_[j] < pivot:
            # increment index of smaller element
            i += 1
            list_[i], list_[j] = list_[j], list_[i]

    list_[i + 1], list_[high] = list_[high], list_[i + 1]
    return i + 1


def k_th_largest(nums, k):
    len_ = len(nums)
    low, high = 0, len_ - 1
    x = len_ - k
    print('x', x)
    print()
    while True:
        i = partition(nums, low, high)
        print('i', i)
        print(nums)

        if nums[i] < nums[x]:
            low = i + 1
            print('low', low)
        elif nums[i] > nums[x]:
            high = i - 1
            print('high', high)
        else:
            print('RET', nums[i])
            return nums[i]
        print()


def tests():
    # list_ = [3, 2, 1, 5, 6, 4]
    # k = 2
    # expected = 5
    # assert k_th_largest(list_, k, ) == expected
    #
    # list_ = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    # k = 4
    # expected = 4
    # assert k_th_largest(list_, k, ) == expected

    # list_ = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    # print(sorted(list_))
    # k = 9
    # expected = 1
    # assert k_th_largest(list_, k) == expected

    list_ = [3, 3, 3, 3, 4, 3, 3, 3, 3]
    print(sorted(list_))
    k = 1
    expected = 4
    assert k_th_largest(list_, k) == expected


if __name__ == '__main__':
    main()