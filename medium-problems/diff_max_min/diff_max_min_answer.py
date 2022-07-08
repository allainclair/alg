"""Given a number, return the difference between the maximum and minimum numbers
that can be formed when the digits are rearranged.

Examples
rearranged_difference(972882) ➞ 760833
# 988722 - 227889 = 760833

rearranged_difference(3320707) ➞ 7709823
# 7733200 - 23377 = 7709823

rearranged_difference(90010) ➞ 90981
# 91000 - 19 = 90981

It validates python:
1. The use of casting (str) and (int)
3. str.join
2. sorted or sort function (and reverse param)
3. [::-1] "trick".
4. good naming variables (Avoid using i, j, s, etc)

Source: https://edabit.com/challenge/jwzAdBnJnBxCe4AXP
"""


def diff_max_min1(number):
    sorted_min = ''.join(sorted(str(number)))
    sorted_max = ''.join(sorted(str(number), reverse=True))
    return int(sorted_max) - int(sorted_min)


def diff_max_min2(number):
    sorted_min = ''.join(sorted(str(number)))
    sorted_max = sorted_min[::-1]
    return int(sorted_max) - int(sorted_min)


def diff_max_min3(number):
    sorted_min = ''.join(sorted(str(number)))
    return int(sorted_min[::-1]) - int(sorted_min)


def test_diff_max_min(diff_function):
    number = 15953245
    max_ = 95554321
    min_ = 12345559
    result = diff_function(number)
    assert result == max_ - min_


def test_main():
    for diff_function in [diff_max_min1, diff_max_min2, diff_max_min3]:
        test_diff_max_min(diff_function)


if __name__ == '__main__':
    test_main()
