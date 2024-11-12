from classes.product_iterator import ProductIterator


def test_product_iterator(first_category):
    iterator = ProductIterator(first_category)
    for product in iterator:
        assert product in first_category.products
