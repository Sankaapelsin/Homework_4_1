class Product:
    name: str
    description: str
    price: int
    quantity: int

    all_quantities = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.all_quantities += self.quantity

    def __str__(self):
        return f"Наименование:{self.name} Описание:{self.description} Цена:{self.__price} Количество:{self.quantity}"

    @classmethod
    def new_product(cls, product):
        name = product["name"]
        description = product["description"]
        price = product["price"]
        quantity = product["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            response = input("Вы уверены, что хотите понизить цену? (y/n): ")
            if response.lower() == 'y':
                self.__price = new_price
            else:
                print("Изменение цены отменено.")
        else:
            self.__price = new_price
