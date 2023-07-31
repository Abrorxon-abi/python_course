
class Cat:

    __slots__ = ('_name', '_age')

    def __init__(self, name, age) -> None:

        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise AttributeError('name cannot be empty!')
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 1 or value > 15:
            raise AttributeError('age should be between 1-15')
        self._age = value

    def __repr__(self) -> str:
        return f'Cat: {self.name}, age: {self.age}'


tom = Cat("Tom", 2)

if __name__ == '__main__':
    tom.name1 = 'qwe'
    tom.age = 6
    print(tom)
