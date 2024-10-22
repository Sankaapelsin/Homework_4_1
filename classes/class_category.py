class Category:
    name: str
    description: str
    goods: list

    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods
        Category.total_categories += 1
        Category.total_unique_products += len(set(goods))

    def __str__(self):
        return (f"{str(Category.total_categories)}.Наименование категории:{self.name} Описание:{self.description} "
                f"Товары:{self.goods} ")
