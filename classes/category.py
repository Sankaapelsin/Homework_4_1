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

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return [
            f"Название продукта: {product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        ]
