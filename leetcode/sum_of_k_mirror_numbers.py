# https://leetcode.com/problems/sum-of-k-mirror-numbers/


def change_base(base, b10_number):
    div = b10_number
    number = ''
    while div >= base:
        digit = div % base
        div = div // base
        number = f'{digit}{number}'
    number = f'{div}{number}'
    return int(number)


def palindrome(number):
    str_number = str(number)
    return str_number == str_number[::-1]


def k_mirror(k, n):
    count = 0
    number = 1
    sum_ = 0
    print()
    while count < n:
        base_number = change_base(k, number)
        both_palindrome = palindrome(base_number) and palindrome(number)
        if both_palindrome:
            print('number', number)
            print('base_number', base_number)
            print()
            count += 1
            sum_ += number
        number += 1
    return sum_


def test_change_base_1():
    base = 9
    number = 200
    assert change_base(base, number) == 242


def test_change_base_2():
    base = 9
    number = 22
    assert change_base(base, number) == 24


def test_change_base_3():
    base = 2
    number = 16
    assert change_base(base, number) == 10000


def test_k_mirror_1():
    k = 2
    n = 5
    assert k_mirror(k, n) == 25


def test_k_mirror_2():
    k = 3
    n = 7
    assert k_mirror(k, n) == 499


def test_k_mirror_3():
    k = 7
    n = 17
    assert k_mirror(k, n) == 499
