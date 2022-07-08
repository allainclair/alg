class Product:
    def __init__(self, brand_name, deleted, hidden, id, price, product_name):
        self.brand_name = brand_name
        self.deleted = deleted
        self.hidden = hidden
        self.id = id
        self.price = float(price[1:])
        self.product_name = product_name

    def __repr__(self):
        return (
            f"Product(brand_name='{self.brand_name}', "
            f"deleted={self.deleted}, "
            f"hidden={self.hidden}, "
            f"id={self.id}, "
            f"price={self.price:.2f}, "
            f"product_name='{self.product_name}')"
        )

    def __eq__(self, other):
        return repr(other) == self.__repr__()

    def __hash__(self):
        return hash(self.__repr__())

    def __lt__(self, other):
        # This function is called when we use sorted
        # Ref: https://docs.python.org/3/library/functions.html#sorted
        if self.price < other.price:
            return True
        elif self.price == other.price and self.product_name < other.product_name:
            return True
        else:
            return False
