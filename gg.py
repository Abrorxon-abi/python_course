nums = [1, 3, 2, 5, 10, 100, 101]


def remove_odd_nums(arr):
    z = filter(lambda x: x % 2 != 0, arr)
    print(list(z))


remove_odd_nums(nums)

gg = ['www', 123, 'tutuutut', 124]
