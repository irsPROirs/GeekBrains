my_f = open('txt/5.txt', 'w+')
my_list = input()
my_f.write(my_list)
my_f.seek(0)
my_list = my_f.readline().split()
my_list = [int(i) for i in my_list]
print('Сумма =', sum(my_list))
my_f.close()
