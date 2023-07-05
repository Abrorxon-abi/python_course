def get_ten_digits(num):
    return num[:10]


get_ten_digits('37107287533902102798797998220837590246510135740250')


def sum_digits(number):
    print(sum(map(int, number)))


sum_digits(get_ten_digits('37107287533902102798797998220837590246510135740250'))
