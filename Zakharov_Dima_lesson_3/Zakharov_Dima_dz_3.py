def thesaurus(name_list):
    result_dict = {}
    for name in name_list:
        counter = 0
        while counter == 0:
            first_letter = name[counter]
            if first_letter not in result_dict.keys():
                result_dict.fromkeys(first_letter)
                result_dict[first_letter] = list()
                result_dict[first_letter].append(name)
            else:
                result_dict[first_letter].append(name)
            counter += 1
    return result_dict


test = thesaurus(["Иван", "Мария", "Петр", "Илья"])
print(test)
