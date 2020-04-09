from functools import reduce


def fibo_gen():
    my_gen = [[el for el in range(1, i)] for i in range(2, 17)]
    gen = (reduce(lambda a, b=1: a * b, my_gen[i])
           for i in range(len(my_gen)))
    for el in gen:
        yield el


for el in fibo_gen():
    print(el)
