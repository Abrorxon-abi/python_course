from uuid import uuid4

class Tumbochka:
    tmb_count = 0
    
    def __init__(self) -> None:
        self.tumb_id = uuid4()
        Tumbochka.tmb_count += 1

    def open_door(self):
        print(f'opened door in tumb with id: {self.tumb_id}')

    @staticmethod
    def cut_with_qaychi(smth):
        print(f'{smth} was cutted successfully')

    @classmethod
    def show_tmb_count(cls):
        print(f'{cls.tmb_count}')
        

class Tumbochka2(Tumbochka):
    tmb_count = 10

    
print(Tumbochka2.show_tmb_count())

tumbochka = Tumbochka()
tumbochka.open_door()
tumbochka.cut_with_qaychi('paper')
tumbochka.show_tmb_count()