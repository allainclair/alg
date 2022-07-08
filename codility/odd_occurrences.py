# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

from collections import Counter


def solution(A):
    counter = Counter(A)
    for value, count in counter.items():
        if count == 1:
            return value


def test_1():
    A = [9, 3, 9, 3, 9, 7, 9]
    assert solution(A) == 7

def main():
    pass


if __name__ == '__main__':
    main()
