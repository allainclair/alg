# https://leetcode.com/problems/new-21-game/
# Allain:  Stats hard problem

def new21Game(n, k, maxPts):
    single_probability = 1 / maxPts
    for i in range(1, k + 1):
        pass

    sum_ = 0
    while sum_ < k:
        sum_ += maxPts
    sum_ -= maxPts

    max_hit_to_continue = k - sum_ - 1
    continue_probability = max_hit_to_continue / maxPts
    stop_probability = 1 - continue_probability


if __name__ == '__main__':
    n = 21
    k = 17
    maxPts = 10

    result = 0.73278
    print(new21Game(n, k, maxPts))
