"""https://leetcode.com/problems/apply-discount-every-n-orders/"""


class Cashier:
    def __init__(self, n, discount, products, prices):
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices

        self._i = 0

    def getbill(self, product, amount):
        if self._i <= self.n:
            discount = False
            self._i += 1
        else:
            discount = True
            self._i = 0

        bill = 0
        for product_id, n in zip(product, amount):
            product_index = self.products.index(product_id)
            price = self.prices[product_index]
            if discount:
                price -= self.discount*price / 100
            bill += price*n
        return bill


def main():
    pass


if __name__ == '__main__':
    main()
