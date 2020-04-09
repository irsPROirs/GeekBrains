my_list = [1, 2, 3, 3, 4, 1, 2, 4, 5, 6, 7, 1, 2]
new_list = [i for i in my_list if my_list.count(i) == 1]
print(new_list)
