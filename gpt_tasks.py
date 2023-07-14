# # def reverse_key_and_value(cars):
# #     reversed_items = {value: key for key, value in cars.items()}
# #     print(reversed_items)


# # cars = {
# #     'ferrari': 150,
# #     'maserati': 100,
# #     'lamborghini': 200
# # }

# # reverse_key_and_value(cars)


# # x = {
# #     'a': 1,
# #     'b': '2',
# #     'c': 'hello'
# # }

# # z = {
# #     'd': '4',
# #     'e': 3,
# #     'f': 'world'
# # }

# # a = {
# #     'g': 5,
# #     'h': '!!!',
# #     'i': 6
# # }


import timeit
big_dict = {
    'a': 1,
    'a': 1,
    'a': 1,
    'b': '2',
    'c': 'hello',
    'd': '4',
    'e': 3,
    'f': 'world',
    'g': 5,
    'g': 5,
    'g': 5,
    'g': 5,
    'h': '!!!',
    'i': 6,
    'ferrari': 150,
    'maserati': 100,
    'lamborghini': 200
}


# # def remove_all_beside_string(big_dict: dict) -> dict:
# #     rr = {val for val in big_dict.values() if type(
# #         val) == str and not val.isnumeric()}
# #     print(rr)


# # remove_all_beside_string(big_dict)


# # def test(*arr):
# #     qq = 0
# #     # for dict in arr:
# #     #     for key in dict.values():
# #     #         if str(key).isnumeric():
# #     #             qq += int(key)
# #     qq = sum(int(key) for dict in arr for key in dict.values() if str(key).isnumeric())

# #     print(qq)


# # test(x, z, a)


# dic1 = {
#     'a': 1,
#     'b': '2',
#     'c': 'hello',
#     'p': 'pre'
# }

# dic2 = {
#     'd': '4',
#     'e': 3,
#     'f': 'world',
#     'a': 1,
#     'b': '2',
# }


# def take_duplicates(x, z):
#     # total = {}
#     # for key, val in x.items():
#     #     for key2, val2 in z.items():
#     #         if key == key2 and val == val2:
#     #             total.update({key: val})

#     total = {key: val for key, val in x.items()
#              for key2, val2 in z.items() if key == key2 and val == val2}

#     print(total)


# # take_duplicates(dic1, dic2)


# def take_duplicates(x, z):
#     total = {}
#     # for key, val in x.items():
#     #     if key not in z.keys():
#     #         total.update({key: val})

#     total = {key: val for key, val in x.items() if key not in z.keys()}

#     print(total)


# take_duplicates(dic1, dic2)


# def remove_a(x):
#     qq = {key: val for key, val in x.items() if 'a' not in key}
#     print(qq)
#     # print(x.keys())


# remove_a(big_dict)

# import antigravity
# print(antigravity)


# def sum(a, b, c):
#     s = (a + b) * c /2
#     return s

# print(sum(1, 10, 5))


print(timeit.timeit('sum(range(100000))', number=10000))
print(timeit.timeit('(1 + 100000) * 100000 /2', number=10000))
