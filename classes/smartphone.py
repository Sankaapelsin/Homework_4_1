from classes.product import Product


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return (f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity},"
                f" '{self.efficiency}', '{self.model}', {self.memory}, '{self.color}')")
