from classes.class_category import Category


def test_init_category():
    category = Category('TV', 'The best quality and price', ['LG', 'BORK', 'Samsung'])

    assert category.name == 'TV'
    assert category.description == 'The best quality and price'
    assert category.goods == ['LG', 'BORK', 'Samsung']
    assert category.total_categories == 1


def test_total_categories_and_products():
    Category('Smartphone', 'The best quality and price', ['LG', 'BORK', 'Samsung'])
    Category('TV', 'The best quality and price', ['LG', 'BORK', 'Tuborg', 'HP'])
    Category('TV', 'The best quality and price', ['LG', 'BYD', 'Samsung'])

    assert Category.total_categories == 4
    assert Category.total_unique_products == 13
