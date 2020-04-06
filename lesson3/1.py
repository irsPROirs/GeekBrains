def my_func(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = 'Деление на 0'
    return result


a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))
print(my_func(a, b))
