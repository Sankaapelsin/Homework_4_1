from classes.smartphone import Smartphone
from classes.lawn_grass import LawnGrass
from classes.base import Base


class Category(Base):
    name: str
    description: str
    products: list

    total_categories = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.total_categories += 1
        Category.product_count += len(products)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.products})"

    def __str__(self):
        return f"{self.name}, количество продуктов: {Category.get_total_items(self)} шт."

    def add_product(self, product):
        if isinstance(product, (Smartphone, LawnGrass)):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        return [
            f"{product.name}, {product.price} руб. {product.quantity} шт."
            for product in self.__products
        ]

    def get_total_items(self):
        total_items = sum(product.quantity for product in self.__products)
        return total_items
