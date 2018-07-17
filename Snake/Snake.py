# Implementing Snake game on SenseHat
# UCT Computer Science CSC4000W RaspPiSe project
# Ross van der Heyde
# 2 July 2018

import sense_hat
from sense_hat import ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time
from signal import pause
import random
import SnakeClass


def up(event):
    if event.action == ACTION_RELEASED:
        snake.changeDirection(UP)

def down(event):
    if event.action == ACTION_RELEASED:
        snake.changeDirection(DOWN)
        
def right(event):
    if event.action == ACTION_RELEASED:
        snake.changeDirection(RIGHT)

def left(event):
    if event.action == ACTION_RELEASED:
        snake.changeDirection(LEFT)

def stopGame():
    """When the middle button is pressed, stop the game"""
    global playAgain, alive
    playAgain = False
    alive = False

def slither():
    """Moves the snake and food's co-ordinates, but does not set the LEDs
    in the matrix."""
    global food, alive
    newSegment = []

    for i in range(len(snake)):
        segment = snake[i]
        #convert to tuple because a list can't be used as a
        #dictionary key
        pixel = tuple(segment[0])

        # check for turning point
        if pixel in turningPoints.keys():
            segment[1] = turningPoints[pixel]
            
            #if all points in the snake have passed, remove the TP
            if i == len(snake)-1:
                #being removed before the newly added segment gets to it
                turningPoints.pop(pixel)

        if i == 0 and pixel == tuple(food):
            # the head eats the food
            # snake grows (new segment to be added)
            newSegment = list(snake[len(snake)-1])
            newSegment[0] = list(newSegment[0])
            snake.append(newSegment)
            
            #move food
            food = generateFood()

        #move the snake
        dire = segment[1]
        if dire == UP:
            segment[0][1] -=1
        elif dire == LEFT:
            segment[0][0] -=1
        elif dire == DOWN:
            segment[0][1] +=1
        else:
            segment[0][0] +=1

        #check if new position is in the snake
        snakePixels = []
        for i in snake:
            snakePixels.append(i[0])

        if snakePixels.count(segment[0]) > 1:
            die()
            return

def generateFood():
    """Places the food (target LED) on a random LED in the matrix
    that is not in the snake"""
    #good scaffold candidate
    temp = [random.randint(0,7), random.randint(0,7)]

    snakePixels = snake.getPixels()

    #check that the food does not fall in the snake
    while temp in snakePixels:
        temp = [random.randint(0,7), random.randint(0,7)]

    return temp

def updateMatrix():
    """Draws the snake and food in the new positions on the LED matrix"""
    #good scaffold candidate
    global alive

    # draw food
    sense.clear()
    sense.set_pixel(food[0], food[1], gre)

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
        time.sleep(0.2)
        sense.set_pixel(x, y, blu)
        time.sleep(0.2)


def die():
    """When the snake dies by going off the grid or into itself"""
    #scaffold candidate
    global alive
    alive = False
    sense.show_message("You died", text_colour=[255,51,0])
    sense.show_message("Final length: "+ str(snake.getLength()))

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
alive = True

while playAgain:
    DIRECTION = DOWN

    snake = SnakeClass.SnakeClass()
    print("snake created!")

    food = generateFood()

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
        updateMatrix()
        result = snake.slither(food, alive)
        if result == "eat":
            print("eat")
            food = generateFood()
        elif result == "die":
            print("die")
            die()

    

sense.clear()
print("end")


























###
