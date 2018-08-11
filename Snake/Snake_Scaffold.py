# Scaffolding code for Snake game on SenseHat
# 11 August 2018

import sense_hat
import time
import random
import SnakeClass


def up(event):
    """When the joystick is pushed up, change the snake's direction
    of movement to upwards"""
    # Task 2: implement this function
    pass

def down(event):
    """When the joystick is pushed down, change the snake's direction
    of movement to downwards"""
    # Task 2: implement this function
    pass
        
def right(event):
    """When the joystick is pushed right, change the snake's direction
    of movement to the right"""
    # Task 2: implement this function
    pass

def left(event):
    """When the joystick is pushed left, change the snake's direction
    of movement to the left"""
    # Task 2: implement this function
    pass

def stopGame(event):
    """When the middle joystick button is pressed, stop the game"""
    # Task 5: implement this function
    pass

def generateFood():
    """Places the food (target LED) on a random LED in the matrix
    that is not in the snake"""
    # Task 3: rewrite this function
    return [4,5]

def updateMatrix(food, snake):
    """Draws the snake and food in the new positions on the LED matrix"""
    #pass
    # Task 1: display the foodand the snake on the LED matrix

def die():
    """When the snake dies by going off the grid or into itself"""
    # Task 4: implement this function
    pass
    

# MAIN ----------------------------------------------------------------
#set up the senseHat stuff
sense = sense_hat.SenseHat()
sense.low_light = True
sense.stick.direction_down = down
sense.stick.direction_up = up
sense.stick.direction_left = left
sense.stick.direction_right = right
sense.stick.direction_middle = stopGame
blu = [0,0,255]
red = [255,0,0]
gre = [0,255,0]
whi = [255,255,255]
ora = [255,200,0]
yel = [255,255,0]
blk = [0,0,0]

# direction constants
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

playAgain = True

while playAgain:
    snake = SnakeClass.SnakeClass()
    alive = True

    #countdown
    sense.show_letter("3")
    time.sleep(1)
    sense.show_letter("2")
    time.sleep(1)
    sense.show_letter("1")
    time.sleep(1)

    food = generateFood()

    #start game play
    while alive:
        updateMatrix(food, snake)
        result = snake.slither(food)
        if result == "eat":
            print("eat")
            food = generateFood()
        elif result == "die":
            print("die")
            die()

    

sense.clear()
print("end")


























###
