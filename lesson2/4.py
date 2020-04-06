my_list = list(input('Введите строку из слов через пробел: ').split(' '))
for i, j in enumerate(my_list, start=1):
    print(i, j[:10])
