class Cell:
    def __init__(self, param):

        self.param = param

    def __add__(self, other):
        return self.param + other.param

    def __sub__(self, other):
        if self.param - other.param > 0:
            result = self.param - other.param
        else:
            result = 'Ошибка, результат меньше или равен нулю'
        return result

    def __mul__(self, other):
        return self.param * other.param

    def __truediv__(self, other):
        return self.param // other.param

    def make_order(self, kol):
        order_list = ['*' * kol for i in range(self.param // kol)]
        order_list.append('*' * (self.param % kol))
        order = '\n'.join(order_list)
        return order


cell1 = Cell(12)
cell2 = Cell(15)
print(cell1 - cell2)
print(cell1 + cell2)
print(cell1 / cell2)
print(cell1 * cell2)
print(cell1.make_order(5))
print(cell2.make_order(5))
