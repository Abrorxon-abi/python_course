# x = ['qwe', 'helo', 'hello world', 'gg', '0rrr']

# def find_longWord(list):
#     longWord = ''
#     for word in list:
#         if len(word) > len(longWord):
#             longWord = word
#     print(longWord)

# find_longWord(x)


# def qwe(*args):
#     return sum(args)

# print(qwe(10, 20))


# nums = [1, 4, 13, 426, 100, 95, -2]

# def find_longNum(list):
#     big = max(list)
#     return big
# print(find_longNum(nums))


# def find_smallNum(list):
#     small = min(list)
#     return small
# print(find_smallNum(nums))

# def qwe(list):
#     big = max(list)
#     small = min(list)
#     sums = big + small
#     if sums % 2 == 0:
#         print('number is even')
#     else:
#         print('number is odd')
#     return sums

# print(qwe(nums))


# data = [1, 4, 6, 12, 31]
# x = [item * 2 for item in data]
# print(x)

# def qwe_count(arr):
#     return [el for el in arr if el[0:2] == el[-2:][::   -1]]

# print(qwe_count(['abc', 'xyz', 'aba', '1212381923128321', 'dogod']))

# names = ['aziz', 'shapka', 'vova', 'oleg']


# def gg(arr):
#     vowels = ['a', 'o', 'e', 'i', 'u']
#     return [i for i in arr if i[0].lower() in vowels]


# print(gg(names))

a = (1, 2, 1, 3, 4, 5, 'g')


# def gg(massive, findIt):
#     if findIt in massive:
#         print(massive.index(findIt))
#     else:
#         print('False')


# gg(a, 'g')

# def gg(tup, item):
#     return tup.count(item)

# print(gg(a, 1))

user_nums = input("Enter numbers: ")


def sorted_nums(gg):
    nums = list(map(int, gg.split(',')))
    even_nums = sorted([num for num in nums if num % 2 == 0], reverse=True)
    odd_nums = sorted([num for num in nums if num % 2 != 0], reverse=True)
    return tuple(even_nums + odd_nums)


print(sorted_nums(user_nums))
