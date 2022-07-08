def max_profit(difficulty, profit, worker):
    profits = 0
    for ability in worker:
        max_worker_profit = 0
        for i, d in enumerate(difficulty):
            if ability >= d and profit[i] > max_worker_profit:
                max_worker_profit = profit[i]
        # print(ability, max_worker_profit)
        profits += max_worker_profit
    # print(profits)
    return profits


def main():
    difficulty = [2, 4, 6, 8, 10]
    profit = [10, 20, 30, 40, 50]
    worker = [4, 5, 6, 7]
    assert max_profit(difficulty, profit, worker) == 100


if __name__ == '__main__':
    main()
