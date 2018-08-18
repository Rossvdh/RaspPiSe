# Tic tac Toe on SenseHat
# Ross van der Heyde VHYROS001
# Univeristy of Cape Town Computer Science Honours CSC4000W
# 10 May 2018

import random, time
import sense_hat
import sense_hat
from signal import pause
import ttt


# colour is the colour to make the square. array of 3 values bewteen 0 and 255
# corresponding to red, green and blue
# row and col are the co-ords of the grid i.e. 0 - 2
def colourSquare(colour, col, row):
    row = int(row)#row and col might be floats
    col = int(col)
    sense.set_pixel(col, row, colour)
    sense.set_pixel(col+1, row, colour)
    sense.set_pixel(col, row+1, colour)
    sense.set_pixel(col+1, row+1, colour)


def pushed_up(event):
    """What happens when the joystick is pushed up. The marker moves up
    to the next square"""
    if event.action == sense_hat.ACTION_RELEASED:
        # set previous marker pixel to correct square colour
        sense.set_pixel(marker[0], marker[1], sense.get_pixel(marker[0]+1, marker[1]))
        
        #move marker to next square
        marker[1] = (marker[1] - 3) % 9
        #set marker pixel to blue
        sense.set_pixel(marker[0], marker[1], blue)

def pushed_down(event):
    """What happens when the joystick is pushed up. The marker moves 
    down to square below the current one"""
    if event.action == sense_hat.ACTION_RELEASED:
        sense.set_pixel(marker[0], marker[1], sense.get_pixel(marker[0]+1, marker[1]))
        marker[1] = (marker[1] + 3) % 9
        sense.set_pixel(marker[0], marker[1], blue)

def pushed_left(event):
    """What happens when the joystick is pushed up. The marker moves to
    the square left of the current one"""
    if event.action == sense_hat.ACTION_RELEASED:
        sense.set_pixel(marker[0], marker[1], sense.get_pixel(marker[0]+1, marker[1]))
        marker[0] = (marker[0] - 3) % 9
        sense.set_pixel(marker[0], marker[1], blue)

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
        if sense.get_pixel(marker[0], marker[1]+1) == [0,0,0]:
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
    time.sleep(0.5)
    sense.set_pixels(grid)
    sense.set_pixel(marker[0], marker[1], blue)

# MAIN ---------------------------------------------------------
# set up Sense Hat
sense = ttt.set_up_sense_hat()


#set functions for joystick buttons
sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = buttonPushed
#~ sense.stick.direction_any = checkWinner

#define some colours
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
blank = [0,0,0]
white = [255,255,255]

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

#red will play first
redTurn = True

print("about to pause")
pause() #stop execution and wait for event


















#
