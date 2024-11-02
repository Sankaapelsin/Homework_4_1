import pytest


def test_init_category(first_category, second_category):
    assert first_category.name == 'Smartphone'
    assert first_category.description == 'The best quality and price'
    assert second_category.description == 'Description of the category number two'


def test_total_categories_and_products(first_category):
    assert first_category.total_categories == 4


def test_get_total_items(first_category):
    assert first_category.get_total_items() == 47


def test_get_product(first_category):
    with pytest.raises(AttributeError):
        print(first_category.__products)
    assert (
        first_category.products
        == 'Название продукта : Samsung Galaxy C23 Ultra, цена : 180000.0 рублей, '
           'Остаток: 5 штук.',
        'Название продукта : Iphone 15, цена : 210000.0 рублей, Остаток: 8 штук.',
        'Название продукта : Xiaomi Redmi Note 11, цена : 31000.0 рублей, Остаток: 34 '
        'штук.'
    )


def test_str(first_category, second_category):
    assert str(first_category) == 'Smartphone, количество продуктов: 47 шт.'
    assert str(second_category) == 'Category number two, количество продуктов: 76 шт.'
