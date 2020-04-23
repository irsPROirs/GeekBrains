import random as r


class Player:
    def __init__(self, name):
        self.name = name
        self.card_list = [i for i in range(1, 91)]
        r.shuffle(self.card_list)
        self.card = [sorted([self.card_list.pop() for i in range(5)]) for i in range(3)]
        for i in self.card:
            for j in range(4):
                i.insert(r.randint(0, 8), ' ')

    def __str__(self):
        return '\n'.join([' '.join([str(elem) for elem in line]) for line in self.card])

    @property
    def check_card(self):
        number = 0
        for i in range(len(self.card)):
            number += self.card[i].count('-')
        return number


class Game(Player):
    def __init__(self, human, comp):
        super().__init__(name='')
        self.human = human
        self.comp = comp
        self.numbers_list = [i for i in range(1, 91)]
        r.shuffle(self.numbers_list)

    def start_game(self):
        print('Добро пожаловать ' + self.human.name + ' и ' + self.comp.name)
        f = True
        while f:
            kol = 0
            keg = self.numbers_list.pop()
            print('------------------------')
            print('Выпал боченок: ' + str(keg) + ' (осталось' + ' ' + str(len(self.numbers_list)) + ')')
            print('--Карточка пользователя--:')
            print(self.human)
            print('------Карточка ПК:------:')
            print(self.comp)
            question = input('Зачеркнуть y/n: ')
            for i in self.human.card:
                for j in i:
                    if j != keg and question == 'y':
                        kol += 1
                    elif j == keg and question != 'y':
                        kol = 15
                    if j == keg and question == 'y':
                        i[i.index(j)] = '-'
                        continue
            if kol == 15:
                f = False
                print('Вы ошиблись')
            if r.random() < 0.01:
                f = False
                print('Вы ПОБЕДИЛИ из - за ошибки компьютера')
            for i in self.comp.card:
                for j in i:
                    if j == keg:
                        i[i.index(j)] = '-'
            if self.human.check_card == 15:
                print('Вы ПОБЕДИЛИ')
                f = False
            elif self.comp.check_card == 15:
                print('Выиграл ПК')
                f = False
        else:
            print('Конец игры')


human = Player('Человек')
comp = Player('Компьютер')
game = Game(human, comp)
game.start_game()
