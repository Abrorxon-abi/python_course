from functools import reduce

one_hundred_numbers = range(1, 101)

sum_of_squares = reduce(lambda x, y: x + y * y, one_hundred_numbers, 0)
print(sum_of_squares)


sum_of_100_natural_nums = sum(range(1, 101))


def do_square(num):
    return num ** 2


print(do_square(sum_of_100_natural_nums))


square_of_sum = do_square(sum_of_100_natural_nums)

print(square_of_sum - sum_of_squares)
