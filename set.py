def cube():
    n = 1
    while True:
        yield n**3
        n += 1


qq = cube()
print(qq.__next__())
print(qq.__next__())
print(next(qq))
print(next(qq))
print(qq.__next__())
