class Category:
    name: str
    description: str
    goods: list

    total_categories = 0
    total_unique_products = 0
    product_count = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.__goods = goods
        Category.total_categories += 1
        Category.total_unique_products += len(set(goods))
        Category.product_count += len(goods)

    def __str__(self):
        return (f"{str(Category.total_categories)}.Наименование категории:{self.name} Описание:{self.description} "
                f"Товары:{self.__goods} ")

    def add_product(self, product):
        self.__goods.append(product)
        Category.product_count += 1

    @property
    def get_product(self):
        return [
            f"Название продукта : {product.name}, цена : {product.price} рублей, Остаток: {product.quantity} штук."
            for product in self.__goods
        ]
