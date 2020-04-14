my_str = None
my_file = open('txt/1.txt', 'w')
while my_str != '':
    my_str = input('введите строки через пробел:')
    my_file.write(my_str+'\n')
my_file.close()
