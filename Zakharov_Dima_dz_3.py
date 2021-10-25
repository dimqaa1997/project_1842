string_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(f'исходный список: {string_list}')
print(id(string_list), '\n')

element = 0
while element != len(string_list):
    if string_list[element].isdigit() or '+' in string_list[element]:
        string_list.insert(element, '"')
        string_list.insert(element + 2, '"')
        element += 1

    if '+' in string_list[element]:
        problem_digit = string_list.pop(element)
        string_list.insert(element, problem_digit[0])
        char = 0
        while char < len(problem_digit):
            if len(problem_digit) == 2:
                string_list[element] += '0'
                char += 1
            elif problem_digit[char] == '+':
                char += 1
            string_list[element] += problem_digit[char]
            char += 1
    elif len(string_list[element]) == 1 and string_list[element].isdigit():
        string_list[element] = f'0{string_list[element]}'

    element += 1

print(f'обработанный список: {string_list}')
print(id(string_list), '\n')

i = 0
while i < len(string_list):
    if '"' in string_list[i]:
        string_list[i] += string_list.pop(i + 1) + string_list.pop(i + 1)

    i += 1

print(f"результирующая сторока: {' '.join(string_list)}")
print(id(string_list))
