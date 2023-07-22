# file = open('111.txt', 'w')

# file.write('hello world\n')
# file.write('hello world\n')
# file.write('hello world\n')
# file.write('hello world')


# file.close()


# file = open(file='111.txt', mode='r')

# print(file.read())
# file.close()

# import requests

# response = requests.get('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4PgrVA_NQmAELBEyIzmNvHLzjkWfYajFM-w&usqp=CAU')
# with open(file='photo.jpg', mode='wb') as photo:
#     photo.write(response.content)

import os
if os.path.exists('111.txt'):
    os.remove('111.txt')


# def file_read(file_name):
#     with open(file_name, 'r') as file:
#         print(file.read())


# file_read('gg.py')

# ----------------------------------------------

# def read_n_lines(file_name, n):
#     with open(file_name, 'r') as file:
#         i = 0
#         for line in file.readlines():
#             print(line)
#             i += 1
#             if i == n:
#                 break


# read_n_lines('users.csv', 33)

# ----------------------------------------------

# def append_text(file_name, text):
#     with open(file_name, 'a') as file:
#         file.write(text)

#     with open(file_name) as file:
#         print(file.read())


# append_text('test.txt', '\nmove bitch get out the way')

# ----------------------------------------------

# from collections import deque


# def read_last_n_lines(file_path, n):
#     with open(file_path, 'r') as file:
#         last_lines = deque(file, n)
#         for line in last_lines:
#             print(line.strip())


# read_last_n_lines('test.txt', 2)

# ----------------------------------------------

# def read_n_lines(file_name):
#     with open(file_name, 'r') as file:
#         listed_lines = []
#         for line in file.readlines():
#             print(line)
#             listed_lines.append(line)
#         print(listed_lines)


# read_n_lines('test.txt')

# ----------------------------------------------

