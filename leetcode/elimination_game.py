"""https://leetcode.com/problems/elimination-game/"""


def last_remaining(n):
    list_ = list(range(1, n+1))


def main():
    n = 9
    assert last_remaining(9) == 6


if __name__ == '__main__':
    main()
