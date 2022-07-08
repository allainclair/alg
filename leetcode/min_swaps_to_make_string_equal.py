"""
https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/
You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only.
Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].

Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.


Example 1:

Input: s1 = "xx", s2 = "yy"
Output: 1
Explanation:
Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".
Example 2:

Input: s1 = "xy", s2 = "yx"
Output: 2
Explanation:
Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
Note that you can't swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.
Example 3:

Input: s1 = "xx", s2 = "xy"
Output: -1
Example 4:

Input: s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
Output: 4


Constraints:

1 <= s1.length, s2.length <= 1000
s1, s2 only contain 'x' or 'y'.
"""


def get_different_indices(s1, s2):
    index_list = []
    for i, char_pair in enumerate(zip(s1, s2)):
        ch1, ch2 = char_pair
        if ch1 != ch2:
            index_list.append(i)
    return index_list


def count_equal_pairs(s1, s2, index_list):
    sum_x = sum_y = 0
    for i in index_list:
        if s1[i] == 'x':
            sum_x += 1
        elif s1[i] == 'y':
            sum_y += 1
    if sum_x % 2 == 0:
        # print('pair pattern')
        return int(len(index_list) / 2)
    else:
        # print('odd pattern')
        return int(len(index_list) / 2 + 1)


def minimum_swap(s1, s2):
    index_list = get_different_indices(s1, s2)
    # print('s1', s1)
    # print('s2', s2)
    # print('index_list', index_list)
    swaps = 0
    if index_list:
        len_ = len(index_list)
        if len_ % 2 == 0:
            # We can swap the different.
            swaps = count_equal_pairs(s1, s2, index_list)
        else:
            return -1
    # print(swaps)
    return swaps


def main():
    s1 = 'xx'
    s2 = 'yy'
    assert minimum_swap(s1, s2) == 1

    s1, s2 = 'xy', 'yx'
    assert minimum_swap(s1, s2) == 2

    s1, s2 = 'xxxxyyyy', 'yyyyxyyx'
    assert minimum_swap(s1, s2) == 3


if __name__ == '__main__':
    main()
