"""
Find all valid combinations of k numbers that sum up to n such that the
following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the
same combination twice, and the combinations may be returned in any order.



Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations. [1,2,1] is not valid because 1 is used twice.
Example 4:

Input: k = 3, n = 2
Output: []
Explanation: There are no valid combinations.
Example 5:

Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
There are no other valid combinations.
"""


def main():
    tests()


def gen(k):
    digits = [1]*k
    max_digit = 9

    digit_mark = 1
    len_mark = 0
    while True:
        yield digits
        if digits[len_mark] < max_digit:
            digits[len_mark] += 1
        else:
            len_mark += 1
            if len_mark < k:
                digits[:len_mark] = [1]*len_mark
            else:
                break


def comb(k, n, lists, start=0):

    if start < k:
        for digit in range(1, 10):
            return comb(k, n, start+1)
    else:
        return lists


def tests():

    g = gen(2)
    for n in g:
        print(n)
    # k, n = 3, 7
    # expected = [[1, 2, 4]]  # 1 + 2 + 4 = 7
    # assert comb(k, n, []) == expected


if __name__ == '__main__':
    main()
