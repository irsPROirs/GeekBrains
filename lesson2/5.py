my_list = [7, 5, 3, 3, 2]
r = int(input('Введите новый элемент рейтинга: '))
for i in range(len(my_list)):
    if i == len(my_list)-1 and my_list[i] > r:
        my_list.append(r)
        break
    elif my_list[i] > r:
        continue
    elif my_list[i] == r:
        my_list.insert(i+1, r)
        break
    else:
        my_list.insert(i, r)
        break
print(my_list)
