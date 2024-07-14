from classes.class_product import Product


def test_total_categories_and_products():
    Product("Samsung Galaxy C23 Ultra", "256B, Серый цвет, 200MP камера", 180000.0, 5)
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 34)

    assert Product.all_quantities == 47


def test_init_category():
    product = Product('TV', 'The best quality and price', 50000, 3)

    assert product.name == 'TV'
    assert product.description == 'The best quality and price'
    assert product.price == 50000
    assert product.quantity == 3
