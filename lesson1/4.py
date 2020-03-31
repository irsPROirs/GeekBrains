n = input('введите число: ')
i = 1
m = int(n[0])
while i in range(len(n)):
    if int(n[i]) > m:
        m = int(n[i])
    i += 1
print('Максимальное число:', m
