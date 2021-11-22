# Задание 2
class ZeroHandler:
    def __init__(self, number):
        self.num = number

    @staticmethod
    def __handler_zero():
        print("нельзя делить на ноль")

    def __truediv__(self, other):
        try:
            res = self.num / other
        except ZeroDivisionError:
            ZeroHandler.__handler_zero()
        else:
            return res


if __name__ == '__main__':
    num = ZeroHandler(10)
    print(num / 2)

    num = ZeroHandler(10)
    print(num / 0)
