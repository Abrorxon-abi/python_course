class Vehicle:
    __color = 'white'

    def __init__(self, name, max_speed, mileage) -> None:
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self) -> str:
        return f'{self.max_speed} km/h is maxsimum speed for {self.mileage} mile and its color is: {self.__color}'

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
    def __init__(self, name,  max_speed, mileage) -> None:
        super().__init__(name, max_speed, mileage)

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

    def __str__(self) -> str:
        return f'Bus no: {self.name}\'s {self.max_speed} km/h is maxsimum speed for {self.mileage} mile'


supra = Vehicle('Supra', 20, 1.5)
bus = Bus('M3', 70, '11')

print(supra)
print(bus)
print(bus.seating_capacity())
