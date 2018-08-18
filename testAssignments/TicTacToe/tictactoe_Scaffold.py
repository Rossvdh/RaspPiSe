# Scaffolding code for Tic tac Toe on SenseHat

import random, time
import sense_hat
from signal import pause
import ttt


# colour is the colour to make the square. array of 3 values bewteen 0 and 255
# corresponding to red, green and blue
# row and col are the co-ords of the marker
def colourSquare(colour, col, row):
    """Fills the given grid square with the given colour"""
    #Task 2: complete this method
    print("colour square")


def pushed_up(event):
    """What happens when the joystick is pushed up. The marker moves up
    to the next square"""
    #Task 1: complete this method
    print("up")

def pushed_down(event):
    """What happens when the joystick is pushed up. The marker moves 
    down to square below the current one"""
    #Task 1: complete this method
    print("down")

def pushed_left(event):
    """What happens when the joystick is pushed up. The marker moves to
    the square left of the current one"""
    #Task 1: complete this method
    print("left")

def pushed_right(event):
    """What happens when the joystick is pushed up. The marker moves to
    the square right of the current one"""
    if event.action == sense_hat.ACTION_RELEASED:
        sense.set_pixel(marker[0], marker[1], sense.get_pixel(marker[0]+1, marker[1]))
        marker[0] = (marker[0] + 3) % 9
        sense.set_pixel(marker[0], marker[1], blue)

def buttonPushed(event):
    """What happens when the joystick button is pushed. The square is 
    coloured with the appropriate colour"""
    global redTurn
    if event.action == sense_hat.ACTION_RELEASED:
        if sense.get_pixel(marker[0], marker[1]+1) == blank:
            if redTurn:
                redTurn = not redTurn
                colourSquare(red, marker[0], marker[1])
            else:
                redTurn = not redTurn
                colourSquare(green, marker[0], marker[1])
        
        if ttt.checkForResult():
            playAgain()


def playAgain():
    """Restarts the game"""
    # Task 3: complete this function
    pass


# MAIN-----------------------
# set up sense hat
sense = sense_hat.SenseHat()
sense.low_light = True

#set functions for joystick buttons
sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = buttonPushed

#define some colours
white = [255,255,255]
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
blank = [0,0,0]


sense.show_message("Get ready!")

# define the Tic Tac Toe grid
grid=[blank,blank,white,blank,blank,white,blank,blank,
  blank,blank,white,blank,blank,white,blank,blank,
  white,white,white,white,white,white,white,white,
  blank,blank,white,blank,blank,white,blank,blank,
  blank,blank,white,blank,blank,white,blank,blank,
  white,white,white,white,white,white,white,white,
  blank,blank,white,blank,blank,white,blank,blank,
  blank,blank,white,blank,blank,white,blank,blank]

# set grid
sense.set_pixels(grid)

# set position marker to top left corner
marker=[0,0]
sense.set_pixel(marker[0], marker[1], blue)

# red will play first
redTurn = True

print("about to pause")
pause() #stop execution and wait for event


















#
