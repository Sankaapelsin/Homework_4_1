class Category:

    def __init__(self, name=str, description=str, goods=list):
        self.name = name
        self.description = description
        self.goods = goods


class Product:

    def __init__(self, name=str, description=str, cost=int, quantity=int):
        self.name = name
        self.description = description
        self.cost = cost
        self.quantity = quantity

