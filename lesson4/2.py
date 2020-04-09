my_list = input('Введите список чисел через пробел: ').split()
my_list = [my_list[i] for i in range(len(my_list)) if i > 0 and int(my_list[i]) > int(my_list[i - 1])]
print(my_list)
