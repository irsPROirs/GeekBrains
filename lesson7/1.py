import random


class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for i in self.my_list:
            for j in i:
                print(j, end=' ')
            print('\n', end='')
        return ''

    def __add__(self, other):
        result = []
        for i in range(len(self.my_list)):
            new_matr = [self.my_list[i][j] + other.my_list[i][j] for j in range(len(self.my_list[i]))]
            result.append(new_matr)
        return Matrix(result)


n = 3
m = 5
matr1 = [[random.randint(0, 100) for j in range(m)] for i in range(n)]
matr2 = [[random.randint(0, 100) for j in range(m)] for i in range(n)]
matrix1 = Matrix(matr1)
matrix2 = Matrix(matr2)
print('Первая матрица:')
print(matrix1)
print('Вторая матрица:')
print(matrix2)
print('Сумма:')
print(matrix1 + matrix2)
