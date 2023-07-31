class Person:
    def __init__(self, name, surname, age) -> None:
        self.name = name
        self.surname = surname
        self.__age = age

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def describe(self):
        print(
            f"Hello world, My name is {self.name}, and i am {self.__age} years old")


velasco = Person('Velasco', 'qq', 18)

velasco.describe()
velasco.set_age(20)
velasco.describe()
