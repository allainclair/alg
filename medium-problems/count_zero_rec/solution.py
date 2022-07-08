"""Given an integer n, count and return the number of zeros that are present
in the given integer using recursion

input: 10204
output: 2
"""


def count_zero_rec(n):
    """Mod div approach."""
    div, mod = n // 10, n % 10
    if div == 0:
        return 0
    return (1 if mod == 0 else 0) + count_zero_rec(div)


def main():
    n = 10204
    assert count_zero_rec(n) == 2
    n = 102030405
    assert count_zero_rec(n) == 4
    n = 102030440
    assert count_zero_rec(n) == 4


if __name__ == '__main__':
    main()
