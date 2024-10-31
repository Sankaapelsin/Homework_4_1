from classes.class_product import Product
import pytest


def test_total_categories_and_products(first_product, second_product, third_product):

    assert Product.all_quantities == 47


def test_init_category(second_product):

    assert second_product.name == 'Iphone 15'
    assert second_product.description == '512GB, Gray space'
    assert second_product.price == 210000.0
    assert second_product.quantity == 8


def test_new_product(product_dict):
    product4 = Product.new_product(product_dict)
    assert product4.name == "Microwave"
    assert product4.price == "Цена не должна быть нулевая или отрицательная"
    assert product4.quantity == 20


def test_price(first_product):
    first_product.price = -2000.0
    assert first_product.price == "Цена не должна быть нулевая или отрицательная"




