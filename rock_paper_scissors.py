print('Welcome to rock paper scissors game!')
Player_1 = input('Player_1: ')
Player_2 = input('Player_2: ')

if Player_1 == 'rock' and Player_2 == 'scissors':
    print('Player_1 won!')
elif Player_1 == 'scissors' and Player_2 == 'rock':
    print('Player_2 won!')
elif (Player_1 == 'paper' and Player_2 == 'rock'):
    print('Player_1 won!')
elif (Player_1 == 'rock' and Player_2 == 'paper'):
    print('Player_2 won!')
elif (Player_1 == 'scissors' and Player_2 == 'paper'):
    print('Player_1 won!')
elif (Player_1 == 'paper' and Player_2 == 'scissors'):
    print('Player_2 won!')
elif Player_1 == Player_2:
    print('Its a draw')
else:
    print('choose one of game things')