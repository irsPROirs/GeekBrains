import random as r


class Game:
    def __init__(self):
        self.numbers_list = [i for i in range(1, 91)]
        self.card_list = [i for i in range(1, 91)]
        r.shuffle(self.numbers_list)
        r.shuffle(self.card_list)
        self.user_card = [sorted([self.card_list.pop() for i in range(5)]) for i in range(3)]
        self.comp_card = [sorted([self.card_list.pop() for i in range(5)]) for i in range(3)]

    def __str__(self):
        return '\n'.join([' '.join([str(elem) for elem in line]) for line in self.user_card])

    @staticmethod
    def check_card(card):
        number = 0
        for i in range(len(card)):
            number += card[i].count('-')
            return number

    def start_game(self):

        print('Добро пожаловать')
        f = True
        while f:
            kol = 0
            keg = self.numbers_list.pop()
            print('------------------------')
            print('Выпал боченок: ' + str(keg) + ' (осталось' + ' ' + str(len(self.numbers_list)) + ')')
            print('--Карточка пользователя--:')
            print(self.user_card)
            print('-------Карточка ПК:-------:')
            print(self.comp_card)
            question = input('Зачеркнуть y/n: ')
            for i in self.user_card:
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

            for i in self.comp_card:
                for j in i:
                    if j == keg:
                        i[i.index(j)] = '-'
            if r.random() < 0.01:
                f = False
                print('Вы ПОБЕДИЛИ из - за ошибки компьютера')
            if Game().check_card(self.user_card) == 15:
                print('Вы ПОБЕДИЛИ')
                f = False
            elif Game().check_card(self.comp_card) == 15:
                print('Выиграл ПК')
                f = False
        else:
            print('Конец игры')


game = Game()
game.start_game()
