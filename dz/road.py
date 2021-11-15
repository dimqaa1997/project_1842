# Задание 2

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    @staticmethod
    def get_mass(_length, _width):
        result_mess = _length * _width * 25 * 5
        print(result_mess)


if __name__ == '__main__':
    asphalt = Road(20, 5000)
    asphalt.get_mass(20, 5000)
