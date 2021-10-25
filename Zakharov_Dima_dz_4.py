my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
element = 0
while element != len(my_list):
    my_tuple = my_list[element].split()
    print(f'Привет, {my_tuple[-1].capitalize()}')
    element += 1
print('The end')