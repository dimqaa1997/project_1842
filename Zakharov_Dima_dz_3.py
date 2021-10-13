number_list = list(range(1, 101))
word = 'процент'
num_list_ov = number_list[4:20]
for number in number_list:
    if number in num_list_ov:
        print(number, word + 'ов')
    elif number % 10 == 1:
        print(number, word)
    elif number % 10 == 2 or number % 10 == 3 or number % 10 == 4:
        print(number, word + 'a')
    else:
        print(number, word + 'ов')
