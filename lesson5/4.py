first_file = open('txt/4.txt')
second_file = open('txt/4(2).txt', 'w')
my_list = ['Один', 'Два', 'Три', 'Четыре']
lines = first_file.readlines()
i = 0
for line in lines:
    space = line.find(' ')
    print(line[:space])
    line = line.replace(line[:space], my_list[i])
    i += 1
    second_file.writelines(line + '\n')
first_file.close()
second_file.close()
