# Задание 2
class Clothes:
    def __init__(self, name, size, height):
        self.name = name
        self.size = size
        self.height = float(height)

    @property
    def get_quantity(self):
        if self.name == 'coat':
            return self.size / 6.5 + 0.5
        elif self.name == 'suit':
            return 2 * self.height + 0.3


if __name__ == '__main__':
    coat = Clothes('coat', 40, 1.75)
    print(coat.get_quantity)
    suit = Clothes('suit', 40, 1.75)
    print(suit.get_quantity)
