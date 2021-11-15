# Задание 3


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        self.name = name

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        total_income = self._income["wage"] + self._income["bonus"]
        print(f"Должность: {self.position}, доход: {total_income}")


if __name__ == '__main__':
    a = Position(name="Dima", surname="Pane", position="Developer", wage=100000, bonus=35000)
    a.get_full_name()
    a.get_total_income()
