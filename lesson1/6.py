a = int(input('введите a: '))
b = int(input('введите b: '))
counter = 1
while a < b:
    a = a+0.1*a
    counter += 1
print(f'на {counter}-й день спортсмен достиг результата — не менее {b} км.')
