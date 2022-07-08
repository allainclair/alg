"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity
should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


def main():
    nums1 = [1, 3]
    nums2 = [2]
    print(merge(nums1, nums2))

    nums1 = [1, 3, 6, 10, 20]
    nums2 = [2, 4, 11, 15, 18, 22, 25]
    print(merge(nums1, nums2))

    print(median(nums1, nums2))


def merge(nums1, nums2):
    iter1, iter2 = iter(nums1), iter(nums2)
    try:
        n1, n2 = next(iter1), next(iter2)
    except StopIteration:
        return nums1 + nums2

    merged = []
    while True:
        if n1 < n2:
            merged.append(n1)
            try:
                n1 = next(iter1)
            except StopIteration:
                merged += [n2] + list(iter2)
                return merged
        else:
            merged.append(n2)
            try:
                n2 = next(iter2)
            except StopIteration:
                merged += [n1] + list(iter1)
                return merged


def median(nums1, nums2):
    merged = merge(nums1, nums2)
    len_ = len(merged)
    if len_ % 2 == 0:
        mid1 = len_ // 2
        mid2 = mid1 - 1
        return (merged[mid1] + merged[mid2]) / 2
    else:
        mid = len_ // 2
        return merged[mid]


if __name__ == '__main__':
    main()
