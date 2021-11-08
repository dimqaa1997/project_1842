import os


def create_folder(name):
    os.mkdir(name)
    print(f'директория с именем {name} успешно создана')


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as fp:
        if text:
            fp.write(text)
    print(f"файл с именем {name} успешно создан")


def get_scan_document():
    with open('config.yaml', 'r', encoding='utf-8') as fp:
        for line in fp:
            if line.startswith('! '):
                main_folder = line.strip('! \n')
                try:
                    create_folder(main_folder)
                except FileExistsError as e:
                    print(f"папка с именем {main_folder} уже существует")
                    main_folder_path = os.getcwd() + f"\\{main_folder}"
                    continue
                else:
                    main_folder_path = os.getcwd() + f"\\{main_folder}"

            elif line.startswith('  | -'):
                os.chdir(main_folder_path)
                sub_folder = line.strip('| -\n')
                try:
                    create_folder(sub_folder)
                except FileExistsError:
                    print(f"папка с именем {sub_folder} уже существует")
                    sub_folder_path = os.getcwd() + f"\\{sub_folder}"
                    continue
                else:
                    sub_folder_path = os.getcwd() + f"\\{sub_folder}"

            elif '.py' in line:
                new_file = line.strip(' |-\n')
                os.chdir(sub_folder_path)
                try:
                    create_file(new_file)
                except FileExistsError:
                    print(f"файл с именем {new_file} уже существует")
                    continue

            elif line.startswith('  |--| -'):
                os.chdir(sub_folder_path)
                sub_sub_folder = line.strip(' |-\n')
                try:
                    create_folder(sub_sub_folder)
                except FileExistsError:
                    print(f"папка с именем {sub_sub_folder} уже существует")
                    sub_sub_folder_path = os.getcwd() + f"\\{sub_sub_folder}"
                    continue
                else:
                    sub_sub_folder_path = os.getcwd() + f"\\{sub_sub_folder}"

            elif line.startswith('  |--|--| -'):
                os.chdir(sub_sub_folder_path)
                super_sub_folder = line.strip(' |-\n')
                try:
                    create_folder(super_sub_folder)
                except FileExistsError:
                    print(f"папка с именем {super_sub_folder} уже существует")
                    super_sub_folder_path = os.getcwd() + f"\\{super_sub_folder}"
                    continue
                else:
                    super_sub_folder_path = os.getcwd() + f"\\{super_sub_folder}"

            elif '.html' in line:
                os.chdir(super_sub_folder_path)
                new_file = line.strip(' |-\n')
                try:
                    create_file(new_file)
                except FileExistsError:
                    print(f"файл с именем {new_file} уже существует")

        print('end')


if __name__ == '__main__':
    get_scan_document()
