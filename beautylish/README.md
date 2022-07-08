## Summary

It requests
[https://www.beautylish.com/rest/interview-product/list](https://www.beautylish.com/rest/interview-product/list)
and displays a list of products according to some constraints. For more information
check the requirements in the file "Beautylish - Software Engineering Code Interview.pdf"

## Running Environment

### Python version used

* Python 3.10.1 (v3.10.1:2cd268a3a9, Dec  6 2021, 14:28:59)
  [Clang 13.0.0 (clang-1300.0.29.3)]

### Python packages (dependencies)

* To run the tests we need to install `pytest==7.0.1`.

See `requirements.txt` for the full list. You can install them using (recommended):

`$ pip install -r requirements.txt`

## Running main application

From the root project run:

`$ python3 main.py`

The list of (unique) products will be shown in the standard output sorted
by price and name with a summary at the end.

```
List of unique products:

Brand name:     Wonderful Widgets
Product name:   Another Widget
Product price:  $10.00

Brand name:     Acme
Product name:   Anvil
Product price:  $10.00

Brand name:     Wonderful Widgets
Product name:   Widget 3000
Product price:  $10.00

Brand name:     Acme
Product name:   Giant Anvil
Product price:  $99.99

Brand name:     Acme
Product name:   Mini Anvil
Product price:  $99.99

Brand name:     Wonderful Widgets
Product name:   Most Wonderful Widget
Product price:  $99.99

Brand name:     Hooli
Product name:   Nucleus
Product price:  $99.99

Summary:
Total number of unique products: 7
Total number of unique brands: 3
Average price: 61.42
```
## Running tests

From the root project run:

`$ pytest test/`

The `test/test_get_all_products.py` uses the main function `get_all_products` to
test end-to-end the constraints of the application.
