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
