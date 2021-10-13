list_cubes_uneven_numbers = []
for number in range(1, 1001, 2):
    element = number ** 3                            # Прибавил число 17 к каждому элементу списка
    list_cubes_uneven_numbers.append(element + 17)
print(list_cubes_uneven_numbers)
res_list = []
counter = 0
for num in list_cubes_uneven_numbers:
    total = 0
    while num != 0:
        total += num % 10
        num //= 10
    if total % 7 == 0:
        res_list.append(list_cubes_uneven_numbers[counter])
    counter += 1
res_sum = 0
for element in res_list:
    res_sum += element
print(res_sum)
