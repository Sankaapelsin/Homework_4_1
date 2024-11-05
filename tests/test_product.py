from classes.product import Product


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
    assert product4.price == 2005.0
    assert product4.quantity == 20


def test_prod_price_property(capsys, first_product):
    first_product.price = -2000
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_product_str(first_product):
    assert str(first_product) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(first_product, second_product, third_product):
    assert first_product + second_product == 2580000.0
    assert first_product + third_product == 1954000.0



