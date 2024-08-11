import random

def main():
    USER_WINS, COMPUTER_WINS = 0, 0
    OPTIONS = ['rock', 'paper', 'scissors']

    print('WELCOME TO ROCK PAPER SCISSORS GAME')
    print('FIRST TO SCORE 3 WINS!')
    print()

    while True:
        response = input('Click enter to play or Q to Quit - ').lower()
        if response == 'q':
            quit()
        user_pick = input('Pick Rock/Paper/Scissors - ').lower()
        if user_pick not in OPTIONS:
            continue

        random_number = random.randint(0,2)
        # ROCK: 0, PAPER: 1, SCISSORS: 2
        computer_pick = OPTIONS[random_number]
        print(f'Computer picked {computer_pick}.')

        if user_pick == computer_pick:
            print('TIE!')
        elif user_pick == 'paper' and computer_pick == 'rock':
            USER_WINS += 1
            print('YOU WON!')
            if USER_WINS - COMPUTER_WINS == 3:
                print('YOU HAVE WON THE MATCH!')
                break
            elif USER_WINS - COMPUTER_WINS == 0:
                print('TIE')
            elif USER_WINS > COMPUTER_WINS:
                print(f'You are leading by {USER_WINS-COMPUTER_WINS}.')
            else:
                print(f'Computer is leading by {COMPUTER_WINS - USER_WINS}')
        elif user_pick == 'rock' and computer_pick == 'scissors':
            USER_WINS += 1
            print('YOU WON!')
            if USER_WINS - COMPUTER_WINS == 3:
                print('YOU HAVE WON THE MATCH!')
                break
            elif USER_WINS - COMPUTER_WINS == 0:
                print('TIE')
            elif USER_WINS > COMPUTER_WINS:
                print(f'You are leading by {USER_WINS-COMPUTER_WINS}.')
            else:
                print(f'Computer is leading by {COMPUTER_WINS - USER_WINS}')
        elif user_pick == 'scissors' and computer_pick == 'paper':
            USER_WINS += 1
            print('YOU WON!')
            if USER_WINS - COMPUTER_WINS == 3:
                print('YOU HAVE WON THE MATCH!')
                break
            elif USER_WINS - COMPUTER_WINS == 0:
                print('TIE')
            elif USER_WINS > COMPUTER_WINS:
                print(f'You are leading by {USER_WINS-COMPUTER_WINS}.')
            else:
                print(f'Computer is leading by {COMPUTER_WINS - USER_WINS}')
        else:
            COMPUTER_WINS += 1
            print('COMPUTER WINS!')
            if COMPUTER_WINS - USER_WINS == 3:
                print('COMPUTER HAVE WON THE MATCH :(')
                break
            elif COMPUTER_WINS - USER_WINS == 0:
                print('TIE')
            elif COMPUTER_WINS > USER_WINS:
                print(f'Computer is leading by {COMPUTER_WINS-USER_WINS}.')
            else:
                print(f'You are leading by {USER_WINS-COMPUTER_WINS}.')
    print('NICE MATCH! *SHAKES HANDS*')

if __name__ == '__main__':
    main()