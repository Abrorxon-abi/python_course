def smallest_divisible_number():
    number = 1
    while True:
        divisible = True
        for i in range(1, 21):
            if number % i != 0:
                divisible = False
                break
        if divisible:
            return number
        number += 1


smallest_number = smallest_divisible_number()
print(smallest_number)
