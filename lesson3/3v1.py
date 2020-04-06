def my_func(var):
    min_var = min(var)
    var = [int(i) for i in var if i not in min_var]
    return sum(var)


var = input('введите данные через пробел: ').split()
result = my_func(var)
print(result)
