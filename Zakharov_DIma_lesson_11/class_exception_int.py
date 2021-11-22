# Задание 3
class IntHandler:
    num_lust = list()

    @classmethod
    def _add_element(cls, user_list):
        for el in user_list:
            try:
                res_el = float(el)
            except ValueError:
                continue
            else:
                if res_el > int(res_el):
                    IntHandler.num_lust.append(res_el)
                else:
                    IntHandler.num_lust.append(int(res_el))
        # IntHandler.num_lust = (el for el in user_list if isinstance(el, int) or isinstance(el, float))
        print(list(IntHandler.num_lust))

    @classmethod
    def request_user_list(cls):
        user_list = list()
        while True:
            answer = input("Введите число, чтобы добавить его в список\n"
                           "Напишите 'stop' чтобы закончить: ")
            if answer == 'stop':
                break
            else:
                user_list.append(answer)
        IntHandler._add_element(user_list)


if __name__ == '__main__':
    IntHandler.request_user_list()
