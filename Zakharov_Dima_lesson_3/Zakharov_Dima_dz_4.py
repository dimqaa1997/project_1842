def thesaurus_adv(name_list):
    result_dict = dict()

    for name in name_list:
        res_tuple = list()
        new_list = name.split()
        first_name, last_name = new_list
        res_tuple.append(first_name)
        res_tuple.append(last_name)

        counter = 0
        while counter == 0:
            letter_one = res_tuple[-1]
            first_letter = letter_one[0]
            letter_two = res_tuple[0]
            second_letter = letter_two[0]

            if first_letter not in result_dict.keys():
                result_dict.fromkeys(first_letter)
                result_dict[first_letter] = dict
                result_dict[first_letter] = {second_letter: [name]}

            elif first_letter in result_dict.keys() and second_letter not in result_dict[first_letter].keys():
                result_dict[first_letter].fromkeys(second_letter)
                result_dict[first_letter][second_letter] = list()
                result_dict[first_letter][second_letter].append(name)

            elif first_letter in result_dict.keys() and second_letter in result_dict[first_letter].keys():
                result_dict[first_letter][second_letter].append(name)

            counter += 1

    return result_dict


test = thesaurus_adv(["Иван Иванов", "Мария Акимова", "Петр Первый", "Илья Пророк", "Ирина Илидан", "Алексей Воробьев",
                      "Сергей Воронов", "Александр Волков"])
print(test)
