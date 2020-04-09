from sys import argv


def calc(prod, hour, prize):
    return int(prod) * int(hour) + int(prize)


print('ЗП сотрудника =', calc(argv[1], argv[2], argv[3]))
