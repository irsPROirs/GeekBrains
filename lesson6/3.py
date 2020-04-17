class Worker:
    _income = {"wage": 15, "bonus": 13}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = self._income


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self.income["wage"] + self.income["bonus"]


mike = Position('Mike', 'Ivanov', 'DevOps')
print(mike.get_full_name())
print(mike.get_total_income())
