class BlueCat:
    breed = 'Russian Blue'
    names = []
    counter = 0

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.names.append(name)
        BlueCat.breed = 'other'
        self.increment_count()

    def meow(self):
        print(f'{self.name} of {self.breed} says: Meow!')

    @classmethod
    def increment_count(cls):
        cls.counter += 1


if __name__ == '__main__':
    tom = BlueCat('Tom', 3)
    angela = BlueCat('Angela', 1)
    tom.meow()
    angela.meow()
    print(BlueCat.counter)
