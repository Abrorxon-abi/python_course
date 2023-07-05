from functools import reduce

range_1000 = list(range(1000))


def get_all_3_or_5_multiples(i):
    if (i % 3 == 0) or (i % 5 == 0):
        return i


gg = map(get_all_3_or_5_multiples, range_1000)
enumerated_nums = list(gg)
res = [i for i in enumerated_nums if i is not None]


one_res = reduce(lambda x, y: x + y, res)
print(one_res)
