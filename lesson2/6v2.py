d = list()
f = list()
while True:
    a = int(input('ведите номер товара: '))
    while True:
        b = tuple(input('введите характеристику товара и её значение через пробел: ').split(' '))
        d.append(b)
        question = input('Хотите ввести еще аттрибуты? (y/n) ')
        if question != 'y':
            break
    e = dict(d)
    g = (a, e)
    f.append(g)
    question = input('Хотите ввести еще товар? (y/n) ')
    if question != 'y':
        break
print('Выборка: ')
k = 0
d = list(dict(f).get(1).keys())
while k in range(len(d)):
    c = []
    i = 1
    while i in range(len(f)+1):
        c.append(dict(f).get(i).get(d[k]))
        i += 1
    final = {d[k]: list(set(c))}
    print(final)
    k += 1
