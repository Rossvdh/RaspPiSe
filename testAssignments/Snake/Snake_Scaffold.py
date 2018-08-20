# Scaffolding code for Snake game on SenseHat
# 11 August 2018

import sense_hat
import time
import random
import SnakeClass

# define some colours
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

def updateMatrix(food, snake):
    """Draws the snake and food in the new positions on the LED matrix"""
    sense.clear()
    # Task 1: display the food on the LED matrix
    
    # draw snake
    snakePixels = snake.getPixels()
    for pixel in snakePixels:
        if 0 <= pixel[0] <= 7 and 0 <= pixel[1] <= 7:
            sense.set_pixel(pixel[0], pixel[1], blu)
        else:
            die()
            return

    # blink snake's head
    for i in range(2):
        x = snake.head()[0]
        y = snake.head()[1]
        sense.set_pixel(x, y, blk)
        time.sleep(0.1)
        sense.set_pixel(x, y, blu)
        time.sleep(0.1)
    
def left(event):
    """When the joystick is pushed left, change the snake's direction
    of movement to the left"""
    if event.action == sense_hat.ACTION_RELEASED:
        snake.changeDirection(LEFT)

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

def generateFood():
    """Places the food (target LED) on a random LED in the matrix
    that is not in the snake"""
    # Task 3: rewrite this function
    return [4,5]

def stopGame(event):
    """When the middle joystick button is pressed, stop the game"""
    if event.action == sense_hat.ACTION_RELEASED:
        global playAgain, alive
        playAgain = False
        alive = False

def die():
    """When the snake dies by going off the grid or into itself"""
    global alive
    alive = False
    sense.show_message("You died", text_colour=[255,51,0])
    sense.show_message("Final length: "+ str(snake.getLength()))
    

# MAIN ----------------------------------------------------------------
#set up the senseHat stuff
sense = sense_hat.SenseHat()
sense.low_light = True
sense.stick.direction_down = down
sense.stick.direction_up = up
sense.stick.direction_left = left
sense.stick.direction_right = right
sense.stick.direction_middle = stopGame

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
