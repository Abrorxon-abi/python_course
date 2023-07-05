def sum_and_compare(args):
    gg = sum(args)
    print(gg)
    max_val = max(args)
    difference = gg - max_val
    print(difference)
    if difference % 2 == 0:
        print('even')
    else:
        print('odd')


sum_and_compare([1, 2, 3, 4, 5])


def longest_word(arr):
    words_in_nums = map(len, arr)
    qq = list(words_in_nums)
    print(max(qq))


longest_word(['qqwe', 'vovka', 'tqweqwewqeqwewq',
             'askdhlfgasdhilgtfkuyqwg', 'eee'])


def longest_word(arr):
    words_in_nums = map(len, arr)
    qq = list(words_in_nums)
    print(qq)


longest_word(['qqwe', 'vovka', 'tqweqwewqeqwewq',
             'askdhlfgasdhilgtfkuyqwg', 'eee'])

capital_words = 'QWERTYUIOPASDFGHJKLZXCVBNM'


def capitalized_words(*arr):
    qwe = []
    rr = [*capital_words]

    for i in arr:
        if i[0] in rr:
            qwe.append(i)

    print(qwe)


capitalized_words('Qwe', 'Monday', 'qq', 'op', 'YelloAnt')

def longest_word(arr):
    gg = arr.split(',')

    rr = filter(lambda x: len(x) > 4, gg)

    print(list(rr))


longest_word(input('enter words separate them with "," : '))


from functools import reduce


def qwe(arr):
    num = arr.split()

    qq = map(lambda x: int(x) ** 2, num)    
    ww = reduce(lambda x, y: x + y, qq, 0)
    print(ww)


qwe(input('enter a number: '))
