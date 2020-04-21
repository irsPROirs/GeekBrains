from abc import ABC, abstractmethod


class Clothes:
    @abstractmethod
    def __init__(self, param):
        self.param = param

    @property
    def coat_method(self):
        return self.param / 6.5 + 0.5

    @property
    def costume_method(self):
        return self.param * 2 + 0.3

    def __add__(self, other):
        return self.param / 6.5 + 0.5 + other.param * 2 + 0.3


class Boots(Clothes):
    def __init__(self, size):
        super().__init__(self)
        self.size = size

    def boots_method(self):
        pass


coat = Clothes(54)
costume = Clothes(42)
print(coat + costume)
print(coat.coat_method + costume.costume_method)
