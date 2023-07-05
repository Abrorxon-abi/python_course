from functools import reduce

numbers = [1, 2, 33, 5, 10, 9, 11]

    
def get_max_num(acc, next):
    if acc > next:
        return acc
    else:
        return next


result = reduce(get_max_num, numbers)
print(result)


print('♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥')
print(chr(3))

print(globals())

print(hash('qq'))
print(id('qq'))
