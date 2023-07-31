from typing import Any


class Banknote:

    def __init__(self, value: int) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f'Banknote({self.value})'

    def __str__(self) -> str:
        return f'Банкнота c номиналом в {self.value} рублей'

    def __eq__(self, other) -> bool:
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value == other.value

    def __lt__(self, other) -> bool:
        if other is None or not isinstance(other, Banknote):
            raise ValueError()
        return self.value < other.value

    def __le__(self, other) -> bool:
        if other is None or not isinstance(other, Banknote):
            raise ValueError()
        return self.value <= other.value


class Iterator:
    def __init__(self, container) -> None:
        self.container = container
        self.index = 0

    def __next__(self):
        if 0 <= self.index < len(self.container):
            value = self.container[self.index]
            self.index += 1
            return value
        raise StopIteration


class Wallet:
    def __init__(self, *banknotes: Banknote):
        self.container = []
        self.container.extend(banknotes)
        self.index = 0

    def __repr__(self) -> str:
        return f"Wallet({self.container})"

    def __contains__(self, item):
        return item in self.container

    def __bool__(self):
        return bool(self.container)

    def __len__(self):
        return len(self.container)

    def __call__(self) -> Any:
        return f"{sum(e.value for e in self.container)} рублей"

    def __iter__(self):
        return Iterator(self.container)

    def __getitem__(self, item: int):
        return self.container[item]

    def __setitem__(self, key, value):
        if key < 0 or key > len(self.container):
            raise IndexError
        self.container[key] = value


banknote = Banknote(1)
fifty = Banknote(50)
ten = Banknote(10)


if __name__ == '__main__':
    # print(f'{banknote!r}')
    # print(str(banknote))
    # print(repr(banknote))
    # print(ten < fifty)
    # print(ten <= fifty)

    wallet = Wallet(fifty, ten, fifty)
    # print(wallet)
    # print(wallet())
    # for money in wallet:
    #     print(money)

    print(wallet[2])
    wallet[0] = Banknote(500)
    print(wallet)
    print(wallet())
