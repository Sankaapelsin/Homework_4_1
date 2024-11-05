Online shop Describtion: Online shop - функционал для работы интернет магазинов

Установка: Клонируйте репозиторий: git clone git@github.com:Sankaapelsin/Homework_4_1.git скопируйте ключ самостоятельно Установите зависимости Иструкция по использованию: Модуль classes, влючает в себя все классы, которые распологаются в разных файлах:

1. category.py имеет класс Category. Атрибуты класса Category，которые описаны в конструкторе init:
название (name)
описание (description)
список товаров категории (products): 
Атрибут products является приватным и возвращает значение через метод products в формате <"Название товара", "цена товара" руб. Остаток: "количество товара" шт.>.


Метод repr для отладки(для разработчика), который возвращает строковое представление объектов класса. 
Метод str для пользователя, который возвращает строковое представление объектов класса, в виде: "Название категории, количество продуктов: 47 шт.".
Метод add_product принимает экземпляр класса Product и добавляет его в список продуктов данной категорий, если его ещё нет, если такой товар уже есть, то сравнивает цену и выбирает большую, количество товара сумируется.
Метод products, реаализованный при помощи декоратора @property, возвращает строку вида: "Название продукта, цена руб. количество шт.".
Метод get_total_items, возвращает общее количество товаров на складе

2. product.py имеет класс Product. Атрибуты класса Product, которые описаны в конструкторе init:
название (name)
описание (description)
цена (price)
количество в наличии (quantity)
Атрибут price является приватным, к нему можно обратиться через метод price.

Метод repr для отладки(для разработчика), который возвращает строковое представление объектов класса.
Метод str для пользователя, который возвращает строковое представление объектов класса, в виде: "Название товара, цена товара, Остаток: 47 шт.".
Метод add, производит сложение стоимости всех товаров на складе.
Метод new_product принимает на вход словарь и распаковывет его создавая экземпляр класса Product.
Метод выполнен, как класс-метод. Метод price, реаализованный при помощи декоратора @property, возвращает значение цены товара. Также имеет сеттер, для установки новой цены и проверок ошибок, в случае нулевой или цены ниже нуля.

3. lawn_grass.py имеет класс LawnGrass, который является подклассом класса Product. Атрибуты класса LawnGrass, которые описаны в конструкторе init:
название (name)
описание (description)
цена (price)
количество в наличии (quantity)
страна-производитель (country)
срок прорастания (germination_period)
цвет (color)

Метод repr для отладки(для разработчика), который возвращает строковое представление объектов класса.

4. smartphone.py имеет класс Smartphone, который является подклассом класса Product. Атрибуты класса Smartphone, которые описаны в конструкторе init:
название (name)
описание (description)
цена (price)
количество в наличии (quantity)
производительность (efficiency)
модель (model)
объем встроенной памяти (memory)
цвет (color)

Метод repr для отладки(для разработчика), который возвращает строковое представление объектов класса.

5. product_iterator.py имеет класс ProductIterator.Класс для итерации товаров одной категории Атрибуты класса ProductIterator, которые описаны в конструкторе init:
категория (category)
индекс = 0

Методы iter и next, позволяют перебирать все товары в цикле.



Тестирование: В пакете tests проведено тестирование модулей. В модуле conftest содержатся фикстуры для тестирования. Тестирование осуществлять через пользовательский ввод .