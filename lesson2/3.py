month = int(input('Введите месяц: '))
months_list = ['зима', 'весна', 'лето', 'осень']
month_dict = {12: months_list[0], 1: months_list[0], 2: months_list[0],
              3: months_list[1], 4: months_list[1], 5: months_list[1],
              6: months_list[2], 7: months_list[2], 8: months_list[2],
              9: months_list[3], 10: months_list[3], 11: months_list[3]}
print(month_dict.get(month)) if month_dict.get(month) else print('Такого месяца не существет')
