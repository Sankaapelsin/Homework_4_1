from classes.product import  Product

class Category:
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
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return [
            f"{product.name}, {product.price} руб. {product.quantity} шт."
            for product in self.__products
        ]

    def get_total_items(self):
        total_items = sum(product.quantity for product in self.__products)
        return total_items


product1 = Product("Кофе", 80, 15, 10)
product2 = Product("Чай", 60, 10, 22)
product3 = Product("Water", 60, 10, 5)
category = Category("Напитки", 5,  [product1, product2, product3])

# print(product1)  # Вывод: Кофе, 80 руб. Остаток: 10 шт.
print(repr(category))  # Вывод: Напитки, количество продуктов: 37 шт.
