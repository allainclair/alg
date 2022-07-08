"""Print the following pattern for given number of rows.

Time: O(n)
Space: O(1)

Input: 5
Output:
5432*
543*1
54*21
5*321
*4321
"""


def n_pattern(n):
    """"""
    strings = [''.join(list(map(str, range(n, 0, -1)))) for _ in range(n)]
    for i, string in enumerate(strings):
        j = n - i - 1
        print(f'{string[:j]}*{string[j+1:]}')


def n_pattern_O1(n):
    for j in range(1, n+1):
        for i in range(n, 0, -1):
            if j != i:
                print(i, end='')
            else:
                print('*', end='')
        print()


def n_pattern_On(n):
    list_ = list(range(5, 0, -1))

    for _ in range(n):
        print(list_)


def main():
    n_pattern_O1(5)
    print()
    n_pattern_On(5)


if __name__ == '__main__':
    main()
