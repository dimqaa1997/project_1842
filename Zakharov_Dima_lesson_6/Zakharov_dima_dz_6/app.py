import sys
from core import get_data, write_data

if __name__ == '__main__':
    command = sys.argv[1]
    if command == 'get_data':
        if len(sys.argv) == 2:
            get_data()
        elif len(sys.argv) == 3:
            get_data(sys.argv[2])
        else:
            get_data(sys.argv[2], sys.argv[3])

    elif command == 'write_data':
        write_data(price=sys.argv[2])

    elif command == 'help':
        print("write_data - записывает сумму продаж в файл\n"
              "get_data без параметров - выводит все записи\n"
              "get_data с одним параметром (номер записи) - выводит все записи начиная с номера, указанного в параметре\n"
              "det_data с двумя параметрами - выводит записи начиная с первого параметра и заканчивая вотрым")
