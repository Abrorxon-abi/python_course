my_dict = {
    'BMW': 10,
    'Audi': 20,
    'Ferrari': 50,
    'Lamborghini': 40,
    'Mercedes': 30,
    'Maserati': 25,
}


def sort_it_ascending(x):
    qq = sorted(x.items(), key=lambda x: x[1])
    dicted = dict(qq)
    print(dicted)
    return dicted


def sort_it_ascending(x):
    qq = sorted(x.items())
    dicted = dict(qq)
    print(dicted)
    return dicted


sort_it_ascending(my_dict)


def sort_it_descending(x):
    qq = sorted(x.items(), key=lambda x: x[1], reverse=True)
    dicted = dict(qq)
    print(dicted)
    return dicted


sort_it_descending(my_dict)

"""
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
"""

Sample_Dictionary = {0: 10, 1: 20}


def disct_updater(x):
    key_of_dict = 1
    key_of_dict += 1
    Sample_Dictionary.update({key_of_dict: x})
    print(Sample_Dictionary)


disct_updater(30)


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}


def concate_dicts(*x):
    gg = {}
    for d in x:
        gg.update(d)
    print(gg)


concate_dicts(dic1, dic2, dic3)


def checker_key_in_dict(x, y):
    print('found') if x.get(y) else print('not found')


checker_key_in_dict(my_dict, 'Ferrari')


num = int(input("Input a number "))
d = dict()

for x in range(num+1):
    d[x] = x*x

print(d)


def sum_dicts(*dictionary):
    for x in dictionary:
        print(sum(x.values()))


sum_dicts(dic1, dic2, dic3)


def sum_dicts(*dictionary):
    gg = {}
    res = 1
    for x in dictionary:
        gg.update(x)

    for key in gg:
        res *= gg[key]
    print(res)


sum_dicts(dic1, dic2, dic3)


def delete_key(x, y):
    if y in x:
        del x[y]
    print(x)


delete_key(dic1, 1)


list1 = [1, 2, 3, 4, 5]
list2 = ['qwe', 'asd', 'zxc', 'rr', 'pp']


def map_lists_to_dict(keys, values):

    dictionary = {}
    for i in range(len(keys)):
        dictionary.setdefault(keys[i], values[i])

    return dictionary


keys = ['data1', 'data2', 'data3']
values = [100, -54, 247]

result = map_lists_to_dict(keys, values)
print(result)


def get_max_and_min(x):
    print(max(x.values()))
    print(min(x.values()))


get_max_and_min(my_dict)
