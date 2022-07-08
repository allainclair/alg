"""Create a function that takes numbers as arguments, adds them together,
and returns the product of digits until the answer is only 1 digit long.

Examples
sum_dig_prod(16, 28) ➞ 6
16 + 28 = 44
4*4 = 16
1*6 = 6


sum_dig_prod(0) ➞ 0

sum_dig_prod(1, 2, 3, 4, 5, 6) ➞ 2
1 + 2 + 3 + 4 + 5 + 6 = 21
2*1 = 2

Notes
The input of the function is at least one number.

It validates python:
1. *args syntax
2. Casting: str, int
3. sum function
4. *= operator
5. good naming variables (Avoid using i, j, s, etc)
6. iteration without indexing

Source: https://edabit.com/challenge/HrQoXJYqpYZ2Rqvtb
"""
import numpy as np  # Not used


def sum_dig_prod1(*args):
    product = sum(args)
    while product > 9:
        acc_product = 1
        for digit in str(product):
            acc_product *= int(digit)
        product = acc_product
    return product


def sum_dig_prod(*args):
    x = sum(args)
    while x > 9:
        x = np.prod(int(i) for i in str(x))
    return x


def test_sum_dig_prod(sum_dig_prod_function):
    assert sum_dig_prod_function(16, 28) == 6
    assert sum_dig_prod_function(1, 2, 3, 4, 5, 6) == 2
    assert sum_dig_prod_function(0) == 0


def test_main():
    for sum_dig_prod in [sum_dig_prod1]:
        test_sum_dig_prod(sum_dig_prod)


if __name__ == '__main__':
    test_main()