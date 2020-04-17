class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(self.title, 'Пишет')


class Pencil(Stationery):
    def draw(self):
        print(self.title, 'Рисует')


class Handle(Stationery):
    def draw(self):
        print(self.title, 'Закрашивает')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
other = Stationery('Другое')
other.draw()
pen.draw()
pencil.draw()
handle.draw()
