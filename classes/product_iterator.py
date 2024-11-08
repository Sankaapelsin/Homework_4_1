class ProductIterator:
    """Класс для итерации товаров одной категории"""

    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.products):
            good = self.category.products[self.index]
            self.index += 1
            return good
        else:
            raise StopIteration
