# Implementing Snake game on SenseHat
# UCT Computer Science CSC4000W RaspPiSe project
# Ross van der Heyde
# 2 July 2018

import sense_hat
import time
import random
import SnakeClass


def up(event):
    """When the joystick is pushed up, change the snake's direction
    of movement to upwards"""
    pass

def down(event):
    """When the joystick is pushed down, change the snake's direction
    of movement to downwards"""
    pass
        
def right(event):
    """When the joystick is pushed right, change the snake's direction
    of movement to the right"""
    pass

def left(event):
    """When the joystick is pushed left, change the snake's direction
    of movement to the left"""
    pass

def stopGame(event):
    """When the middle joystick button is pressed, stop the game"""
    pass

def generateFood():
    """Places the food (target LED) on a random LED in the matrix
    that is not in the snake"""
    return [4,5]

def updateMatrix():
    """Draws the snake and food in the new positions on the LED matrix"""
    pass

def die():
    """When the snake dies by going off the grid or into itself"""
    pass
    

#MAIN
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
        updateMatrix()
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
