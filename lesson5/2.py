my_f = open('txt/2.txt')
lines = my_f.readlines()
for line in lines:
    print('Количество слов в строке', line.count(' ')+1)
print('Количество строк =', len(lines))
my_f.close()
