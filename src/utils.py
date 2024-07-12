from classes.class_category import Category
from classes.class_product import Product
import json


def func():
    with open('/data/products.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        print(data)
        for category_data in data:
            category_name = category_data['name']
            category_description = category_data['description']
            category_products = []
            for product_data in category_data['products']:
                product = Product(product_data['name'], product_data['description'], product_data['price'],
                                  product_data['quantity'])
                category_products.append(product)
                print(product)
            category = Category(category_name, category_description, category_products)
            print(category)
        print(Category.total_categories)
        print(Category.total_unique_products)
