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

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError

        return self.__price * self.quantity + other.__price * other.quantity

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


# phone1 = Smartphone("Смартфон 1", 56, 500, 30, "perfect", "RedOne","512","red")
# phone2 = Smartphone("Смартфон 2", 56, 1000, 20, "bad", "XiaomiS4","256","black")
# grass1 = LawnGrass("Газонная трава", 56, 1000, 10, "China", "12","red")

# print(phone1 + phone2)

# print(phone1 + grass1)
