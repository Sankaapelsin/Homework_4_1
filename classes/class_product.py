class Product:
    name: str
    description: str
    price: int
    quantity: int

    all_quantities = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.all_quantities += self.quantity

    def __str__(self):
        return f"Наименование:{self.name} Описание:{self.description} Цена:{self.price} Количество:{self.quantity}"
