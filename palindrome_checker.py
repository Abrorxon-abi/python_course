import re
word = input('enter a word that you want to check for palindrome: ')


def remove_symbols(string):
    pattern = r'[\s,!]'
    clean_string = re.sub(pattern, '', string)
    qq = clean_string.lower()
    return qq


clean_word = remove_symbols(word)


def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


if is_palindrome(clean_word):
    print('its a palindrome')
else:
    print('this is not palindrome')
