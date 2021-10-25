words_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(num):
    if num in words_dict.keys():
        return words_dict[num]
    elif num.lower() in words_dict.keys():
        return words_dict[num.lower()].capitalize()
    else:
        return None


user_answer = ''
while user_answer.lower() != 'stop':
    user_answer = input('Чтобы выйти из программы напишите "stop"\nВведите числительное на английском: ')
    print(num_translate_adv(user_answer))
else:
    print('Работа программы завершена')
