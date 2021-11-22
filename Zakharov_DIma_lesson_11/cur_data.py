# Задание 1
import re


class Date:

    @staticmethod
    def valid_date(date_string):
        pattern = re.compile(r'(\d{2}\-){2}\d{4}')
        match = pattern.fullmatch(date_string)
        if match:
            return True
        else:
            return False

    @classmethod
    def get_date(cls, data_string):
        if Date.valid_date(data_string):
            date_list = data_string.split('-')
            for number in date_list:
                number = int(number)
                print(number, type(number))
        else:
            print("Неверный формат")


if __name__ == '__main__':
    string_2 = '21.03.1997'
    Date.get_date(string_2)
    print(Date.valid_date(string_2))
