num = 13
while num != 1:
    print(num)
    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1

print(num)
