import pytest

from classes.category import Category
from classes.product import Product


@pytest.fixture
def first_product():
    return Product(
        name="Samsung Galaxy C23 Ultra",
        description="256B, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def second_product():
    return Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
    )


@pytest.fixture
def third_product():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=34,
    )


@pytest.fixture
def first_category():
    return Category(
        name="Smartphone",
        description="The best quality and price",
        products=[
            Product(
                name="Samsung Galaxy C23 Ultra",
                description="256B, Серый цвет, 200MP камера",
                price=180000.0,
                quantity=5,
            ),
            Product(
                name="Iphone 15",
                description="512GB, Gray space",
                price=210000.0,
                quantity=8,
            ),
            Product(
                name="Xiaomi Redmi Note 11",
                description="1024GB, Синий",
                price=31000.0,
                quantity=34,
            ),
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Category number two",
        description="Description of the category number two",
        products=[
            Product(
                name="Product",
                description="Description of the product",
                price=84.50,
                quantity=10,
            ),
            Product(
                name="Product number two",
                description="Description of the product number two",
                price=155.87,
                quantity=34,
            ),
            Product(
                name="Product number three",
                description="Description of the product three",
                price=8467.56,
                quantity=32,
            ),
        ],
    )


@pytest.fixture
def product_dict():
    return {
        "name": "Microwave",
        "description": "Description of the product Microwave",
        "price": 2005.0,
        "quantity": 20,
    }
