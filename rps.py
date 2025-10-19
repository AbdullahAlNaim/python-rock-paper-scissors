import random

player_input = ''

moves = ['rock', 'paper', 'scissors']
print('player vs ai in rock paper scissors. Begin!!!')

while player_input != 'close':
    print('Choose between r(rock) p(paper) s(scissors): ')
    player_input = input()

    ai_chose = random.choice(moves)
    print(f"player chose: {player_input}")
    print(f"ai chose: {ai_chose}") 

    if player_input == 'r' and ai_chose == 'rock':
        print('ITS A TIE')
    elif player_input == 'r' and ai_chose == 'paper':
        print('AI WINS')
    elif player_input == 'r' and ai_chose == 'scissors':
        print('PLAYER WINS')

    elif player_input == 'p' and ai_chose == 'rock':
        print('PLAYER WINS')
    elif player_input == 'p' and ai_chose == 'paper':
        print('ITS A TIE')
    elif player_input == 'p' and ai_chose == 'scissors':
        print('AI WINS')

    elif player_input == 's' and ai_chose == 'rock':
        print('AI WINS')
    elif player_input == 's' and ai_chose == 'paper':
        print('PLAYER WINS')
    elif player_input == 's' and ai_chose == 'scissors':
        print('ITS A TIE')
    else:
        print('INVALID INPUT. TRY AGAIN!')

    