from classes.category import Category
from classes.product import Product
import json


def load():
    with open('data/products.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def func():
    data = load()
    for category_data in data:
        category_name = category_data['name']
        category_description = category_data['description']
        category_products = []
        for product_data in category_data['products']:
            product = Product(product_data['name'], product_data['description'], product_data['price'],
                              product_data['quantity'])
            category_products.append(product.name)
            category_products.append(product.description)
            category_products.append(product.price)
            category_products.append(product.quantity)
        category = Category(category_name, category_description, category_products)
        print(category)

