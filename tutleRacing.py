import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'black','yellow', 'purple', 'pink', 'brown', 'cyan']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('How many turtles do you want to race (2-10)... ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not numeric... Try Again!')
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print('NUMBER OF RACERS NOT IN RANGE (2-10). TRY AGAIN!')

def race(colors):
    turtles = build_racers(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            x, y = racer.pos()
            if y >= HEIGHT//2-10:
                return colors[turtles.index(racer)].upper()

def build_racers(colors):
    turtles = []
    spacing_x = WIDTH//(len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * spacing_x,-HEIGHT//2 + 20)
        turtles.append(racer)
    return turtles

def setup_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('TURTLE RACING')

def main():
    racers = get_number_of_racers()
    setup_screen()
    random.shuffle(COLORS)
    colors = COLORS[:racers]

    winner = race(colors)
    print(f'Winner is turtle with color {winner}')
    time.sleep(5)

if __name__ == '__main__':
    main()