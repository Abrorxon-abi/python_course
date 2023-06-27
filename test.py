# gg = [21, 22, 56, 0]

# def even_num(gg):
#     print(f"all nums are even: {all(gg)}")

# even_num(gg)


# def chr(num):
#     print(chr(num))

# chr(12)

# def print_ascii_chars(num):
#     for i in range(num):
#         if i >= 32 and i <= 126:
#             print(chr(i), end=' ')

# print_ascii_chars(38)


a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)


# ========================================


my_car = {
    'brand': 'BMW',
    'price': 12000
}

print('brand' in my_car)
print('brand' not in my_car)


# ========================================


set1 = {1, 3, 5, 0}
set2 = {1, 3, 5, 0}
print(set1 == set2)
print(set1 is set2)
print(5 in set2)
print(5 not in set2)

