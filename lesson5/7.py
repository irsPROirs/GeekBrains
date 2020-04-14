import json

with open('txt/7.txt') as my_f:
    my_list = my_f.readlines()
srar = float()
final_list = []
firm_dict = {}
average_dict = {}
pr = []
k = int()
for l in my_list:
    firm = l.split()
    profit = int(firm[2]) - int(firm[3])
    pr.append(profit)
    if profit > 0:
        srar += profit
        k += 1
    firm_dict[firm[0]] = profit
average_dict['average_profit'] = int(srar / k * 100) / 100
final_list.append(firm_dict)
final_list.append(average_dict)
print(final_list)
with open('txt/7(2).json', 'w') as f:
    json.dump(final_list, f)
