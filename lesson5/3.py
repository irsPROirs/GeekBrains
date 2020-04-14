srar = float()
list_of_emp = list()
kol = int()
my_f = open('txt/3.txt', encoding='utf-8')
lines = my_f.readlines()
for line in lines:
    my_list = line.split()
    srar += float(my_list[1])
    kol += 1
    if int(my_list[1]) < 20000:
        list_of_emp.append(my_list[0])
if len(list_of_emp) != 0:
    print('Сотрудники с окладом < 20000:\n', list_of_emp)
print('Средний доход =', srar/kol)
my_f.close()
