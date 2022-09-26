from product import Product

from test.fixture_product_dict import (
    product_1,
    product_2,
)


def test_product_field_values():
    p = Product(
        brand_name='Brand name 1',
        deleted=False,
        hidden=False,
        id=1,
        price='$11.11',
        product_name='Product 1',
    )
    assert p == eval(
        "Product(brand_name='Brand name 1', "
        "deleted=False, "
        "hidden=False, "
        "id=1, "
        "price='$11.11', "
        "product_name='Product 1')"
    )


def test_product_equal(product_1):
    p1 = Product(**product_1)
    p2 = Product(**product_1)
    assert p1 == p2


def test_product_different(product_1):
    p1 = Product(**product_1)
    p2 = Product(**product_1)

    # Any different field causes different objects.
    p2.brand_name += ' anything'
    assert p1 != p2


def test_product_comparing_p1_cheaper_and_same_names(product_1):
    p1 = Product(**product_1)
    p2 = Product(**product_1)
    p2.price += 1
    assert p1 < p2
    assert not p2 < p1


def test_product_comparing_p1_cheaper_and_p2_naming_after(product_1):
    p1 = Product(**product_1)
    p2 = Product(**product_1)
    p2.price += 1
    p2.product_name += ' anything'
    assert p1 < p2
    assert not p2 < p1


def test_product_comparing_p1_cheaper_and_p2_naming_before(product_1):
    p1 = Product(**product_1)
    p2 = Product(**product_1)
    p2.price += 1
    p2.product_name = f'A prefix to sort it before {p1.product_name}'
    assert p1 < p2
    assert not p2 < p1


def test_product_comparing_same_prices_and_different_names(product_1):
    p1 = Product(**product_1)
    p2 = Product(**product_1)
    p2.product_name += ' anything'
    assert p1 < p2
    assert not p2 < p1
