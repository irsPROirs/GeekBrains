def my_func(var_1, var_2, var_3):
    min_var = min(var_1, var_2, var_3)
    sum_var = 0
    if var_1 > min_var:
        sum_var += var_1
    if var_2 > min_var:
        sum_var += var_2
    if var_3 > min_var:
        sum_var += var_3
    return sum_var


var_1 = int(input('введите переменную 1: '))
var_2 = int(input('введите переменную 2: '))
var_3 = int(input('введите переменную 3: '))
result = my_func(var_1, var_2, var_3)
print(result)
