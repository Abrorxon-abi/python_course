def concatenate_dict(*args):
    main_dict = {}
    for dict in args:
        main_dict |= dict
    print(main_dict)


concatenate_dict({'qwe': 'qwe'}, {'asd': 'asd'}, {'qq': 'qq'})


x = {
    'qwe': 'yyyy',
    'gg': 'zzzz',
    'rrrr': 'ppppp'
}


z = {
    'yyyy': 'qwe',
    'zzzz': 'gg',
    'ppppp': 'rrrr'
}


def get_key(dict, key):
    print('found') if dict.get(key) else print('not found')


get_key(z, 'yy')


def generate_dict(n):
    print({i: i**2 for i in range(n+1)})


generate_dict(15)
