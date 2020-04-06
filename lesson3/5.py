def my_func(my_str, result, f_fun):
    for i in range(len(my_str)):
        try:
            result = result + int(my_str[i])
        except:
            f_fun = False
            print('Введен стоп символ "/"')
            break
    print('Промежуточная сумма =', result)
    return result, f_fun


result_sum = int()
f = True
while f:
    my_str = input('введите числа через пробел или "/" для остановки: ').split()
    result_sum, f = my_func(my_str, result_sum, f)
print('Итог:', result_sum)
