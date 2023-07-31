from abc import abstractmethod, ABC


class Books(ABC):
    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def test(self):
        print('hello')
        
    @property
    def name(self):
        return self.__name


class EBooks(Books):
    def __init__(self, name, link):
        super().__init__(name)
        self.link = link

    def test(self):
        print("Hello world from child")
        return ""


class PaperBooks(Books):
    def __init__(self, name, paper):
        super().__init__(name)
        self.paper = paper

    def test(self):
        return ""

child = EBooks("Cook book", 'https://buybooks.com')
child_2 = PaperBooks("python", 'wooden paper')
print(child.test())
print(child.link)
print(child_2.test())
print(child_2.paper)      