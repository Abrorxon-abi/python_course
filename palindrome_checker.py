word = input('enter a word that you want to check for paalindrome: ')

if word[0:] == word[-1::-1]:
    print('its a palindrome')
else:
    print('this is not palindrome')