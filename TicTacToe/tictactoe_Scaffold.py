# Scaffolding code for Tic tac Toe on SenseHat
# Ross van der Heyde VHYROS001
# 16 July 2018

import random, time
import sense_hat
from signal import pause


# colour is the colour to make the square. array of 3 values bewteen 0 and 255
# corresponding to red, green and blue
# row and col are the co-ords of the grid i.e. 0 - 2
def colourSquare(colour, row, col):
    """Fills the given grid square with the given colour"""
    pass


def pushed_up(event):
    """What happens when the joystick is pushed up. The marker moves up
    to the next square"""
    pass

def pushed_down(event):
    """What happens when the joystick is pushed up. The marker moves 
    down to square below the current one"""
    pass

def pushed_left(event):
    """What happens when the joystick is pushed up. The marker moves to
    the square left of the current one"""
    pass

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
    pass

def isWinningRow():
    """Check if a player has won on a row (i.e. there is a row that is 
    all the same colour.) Returns the colour of the row if there is a 
    winning row, else -1"""
    pass

def isWinningCol():
    """Check if a player has won on a column i.e. there is a column that
    is all the same colour.) Returns the colour of the col if there is a 
    winning row, else -1"""
    pass

def isWinningDiag():
    """Check if a player has won on one of the diagonals (i.e. there is 
    a diagonal that is all the same colour). Returns the colour of the 
    diagonal if it is a winning diagonal, else -1"""
    pass
  
def getWinner():
    """Determine which colour has won (if any)"""
    pass

def checkTie():
    """Checks if the game is a tie (no winner). If there is a blank 
    pixel, at least one square of the grid is not coloured yet and it is
     not a tie yet"""
    pass

def checkWinner():
    """Checks if someone has won. Runs after every button action"""
    pass

def playAgain():
    """Restarts the game"""
    pass


# MAIN-----------------------
# set up sense hat
sense = sense_hat.SenseHat()
sense.low_light = True;

#set functions for joystick buttons
sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = buttonPushed

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

# red will play first
redTurn = True

print("about to pause")
pause() #stop execution and wait for event


















#
