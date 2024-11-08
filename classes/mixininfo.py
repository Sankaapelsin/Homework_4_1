class MixinInfo:
    """Класс миксин для вывода в консоль информацию об объекте"""

    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}{tuple(self.__dict__.values())}"
