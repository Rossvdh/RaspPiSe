# Scaffolding code for Snake game on SenseHat
# 11 August 2018

# REVISED ASSIGNMENT

import sense_hat
import time
import random
import SnakeClass

#define some colours
blue = [0,0,255]
red = [255,0,0]
green = [0,255,0]
blank = [0,0,0]

# direction constants
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

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
    if event.action == sense_hat.ACTION_RELEASED:
        snake.changeDirection(LEFT)

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
    sense.clear()
    # draw snake
    snakePixels = snake.getPixels()

    # Task 1: Add some code here to display the food on the LED matrix
    # food is a list with 2 elements: the first is the x co-ordinate (column)
    # on the LED matrix and the second is the y co-ordinate (row)
    sense.set_pixel(food[0], food[1], green)

    # Task 1: display the snake body on the LED matrix.
    # the list snakePixels contains the pixels that make up the snake
    # body. each pixel is a 2-tuple (x, y).
    # snakePixels lsit structure: [(x, y), (x, y), ...]

    # blink snake's head
    x = snake.head()[0]
    y = snake.head()[1]
    for i in range(2):        
        sense.set_pixel(x, y, blank)
        time.sleep(0.1)
        sense.set_pixel(x, y, blue)
        time.sleep(0.1)
        

def die():
    """When the snake dies by going off the grid or into itself"""
    global alive
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

playAgain = True #we want to play again after dying

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
    while alive: #while snake is alive, keep moving and updating the matrix
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
