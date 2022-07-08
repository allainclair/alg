# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/RM1BDv71V60
"""
weight
profit
Capacity -> maximize
"""


def max_profit_memoized(weights, profits, capacity):
    pass


def max_profit_recursive(weights, profits, capacity, index):
    if capacity <= 0 or index >= len(profits):
        return 0

    profit_1 = 0
    current_weight = weights[index]
    if weights[index] <= capacity:
        profit_1 = profits[index] + max_profit_recursive(
            weights, profits, capacity - current_weight, index+1)

    profit_2 = max_profit_recursive(weights, profits, capacity, index+1)

    return max(profit_1, profit_2)


def main():
    weights = [2, 3, 1, 4]
    profits = [4, 5, 3, 7]
    capacity = 5

    profit = max_profit_recursive(weights, profits, capacity)



if __name__ == '__main_':
    main()
