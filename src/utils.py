from classes.category import Category
from classes.product import Product
import json
import os


def load(path: str):
    """Конвертирует файл json в словарь"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def func():
    """Преобразует данные из словаря в объекты класса"""
    data = load("..//data/products.json")
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
            name = category["name"]
            description = category["description"]
            category_instance = Category(name, description, products)
            categories.append(category_instance)
        return categories


result = func()
print(result)
