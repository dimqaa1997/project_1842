import os
import shutil


def get_copy_templates():
    pass
os.chdir("my_project")
root_path = os.getcwd()
try:
    os.mkdir('templates')
except FileExistsError:
    print('папка уже существует')
target_path = root_path + '\\templates'
list_dir = os.listdir(root_path)

for root, dirs, file in os.walk(root_path, topdown=False):
    for name in dirs:
        if name == 'templates':
            folder = os.path.join(root, name)
            os.chdir(folder)
            print(os.listdir(), type(os.listdir()))
            try:
                sub_folder = os.listdir()[-1]
            except IndexError:
                print("пустой список")
            else:
                print(sub_folder)
                if sub_folder:
                    try:
                        shutil.copytree(os.path.join(folder, sub_folder), target_path + f"\\{sub_folder}")
                    except FileExistsError:
                        print("уже скопировано")
