from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass

    @abstractmethod
    def __repr__(self):
        pass
