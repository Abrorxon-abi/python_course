import random

lower_letters = 'qwertyuiopasdfghjklzxcvbnm'
upper_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
symbols = '!@#'
numbers = '1234567890'
password_characters = lower_letters + upper_letters + symbols + numbers

level = input('How strong do you want to be your password? ')


def generate_password(i):
    match level:
        case 'easy':
            print(''.join(random.sample(i, 5)))
        case 'medium':
            print(''.join(random.sample(i, 8)))
        case 'difficult':
            print(''.join(random.sample(i, 13)))
        case _:
            print(''.join(random.sample(i, len(i))))


generate_password(password_characters)
