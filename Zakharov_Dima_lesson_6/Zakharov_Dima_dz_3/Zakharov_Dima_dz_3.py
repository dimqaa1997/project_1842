import json


def get_result_dict():
    with open('users.csv', 'r', encoding='utf-8') as fp:
        user_list = list(map(lambda el: el.strip(), fp.readlines()))

    with open('hobby.csv', 'r', encoding='utf-8') as fp:
        hobby_list = list(map(lambda el: el.strip(), fp.readlines()))

    if len(user_list) >= len(hobby_list):
        delta = len(user_list) - len(hobby_list)
        for _ in range(delta):
            hobby_list.append(None)
        for key, value in zip(user_list, hobby_list):
            hobbies_of_users[key] = value
        return hobbies_of_users

    else:
        return "Error: 1"


def write_to_file(hobbies_of_users_dict):
    with open('hobbies_of_users.json', 'w', encoding='utf-8') as fp:
        json.dump(hobbies_of_users_dict, fp, ensure_ascii=False)

    with open('hobbies_of_users.txt', 'w', encoding='utf-8') as fp:
        fp.write(str(hobbies_of_users_dict))


if __name__ == '__main__':
    hobbies_of_users = dict()
    hobby_user_dict = get_result_dict()
    # print(hobby_user_dict)
    write_to_file(hobby_user_dict)

    with open('hobbies_of_users.json', 'r', encoding='utf-8') as fp:
        rf_dict = json.load(fp)
        # rf_dict = fp.read()
    print('json', rf_dict, type(rf_dict), sep='\n')

    with open('hobbies_of_users.txt', 'r', encoding='utf-8') as fp:
        rf_dict = fp.read()
    print('txt', rf_dict, type(rf_dict), sep='\n')
