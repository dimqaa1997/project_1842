import sys


def get_enum(names_list, klasses_list):
    if len(names_list) > len(klasses_list):
        while len(klasses_list) != len(names_list):
            klasses_list.append(None)
    for tutor in range(len(names_list)):
        yield (names_list[tutor], klasses_list[tutor])


if __name__ == '__main__':
    tutors_1 = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена', 'Катя', 'Вика', 'Петр', 'Сергей', 'Лена'
    ]

    klasses = [
        '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
    ]

    res = get_enum(tutors_1, klasses)
    print(res, type(res), sys.getsizeof(res), next(res), next(res), next(res), list(res), sep='\n')
