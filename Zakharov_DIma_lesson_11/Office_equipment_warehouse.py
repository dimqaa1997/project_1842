# Задания 4, 5, 6
class Storage:
    storage_dict = {}

    @classmethod
    def __valid_data(cls, num):
        if isinstance(num, int):
            return True
        else:
            return False

    @classmethod
    def give_to_warehouse(cls, name, quantity):
        if Storage.__valid_data(num=quantity):
            if Storage.storage_dict.get(name):
                Storage.storage_dict[f'{name}'] += quantity
                print(f"{name} в количестве {quantity} добавлен на склад")
            else:
                Storage.storage_dict[f'{name}'] = quantity
                print(f"{name} в количестве {quantity} добавлен на склад")
        else:
            print("невнрный формат данных\n"
                  "нужно число")

    @classmethod
    def get_to_warehouse(cls, name, quantity, subdivision):
        if Storage.__valid_data(num=quantity):
            try:
                Storage.storage_dict[name] -= quantity
            except KeyError:
                print(f"{name} нет на складе")
            else:
                print(f"{name} в количестве {quantity} шт было направлено в подразделение {subdivision}")
        else:
            print("невнрный формат данных\n"
                  "нужно число")


class OfficeEquipment:
    name = ''
    stationary = True

    @staticmethod
    def get_copy():
        pass


class Printer(OfficeEquipment):
    name = "printer"
    consumes_paint = True

    @staticmethod
    def get_copy():
        print("Создает бумажную копию цифрового объекта")


class Scanner(OfficeEquipment):
    name = "scanner"
    consumes_paint = False

    @staticmethod
    def get_copy():
        print("Создает цифровую копию бумажного объекта")


class Xerox(OfficeEquipment):
    name = "xerox"
    consumes_paint = True

    @staticmethod
    def get_copy():
        print("Копирует физическую бумагу")


if __name__ == '__main__':
    printer = Printer()
    print(printer.stationary)
    printer.get_copy()

    scanner = Scanner()

    xerox = Xerox()

    Storage.give_to_warehouse(printer.name, 5)
    print(Storage.storage_dict['printer'], type(Storage.storage_dict['printer']))

    Storage.give_to_warehouse(printer.name, 5)
    print(Storage.storage_dict)

    Storage.give_to_warehouse(scanner.name, 5)
    print(Storage.storage_dict)

    Storage.give_to_warehouse(xerox.name, 7)
    print(Storage.storage_dict)

    Storage.get_to_warehouse(printer.name, 1, "бухгалтерия")
    print(Storage.storage_dict)

    Storage.get_to_warehouse(scanner.name, 2, "отдел развития чувства вины")
    print(Storage.storage_dict)

    Storage.get_to_warehouse(xerox.name, 3, "отдел рапределения")
    print(Storage.storage_dict)

    Storage.give_to_warehouse(xerox.name, 'два')
    print(Storage.storage_dict)

    Storage.get_to_warehouse(scanner.name, "one", "отдел развития чувства вины")
    print(Storage.storage_dict)

    # some_dict = dict()
    # print(some_dict['some'])
