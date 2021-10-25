# Задание 5_А
from copy import copy

price_list = [65.2, 68.95, 12.06, 84.60, 545.03, 51.4, 5.5, 13.9, 95.6, 85.5]
print(id(price_list), price_list)
price = 0
rub, penny = 'руб', 'коп'
res_list = []
while price != len(price_list):
    temp_var = int((price_list[price] * 100) % 100)
    res_list.extend([str(int(price_list[price])), rub])
    if 1 <= temp_var <= 9:
        temp_var = '0' + str(temp_var)
        res_list.extend([temp_var, penny])
    else:
        res_list.extend([str(temp_var), penny])

    print(temp_var, end=' ')
    price += 1
print('\n', price_list)
print(res_list)
print(' '.join(res_list))

# Задание 5_B
price_list = [65.2, 68.95, 12.06, 84.60, 545.03, 51.4, 5.5, 13.9, 95.6, 85.5]
price_list.sort()
print(id(price_list), price_list)

# Задание 5_C
price_list = [65.2, 68.95, 12.06, 84.60, 545.03, 51.4, 5.5, 13.9, 95.6, 85.5]
new_revers_list = copy(price_list)
new_revers_list.reverse()
print(id(new_revers_list), new_revers_list)

# Задание 5_D
price_list = [65.2, 68.95, 12.06, 84.60, 545.03, 51.4, 5.5, 13.9, 95.6, 85.5]
price_list.sort()
print(id(price_list[-1:-6:-1]), price_list[-1:-6:-1])
