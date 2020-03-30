vyr = int(input('введите выручку: '))
izd = int(input('введите издержки: '))
if vyr > izd:
    print('Прибыль')
    print('Рентабильность:', (vyr - izd) / vyr)
    count = int(input('введите количество сотрудников: '))
    print('Прибыль на 1 сотрудника:', (vyr - izd) / count)
elif vyr < izd:
    print('Убыток')
