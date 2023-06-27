# def find_numbers():

#     nums = 0

#     for num in range(100):
#         if num % 3 == 0 or num % 5 == 0:
#             nums += num

#     print(nums)


# find_numbers()


# def find_prime():

#     nums = 0

#     for num in range(2, 100):
#         if num / num == 1 and num % 1 == num:
#             nums += 1

#     print(nums)


# find_prime()

# fruits = ['apple', 'disgusting lemon', 'orange']

# for fruit in fruits:
#     if 'disgusting' in fruit:
#          continue
#     else:
#         print(fruit)


import random

letters = 'qwertyuiopasdfghjklzxcvbnm'
nums = '1234567890'
symbols = '@#$%*'

total_symbols_for_password = int(input('enter password length: '))
everething_included = letters + nums + symbols

password = ''

for i in range(total_symbols_for_password):
    random_int = random.randint(0, len(everething_included)-1)
    password += everething_included[random_int]

print(password)
