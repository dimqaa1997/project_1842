# Не уверен, что верно понял задание)))
# Но список тут только один
list_cubes_uneven_numbers = []
for number in range(1, 1001, 2):
    element = number ** 3
    list_cubes_uneven_numbers.append(element + 17)
print(list_cubes_uneven_numbers)
counter = 0
res_sum = 0
for num in list_cubes_uneven_numbers:
    total = 0
    while num != 0:
        total += num % 10
        num //= 10
    if total % 7 == 0:
        res_sum += list_cubes_uneven_numbers[counter]
    counter += 1
print(res_sum)
