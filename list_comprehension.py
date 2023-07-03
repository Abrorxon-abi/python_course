a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
gg = [x for x in a if x % 2 == 0]
print(gg)

d = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
ff = [x for x in d if x in b]
print(ff)