class Animal:
    def __init__(self, noise) -> None:
        self.noise = noise

    def sound(self):
        print(f"i'm a {self.__class__.__name__}: {self.noise}")


class Cat(Animal):
    def __init__(self, noise) -> None:
        super().__init__(noise)


class Dog(Animal):
    def __init__(self, noise) -> None:
        super().__init__(noise)


class Car:
    def sound(self):
        print('bi-bip')


def noise(animal: Animal):
    animal.sound()
    return ''


cat = Cat('meow')
dog = Dog('gav gav')

if __name__ == '__main__':
    print(noise(cat))
    print(noise(dog))
    print(noise(Car()))


# class Animal:
#     def sound(self):
#         print('grrr')


# class Cat(Animal):
#     def sound(self):
#         print('meow')


# class Dog(Animal):
#     def sound(self):
#         print('gav gav')


# def noise(animal:Animal):
#     animal.sound()
#     return ''


# if __name__ == '__main__':
#     print(noise(Cat()))
