# Задание 5
class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки для {self.title}")


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки для {self.title}")


class Marker(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки для {self.title}")


if __name__ == '__main__':
    m = Marker("маркер")
    m.draw()

    pen = Pen("ручка")
    pen.draw()
