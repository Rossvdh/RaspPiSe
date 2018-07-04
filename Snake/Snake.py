# Implementing Snake game on SenseHat
# UCT Computer Science CSC4000W RaspPiSe project
# Ross van der Heyde
# 2 July 2018

import sense_hat
from sense_hat import ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time
from signal import pause
import random

#SORT OUT THESE NAMES!
def down(event):
    global DIRECTION, turningPoints, snake
    if event.action == ACTION_RELEASED:
        if DIRECTION != DOWN: # don't let the snake go back on itself
            DIRECTION = UP
            #convert to tuple because a list can't be used as a
            #dictionary key
            turningPoints[tuple(snake[0][0])] = UP

def up(event):
    global DIRECTION, turningPoints, snake
    if event.action == ACTION_RELEASED:
        if DIRECTION != UP:
            DIRECTION = DOWN
            turningPoints[tuple(snake[0][0])] = DOWN
        
def left(event):
    global DIRECTION, turningPoints, snake
    if event.action == ACTION_RELEASED:
        if DIRECTION != LEFT:
            DIRECTION = RIGHT
            turningPoints[tuple(snake[0][0])] = RIGHT

def right(event):
    global DIRECTION, turningPoints, snake
    if event.action == ACTION_RELEASED:
        if DIRECTION != RIGHT:
            DIRECTION = LEFT
            turningPoints[tuple(snake[0][0])] = LEFT

def stopGame():
    """When the middle button is pressed, stop the game"""
    global playAgain, alive
    playAgain = False
    alive = False

def slither():
    """Moves the snake and food's co-ordinates, but does not set the LEDs
    in the matrix."""
    global food, alive
    grow = []
    eat = False
    for i in range(len(snake)):
        segment = snake[i]
        #convert to tuple because a list can't be used as a
        #dictionary key
        pixel = tuple(segment[0])

        if pixel in turningPoints.keys():
            segment[1] = turningPoints[pixel]
            
            #if all points in the snake have passed, remove the TP
            if i == len(snake)-1:
                #being removed before the newly added segment gets to it
                turningPoints.pop(pixel)

        if i == 0 and pixel == tuple(food):
            # the head eats the food
            print("eat")

            #snake grows (new segment to be added)
            grow = list(snake[len(snake)-1])
            grow[0] = list(grow[0])
            snake.append(grow)
            
            #move food
            food = generateFood()

        #move
        dire = segment[1]
        if dire == UP:
            segment[0][1] -=1
        elif dire == LEFT:
            segment[0][0] -=1
        elif dire == DOWN:
            segment[0][1] +=1
        else:
            segment[0][0] +=1

        #check if new position is not in the snake
        snakePixels = []
        for i in snake:
            snakePixels.append(i[0])

        if snakePixels.count(segment[0]) > 1:
            die()
            return
        

def generateFood():
    """Place sthe food (target LED) on a random LED in the matrix
    that is not in the snake"""
    temp = [random.randint(0,7), random.randint(0,7)]

    snakePixels = []
    for i in snake:
        snakePixels.append(i[0])

    #check that the food does not fall in the snake
    while temp in snakePixels:
        temp = [random.randint(0,7), random.randint(0,7)]

    return temp

def play():
    global alive
    # draw snake
    sense.clear()
    sense.set_pixel(food[0], food[1], gre)
    
    for dot in snake:
        if 0 <= dot[0][0] <= 7 and 0 <= dot[0][1] <= 7:
            sense.set_pixel(dot[0][0], dot[0][1], blu)
        else:
            die()
            return

    if alive:
        # blink snake's head
        for i in range(2):
            x = snake[0][0][0]
            y = snake[0][0][1]
            sense.set_pixel(x, y, blk)
            time.sleep(0.2)
            sense.set_pixel(x, y, blu)
            time.sleep(0.2)

        slither()

def die():
    """When the snake dies by going off the grid or into itself"""
    global alive
    alive = False
    sense.show_message("You died", text_colour=[255,51,0])
    sense.show_message("Final length: "+ str(len(snake)))

#MAIN
sense = sense_hat.SenseHat()

sense.low_light = True
sense.set_rotation(180)

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

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

playAgain = True
alive = True

while playAgain:
    DIRECTION = DOWN

    # dictionary of points where the snake turns. a turning point
    # consists of a 2-tuple (x,y) as the key and the direction to which
    # the snake turns as the value, e.g. {(3, 5): 1} (where 1 is RIGHT)
    turningPoints = {}

    # the snake is a list of pixels, where a pixel is a 2-tuple where
    # the first entry is a list with the co-ords, and the second is the
    # direction that the pixel is moving in.
    snake = [[[4,1], DOWN], [[4,0], DOWN]]

    #we are reaching the point where Snake probably needs to be a class
    #or maybe just pixel, and then snake is a list of pixels

    ##food = generateFood()

    food = [4,3]
    ##sense.set_pixel(food[0], food[1], gre)

    alive = True

    #countdown
    sense.show_letter("3")
    time.sleep(1)
    sense.show_letter("2")
    time.sleep(1)
    sense.show_letter("1")
    time.sleep(1)

    #start game play
    while alive:
        play()


sense.clear()
print("end")


























###
