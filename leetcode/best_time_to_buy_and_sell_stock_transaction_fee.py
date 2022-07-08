"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
"""
import pprint


def profit(endprice, startprice, fee):
    return endprice - startprice - fee


def bestbuy(prices, fee):
    if len(prices) < 2:
        return 0

    profits = [[None]*len(prices) for _ in prices]

    for i, price1 in enumerate(prices):
        for j, price2 in enumerate(prices):
            if i < j:
                profits[i][j] = profit(price2, price1, fee)

    sum_ = 0
    prevmax = 0
    while profits:
        found = False
        maxi, maxj = 0, 0
        maxprofit = 0
        for i in range(len(profits)):
            for j in range(len(profits)):
                if profits[j][i] is not None and profits[j][i] > maxprofit:
                    maxprofit = profits[j][i]
                    maxi, maxj = j, i
                    found = True
                    print(f'[i][j]: {maxi, maxj}')
                    print(f'maxprofit {maxprofit}')
            if found:
                break

        print('current')
        pprint.pprint(profits)
        newps = []
        for l in profits[maxj + 1:]:
            newps.append(l[maxj + 1:])
        profits = newps
        print('new')
        pprint.pprint(profits)

        print('prev max', prevmax)
        print('maxprofit', maxprofit)
        if maxprofit < prevmax:
            sum_ += maxprofit
            prevmax = maxprofit
        else:
            sum_ = maxprofit
        print(sum_)
        print()

    return sum_


def main():
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    assert bestbuy(prices, fee) == 8
    # prices = [1, 3, 7, 5, 10, 3]
    # fee = 3
    # assert bestbuy(prices, fee) == 6


if __name__ == '__main__':
    main()
