import pytest


def test_init_category(first_category, second_category):
    assert first_category.name == 'Smartphone'
    assert first_category.description == 'The best quality and price'
    assert second_category.description == 'Description of the category number two'


def test__repr(repr_category):
    assert repr(repr_category) == "Category('Smartphone', 'The best', ['Samsung, 180000.0 руб. 5 шт.'])"


def test_total_categories_and_products(first_category):
    assert first_category.total_categories == 4


def test_get_total_items(first_category):
    assert first_category.get_total_items() == 47


def test_products(first_category):
    assert first_category.products[0] == 'Samsung Galaxy C23 Ultra, 180000.0 руб. 5 шт.'


def test_str(first_category, second_category):
    assert str(first_category) == 'Smartphone, количество продуктов: 47 шт.'
    assert str(second_category) == 'Category number two, количество продуктов: 76 шт.'


def test_add_product(first_category, smartphone_for_adding, lawn_grass_for_adding):
    first_category.add_product(smartphone_for_adding)
    first_category.add_product(lawn_grass_for_adding)
    assert smartphone_for_adding.name in first_category.products[3]


def test_add_product1(first_category, smartphone_for_adding, lawn_grass_for_adding):
    first_category.add_product(smartphone_for_adding)
    first_category.add_product(lawn_grass_for_adding)
    for i in first_category.products:
        assert i in first_category.products


def test_add_product_error(first_category, gray_for_adding):
    with pytest.raises(TypeError):
        first_category.add_product(gray_for_adding)
