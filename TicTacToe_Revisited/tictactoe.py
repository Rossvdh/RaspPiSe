# Tic tac Toe Revisited: adding a computer player
# Ross van der Heyde VHYROS001
# Univeristy of Cape Town Computer Science Honours CSC4000W
# 1 August 2018

import random, time
import sense_hat
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
import ttt


# colour is the colour to make the square. array of 3 values bewteen 0 and 255
# corresponding to red, green and blue
# row and col are the co-ords of the LED in the top left corner of the ttt
# grid square
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
    if event.action == ACTION_RELEASED:
        # set previous marker pixel to correct square colour
        sense.set_pixel(marker[0], marker[1], sense.get_pixel(marker[0]+1, marker[1]))
        
        #move marker to next square
        marker[1] = (marker[1] - 3) % 9
        #set marker pixel to blue
        sense.set_pixel(marker[0], marker[1], blue)

def pushed_down(event):
    """What happens when the joystick is pushed up. The marker moves 
    down to square below the current one"""
    if event.action == ACTION_RELEASED:
        sense.set_pixel(marker[0], marker[1], sense.get_pixel(marker[0]+1, marker[1]))
        marker[1] = (marker[1] + 3) % 9
        sense.set_pixel(marker[0], marker[1], blue)

def pushed_left(event):
    """What happens when the joystick is pushed up. The marker moves to
    the square left of the current one"""
    if event.action == ACTION_RELEASED:
        sense.set_pixel(marker[0], marker[1], sense.get_pixel(marker[0]+1, marker[1]))
        marker[0] = (marker[0] - 3) % 9
        sense.set_pixel(marker[0], marker[1], blue)

def pushed_right(event):
    """What happens when the joystick is pushed up. The marker moves to
    the square right of the current one"""
    if event.action == ACTION_RELEASED:
        sense.set_pixel(marker[0], marker[1], sense.get_pixel(marker[0]+1, marker[1]))
        marker[0] = (marker[0] + 3) % 9
        sense.set_pixel(marker[0], marker[1], blue)

def buttonPushed(event):
    """What happens when the joystick button is pushed. The square is 
    coloured with the appropriate colour"""
    # update board matrix
    #draw board on LEDs
    global redTurn
    if event.action == ACTION_RELEASED:
        print("redTurn: ",redTurn,"x:", red,"marker[0]:",marker[0], ". marker[1]:",marker[1])

        if sense.get_pixel(marker[0], marker[1]+1) == [0,0,0]:
            if redTurn:
                redTurn = not redTurn
                board[marker[1]//3][marker[0]//3] = red
            else:
                redTurn = not redTurn
                board[marker[1]//3][marker[0]//3] = green

        drawBoard(board)

        result = ttt.checkForWinner(board)
        if result == "red":
            sense.show_message("Red wins")
            playAgain()
        elif result == "green":
            sense.show_message("Green wins")
            playAgain()
        elif result == "tie":
            sense.show_message("Tie")
            playAgain()
        else:
            computerPlay()

def playAgain():
    global board
    """Restarts the game"""
    time.sleep(0.5)
    sense.set_pixels(grid)
    sense.set_pixel(marker[0], marker[1], blue)

    #clear the board
    for row in range(3):
        for col in range(3):
            board[row][col]= blank

"""Draws the board on the LED matrix"""
def drawBoard(board):
    for row in range(3):
        for col in range(3):
            print(board[col][row], "\t", end="")
            colourSquare(board[col][row], row*3, col*3)
        print("")

"""Performs the computer's move"""
def computerPlay():
    print("computer moves")

# MAIN-------------------------------------------------
# set up sense hat
sense = sense_hat.SenseHat()
sense.low_light = True
#sense.set_rotation(180)

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

# define the Tic Tac Toe grid
grid=[blank,blank,white,blank,blank,white,blank,blank,
  blank,blank,white,blank,blank,white,blank,blank,
  white,white,white,white,white,white,white,white,
  blank,blank,white,blank,blank,white,blank,blank,
  blank,blank,white,blank,blank,white,blank,blank,
  white,white,white,white,white,white,white,white,
  blank,blank,white,blank,blank,white,blank,blank,
  blank,blank,white,blank,blank,white,blank,blank]

# matrix representing the TTT grid
board = [[blank, blank, blank],
         [blank, blank, blank],
         [blank, blank, blank]]

#sense.show_message("Get ready!")
# set grid
sense.set_pixels(grid)


# set position marker to top left corner
marker=[0,0]
sense.set_pixel(marker[0], marker[1], blue)

#red plays first
redTurn = True

print("about to pause")
pause() #stop execution and wait for event


















#
