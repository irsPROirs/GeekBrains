my_list = list(input('Введите список эл-тов через пробел: ').split(' '))
print(my_list)
i = 0
while i in range(len(my_list)-1):
    t = my_list[i]
    my_list[i] = my_list[i+1]
    my_list[i + 1] = t
    i += 2
print(my_list)
