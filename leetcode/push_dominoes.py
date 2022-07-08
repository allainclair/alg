# https://leetcode.com/problems/push-dominoes/submissions/

R = 'R'
L = 'L'
S = '.'

MOVING_MAP = {
    R: 1,
    L: -1,
}


def step(dominoes_list, moving_indices):
    new_dominoes = dominoes_list[:]
    for index in moving_indices[1:-1]:
        moving_dom = dominoes_list[index]
        i = MOVING_MAP[moving_dom]
        next_dom = dominoes_list[index + i]
        next_dom_index = index + i
        if next_dom == S:
            next_next_dom = dominoes_list[next_dom_index + i]
            if next_next_dom == moving_dom or next_next_dom == S:
                new_dominoes[next_dom_index] = moving_dom
    return new_dominoes


def check_neighbours_falling(dominoes, i):
    left, right = dominoes[i - 1], dominoes[i + 1]
    if left == R and (right == R or right == S):
        return True
    elif right == L and (left == L or left == S):
        return True


def falling(dominoes):
    for i, dom in enumerate(dominoes):
        if dom == S and check_neighbours_falling(dominoes, i):
            return True
    return False


def pushDominoes(dominoes_string):
    dominoes_list = [L] + list(dominoes_string) + [R]
    moving_indices = [i for i, d in enumerate(dominoes_list) if d != S]
    while falling(dominoes_list):
        dominoes_list = step(dominoes_list, moving_indices)
        moving_indices = [i for i, d in enumerate(dominoes_list) if d != S]
    return ''.join(dominoes_list[1:-1])


if __name__ == '__main__':
    # input_ = 'RR.L'
    # print(pushDominoes(input_))
    # result = "RR.L"

    # input_ = ".L.R...LR..L.."
    # print(pushDominoes(input_))
    # result = "LL.RR.LLRRLL.."

    # input_ = ".L.R."
    # print(pushDominoes(input_))
    # result = "LL.RR"

    input_ = "..R.."
    print(pushDominoes(input_))
    result = "..RRR"
