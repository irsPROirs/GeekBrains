def first_up(my_str):
    my_str = list(my_str)
    my_str[0] = my_str[0].upper()
    my_str = ''.join(my_str)
    return my_str


my_list = input('Введите слова через пробел: ').split()
for i in my_list:
    print(first_up(i), end=' ')
