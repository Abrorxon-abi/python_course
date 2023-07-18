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


def find_max_and_min_key_by_value(dict):
    print(max(dict, key=dict.get), min(dict, key=dict.get))


find_max_and_min_key_by_value(
    {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20})


def sort_values(dict):
    qq = {val for val in dict.values()}
    print(sorted(qq))


sort_values(
    {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20})


def sort_keys(dict):
    qq = {key for key in dict.keys()}
    print(sorted(qq, reverse=True))


sort_keys(
    {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20})


def transform_dict_into_tuple(dict):
    qq = {key for key in dict.keys()}
    dd = {val for val in dict.values()}
    print(tuple(zip(qq, dd)))


transform_dict_into_tuple(
    {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4})


def converter_two_lists_into_dict(keys, vals):
    print(dict(zip(keys, vals)))


converter_two_lists_into_dict(['a', 'b', 'c', 'd', 'e', 'f'], [1, 2, 3, 4, 5])


def find_key_by_value(dict, val):
    qq = {key for key, value in dict.items() if val == value}
    print(qq)


find_key_by_value({'Theodore': 19, 'Roxanne': 20,
                  'Mathew': 21, 'Betty': 20}, 20)


def get_vals(arr, key):
    qq = [x.get(key) for x in arr]
    print(qq)


get_vals([{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {
   'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}], 'age')


def unique_keys(arr):
    print(dict(zip(list(range(1, len(arr) + 1)), arr)))


unique_keys(['theodore', 'mathew', 'roxanne', 'qwe'])
