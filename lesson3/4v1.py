def my_func(x, y):
    i = -1
    result = 1
    while i >= y:
        result = result * 1 / x
        i += -1
    return result


x = int(input('введите переменную x: '))
y = int(input('введите переменную y: '))
result = my_func(x, y)
print(result)