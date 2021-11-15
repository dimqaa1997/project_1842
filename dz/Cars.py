# Задание 4
class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go_car(self):
        print("Машина поехала")

    def stop_car(self):
        print("Машина остановилась")

    def turn_car(self, direction):
        self.direction = direction
        print(f"Машина повернула. Направление :{self.direction}")

    def show_speed(self):
        print(f"speed {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed >= 60:
            print("Внимание!!! Превышение скорости")
        else:
            print(f"скорость :{self.speed}")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super(SportCar, self).__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed >= 40:
            print(f"Внимание!!! Превышение скорости\n"
                  f"Ваша скорость {self.speed}")
        else:
            print(f"скорость :{self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)
        self.speed = speed
        self.color = color
        self.name = name


if __name__ == '__main__':
    police_car = PoliceCar(140, "black", "Nisan")
    police_car.go_car()
    police_car.show_speed()

    work_car = WorkCar(name="Lada", color="Grey", speed=50)
    work_car.show_speed()
    work_car.turn_car("направо")
