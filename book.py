import timeit

import time

startTime = time.time()  # время начала замера

# здесь пишем код, время которого необходимо измерить


def find_two_biggest(arr):
    return tuple(sorted(arr, reverse=True)[:2])


# print(find_two_biggest([1, 2, 33, 4, 15, 5]))

def largest_two(A):
    my_max, second = A[:2]
    if my_max < second:
        my_max, second = second, my_max
    for idx in range(2, len(A)):

        if my_max < A[idx]:
            my_max, second = A[idx], my_max
        elif second < A[idx]:
            second = A[idx]
    return (my_max, second)


# print(largest_two([1, 2, 43, 5, 6]))


endTime = time.time()  # время конца замера
totalTime = endTime - startTime  # вычисляем затраченное время

print("Время, затраченное на выполнение данного кода = ", totalTime)

print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))


# def largest_two(A):
#     my_max, second = A[:2]
#     if my_max < second:
#         my_max, second = second, my_max
#     for idx in range(2, len(A)):

#         if my_max < A[idx]:
#             my_max, second = A[idx], my_max
#         elif second < A[idx]:
#             second = A[idx]
#     return (my_max, second)


# print(largest_two([1, 2, 43, 5, 6]))

