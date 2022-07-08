"""Write a recursive function that returns the sum of the digits of a
given integer.

input: 12345
output: 15
"""


def sumrec(n):
    """Div mod approach"""
    div, mod = n // 10, n % 10
    if div == 0:
        return mod
    return mod + sumrec(div)


def sum_tailrec(n, sum_=0):
    div, mod = n // 10, n % 10
    if div == 0:
        return sum_ + mod
    return sum_tailrec(div, sum_ + mod)


if __name__ == '__main__':
    n = 12345
    assert sumrec(n) == 15
    n = 1122334455
    assert sumrec(n) == 30

    n = 12345
    assert sum_tailrec(n) == 15
    n = 1122334455
    assert sum_tailrec(n) == 30
