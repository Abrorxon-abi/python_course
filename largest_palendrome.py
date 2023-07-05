def is_palindrome(num):
    return str(num) == str(num)[::-1]

highest_palindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        palendrom_number = i * j
        if is_palindrome(palendrom_number) and palendrom_number > highest_palindrome:
            highest_palindrome = palendrom_number

print(highest_palindrome)