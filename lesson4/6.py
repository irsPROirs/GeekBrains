from itertools import count, cycle
from sys import argv

if argv[1] == '1':
    start_num = int(argv[2])
    for i in count(start_num, 2):
        print(i)
elif argv[1] == '2':
    my_list = ['one', 2, True]
    for i in cycle(my_list):
        print(i)
elif argv[1] == 'help':
    print('1 - скрипт генерирующий беск. целые числа\n'
          '2 - скрипт повторяющихся эл - тов списка')
