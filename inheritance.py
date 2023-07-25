class Employee:
    def __init__(self, name, salary, bonus) -> None:
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def calculate_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.name}, salary={self.salary}, bonus={self.bonus}%, total bonus={self.calculate_total_bonus()} rub"


class Cleaner(Employee):
    def __init__(self, name) -> None:
        super().__init__(name, 15000, 1)


class Manager(Employee):
    def __init__(self, name) -> None:
        super().__init__(name, 45000, 15)


class CEO(Employee):
    def __init__(self, name) -> None:
        super().__init__(name, 105000, 100)

    def calculate_total_bonus(self):
        return 200_000


def calc_bonuses(*employees):
    for employee in employees:
        print(
            f'calc bonus for {employee.name} is = {employee.calculate_total_bonus()}')


if __name__ == '__main__':
    masha = Cleaner('Maria Ivanovna')
    # print(masha)
    # print(dir(masha))
    grisha = Manager('Grigoriy Petrovich')
    # print(grisha)

    ivan_palych = CEO('Ivan Pavlovich')
    # print(ivan_palych)

    print(calc_bonuses(masha, grisha, ivan_palych))
