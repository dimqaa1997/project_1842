# Задание 1
import time


class TrafficLights:

    def __init__(self):
        self.__colors = ('красный', 'желтый', 'зеленый')

    def running(self):
        start_point = time.time()
        for color in self.__colors:
            if color == 'красный':
                print(color)
                time.sleep(7)

                end_point_red = time.time()
                print(end_point_red - start_point)

            elif color == 'желтый':
                print(color)
                time.sleep(2)
                end_point_yellow = time.time() - start_point - 7
                print(end_point_yellow)

            elif color == 'зеленый':
                print(color)
                time.sleep(10)
                end_point = time.time() - start_point - 9
                print(end_point)


if __name__ == '__main__':
    tr_1 = TrafficLights()
    tr_1.running()
