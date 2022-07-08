# https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/


def main():
    test_n_2()
    test_n_4()
    test_n_6()


def test_n_2():
    n = 2
    assert reinitialize_permutation(n) == 1


def test_n_4():
    n = 4
    assert reinitialize_permutation(n) == 2


def test_n_6():
    n = 6
    assert reinitialize_permutation(n) == 4


def apply_rule(i, n, perm):
    if i % 2 == 0:
        return perm[i // 2]
    elif i % 2 == 1:
        return perm[(n // 2) + (i - 1) // 2]


def operation(perm, n):
    return [apply_rule(i, n, perm) for i, _ in enumerate(perm)]


def reinitialize_permutation(n):
    init_perm = list(range(n))

    perm = init_perm
    new_perm = operation(perm, n)
    n_operations = 1  # At least one operation needed.
    while new_perm != init_perm:
        perm = new_perm
        new_perm = operation(perm, n)
        n_operations += 1
    return n_operations


if __name__ == '__main__':
    main()

