import json
import os


# Если значение ключа сразу сделать кортежем, то не получается изменить количество файлов удв условиям
# Поэтому сделал сначала список, а потом привел к кортежу


def get_extensions(path_f, root, file):
    path_f = os.path.split(os.path.join(root, file))
    name_and_ext = path_f[-1].split('.')
    return name_and_ext[-1]


def get_size_dict(current_path):
    size_dict = {
        '100': [0, list()],
        '1000': [0, list()],
        '10000': [0, list()],
        '100000': [0, list()],
        'others': [0, list()]

    }

    for root, dirs, files in os.walk(current_path, topdown=False):
        for file in files:
            file_size = os.stat(os.path.join(root, file)).st_size
            if file_size <= 100:
                file_extension = get_extensions(os.path.split(os.path.join(root, file)), root, file)
                size_dict['100'][0] += 1
                size_dict['100'][-1].append(file_extension)

            elif 100 < file_size <= 1000:
                file_extension = get_extensions(os.path.split(os.path.join(root, file)), root, file)
                size_dict['1000'][0] += 1
                size_dict['1000'][-1].append(file_extension)

            elif 1000 < file_size <= 10000:
                file_extension = get_extensions(os.path.split(os.path.join(root, file)), root, file)
                size_dict['10000'][0] += 1
                size_dict['10000'][-1].append(file_extension)

            elif 10000 < file_size <= 100000:
                file_extension = get_extensions(os.path.split(os.path.join(root, file)), root, file)
                size_dict['100000'][0] += 1
                size_dict['100000'][-1].append(file_extension)

            else:
                file_extension = get_extensions(os.path.split(os.path.join(root, file)), root, file)
                size_dict['others'][0] += 1
                size_dict['others'][-1].append(file_extension)

    for key, value in size_dict.items():
        value[-1] = list(set(el for el in value[-1]))
        value = tuple(value)
        print(key, value)

    return size_dict


def serialize_dict(current_path, res_size_dict):
    current_path_list = current_path.split('\\')
    folder_name = current_path_list[-1]

    with open(f"{folder_name}.json", "w", encoding="utf-8") as fp:
        json.dump(res_size_dict, fp, ensure_ascii=False)


if __name__ == '__main__':
    # cur_path = os.path.join(os.getcwd(), 'my_project')
    cur_path = os.getcwd()
    size_dict = get_size_dict(cur_path)
    print(cur_path, type(cur_path))
    serialize_dict(cur_path, size_dict)
