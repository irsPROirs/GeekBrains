with open('txt/6.txt', encoding='utf-8') as my_f:
    my_list = my_f.readlines()
my_dict = {}
num = ''

for l in my_list:
    digits = []
    my_str = ''
    res = l.find(':')
    my_str = l[:res]
    for i in l[res:]:
        if i.isdigit():
            num = num + i
        elif num != '':
            digits.append(int(num))
            num = ''
    my_dict[my_str] = sum(digits)
print(my_dict)
