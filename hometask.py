from functools import reduce


def average_of_nums(arr):
    qq = arr.replace(" ", "").split(',')
    gg = reduce(lambda x, y: int(x) + int(y), qq)
    average = gg / len(qq)

    closest = qq[0]
    for num in qq:
        if abs(int(num) - int(average)) < abs(int(closest) - int(average)):
            closest = num
    print(closest)


average_of_nums(input('Enter numbers and separate them using "," : '))


def convert_str_to_int(i):

    if str(i).isnumeric() == False:
        return len(i)
    else:
        return int(i)


def list_of_numbers(arr):
    qq = map(convert_str_to_int, arr)
    print(list(qq))


list_of_numbers(["www", "12345", "qwe", 124, '54321', 'aaaaa'])


def remover_odd_nums(arr):
    print(list(filter(lambda x: x % 2 == 0, arr)))


remover_odd_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, -2])


def map_and_filter(arr):
    integer_nums = map(int, arr)
    return filter(lambda x: x % 2 == 0, integer_nums)


print(map_and_filter(['123', '1', '2', '3', '4']))
