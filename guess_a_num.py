import random

random_num = random.randint(1, 9)

attempts = 0
guessed_num = 0
print('Random number was generated')

while random_num != guessed_num:
    guessed_num = int(input('Guess it: '))

    if random_num > guessed_num:
        attempts += 1
        print('its too low')
    elif random_num < guessed_num:
        attempts += 1
        print('its too high')
    else:
        attempts += 1
        print(f"Congratulations you won in {attempts} attempts")
