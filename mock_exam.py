# 0 - 100
# 7 guesses

# start 50
# high low correct


def guess_number():
    lower_limit = 1
    upper_limit = 100
    guessed = False
    while not guessed:
        guess = (lower_limit + upper_limit) // 2
        print("is this?", guess)

        response = input("type 'high', 'low' или 'correct': ")
        if response == "high":
            lower_limit = guess + 1
        elif response == "low":
            upper_limit = guess - 1
        elif response == "correct":
            print("Congratulations! you won.")
            guessed = True


print("think one number from 1 to 100, i will guess it")
guess_number()


def count_occurences(string):
    dict = {}
    for i in string:
        dict[i] = string.count(i)
    return dict
# return {letter: string.count(letter) for letter in string}


print(count_occurences('qqwe'))


def remove_duplicates_and_count_letters():
    sentence = input("Enter a sentence: ")
    total = {}

    letters = []

    def del_duplicates(letter):
        if letter not in letters and not letter.isspace():
            return letters.append(letter.lower())

    list(filter(del_duplicates, list(sentence)))

    print(letters)
    for letter in letters:
        total[letter] = sentence.count(letter)

    print(total)


remove_duplicates_and_count_letters()


def numbers(arr):

    arr.sort()
    qq = map(lambda x: abs(x), arr)
    min_plus_num = min(qq)

    arrq = [x for x in arr if x < 0]
    max_minus_num = max(arrq)

    difference = min_plus_num - max_minus_num
    print(arr[difference])


numbers([-1, -2, 10, 44, 11, 6, 5, -6, 7, 8, 9])


def draw():
    board = ''

    for i in range(-1, 6):

        if i % 2 == 0:
            board += '|      ' * 4
            board += '\n|      |      |      |'

        else:
            board += ' _____ ' * 3

        board += '\n'
    print(board)


draw()
