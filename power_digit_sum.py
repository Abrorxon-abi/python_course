num = 2 ** 1000

stringed_num = str(num)


def sum_all_digits(n):
    return sum(map(int, n))


print(sum_all_digits(stringed_num))
