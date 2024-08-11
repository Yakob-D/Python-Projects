import random
import time
import threading


def generate_problem(max, min, operators):
    left = random.randint(min,max)
    right = random.randint(min,max)
    operator = random.choice(operators)
    problem = str(left) + ' ' + operator + ' ' + str(right)
    return problem, left, right, operator

def ask(problem):
    print('Here is your problem')
    answer = input(f'{problem} = ')
    return answer

def check(left, right, operator, answer):
    def calculate(left,right,operator):
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            return left // right
        elif operator == '**':
            return left ** right
    try:
        correct_answer = calculate(left,right,operator)
        if operator == '/':
            correct_answer = round(correct_answer)
        return correct_answer == int(answer)
    except (ValueError):
        return False
    
def play(TIME_LIMIT,max,min,operators):
    global time_up
    time_up = False

    timer_thread = threading.Thread(target=countdown, args=(TIME_LIMIT,))
    timer_thread.start()

    score = 0

    start_time = time.time()
    end_time = start_time + TIME_LIMIT

    while not time_up:
        remaining_time = int(end_time - time.time())
        print()
        print(f'{remaining_time} seconds left' + '\n')
        problem,left,right,operator = generate_problem(max,min,operators)
        answer = ask(problem)
        if check(left,right,operator,answer):
            score += 1
        if time_up:
            break
            
    timer_thread.join()
    print(f'You scored {score}')

def countdown(t):
    global time_up
    while t:
        time.sleep(1)
        t-=1
    time_up = True
    print('\n' + 'TIME IS UP! Press enter to see your score..',end = ' ')

def main():
    print('WELCOME TO MY MATH QUIZ', '\n')
    print('Here is how the game work..')
    print('When you start the game you will be given 30 seconds and during that time you will be asked multiple math questions, the goal is to answer as many questions as possible. YOUR ANSWERS SHOULD BE WHOLE NUMBERS(ROUND YOUR ANSWERS TO THE NEAREST WHOLE NUMBER WHEN NEEDED)')
    print('When the time limit is up your score will be displayed')
    print('Operators, * -- denotes multiplication, ** -- denotes exponential(raised to), / -- denotes division, + -- denotes addition, - -- denotes subtraction')
    print()
    while True:
        mode = input('Pick a mode EASY/AMATURE/HARD... ').lower()
        if mode == 'easy':
            time_limit = 30
            max = 10
            min = 1
            operators = ['+','-']
            break
        elif mode == 'amature':
            time_limit = 30
            max = 15
            min = 5
            operators = ['+','-','*']
            break
        elif mode == 'hard':
            time_limit = 15
            max = 35
            min = 15
            operators = ['+','-','*','/','**']
            break
        else:
            print('INVALID MODE')
    input('\n' + 'Press Enter to start playing... ')
    play(time_limit, max, min, operators)
    choice = input('Do you want to play again? (yes/no)').lower()
    if choice == 'yes':
        play(time_limit, max, min, operators)
    elif choice == 'no':
        quit()
    else:
        print('INVALID CHOICE!')

if __name__ == '__main__':
    main()