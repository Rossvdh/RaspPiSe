# Scaffolding code for Tic tac Toe Revisited: adding a computer player
# Ross van der Heyde VHYROS001
# Univeristy of Cape Town Computer Science Honours CSC4000W
# 10 August 2018

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
    """Fills the grid square at the co-ords with the given colour"""
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
    global redTurn
    if event.action == ACTION_RELEASED:
        #print("redTurn: ",redTurn,"x:", red,"marker[0]:",marker[0], ". marker[1]:",marker[1])

        if sense.get_pixel(marker[0], marker[1]+1) == [0,0,0]:
            if redTurn:
                board[marker[1]//3][marker[0]//3] = red
            else:
                board[marker[1]//3][marker[0]//3] = green
                
            redTurn = not redTurn
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
                #no result, so its the computer's turn
                computerPlay()

def shuffle(lst):
    """Shuffles the array of moves and their scores"""
    for i in range(len(lst)-1, 0, -1):
        rand = random.randint(0, i)
        lst[i], lst[rand] = lst[rand], lst[i]
    return lst

def playAgain():
    """Restarts the game"""
    global board, redTurn
    time.sleep(0.5)
    redTurn = True
    sense.set_pixels(grid)
    sense.set_pixel(marker[0], marker[1], blue)

    board = [[red, blank, blank],
    [blank, green, blank],
    [blank, blank, blank]]

    drawBoard(board)


def drawBoard(board):
    """Draws the board on the LED matrix"""
    #Task 1: complete this function
    pass

def copyBoard(board):
    """Creates a copy of the given board"""
    pass

def getAvailableMoves(board):
    """"Returns a list [(row, col), ...] of blank grid sqaures"""
    #Task 3: complete this function


def getBestMove(board, colour):
    """Returns the best move ((row, col), score) for the given colour on the given board"""
    #random move
    row = random.randint(0, 2)
    col = random.randint(0, 2)

    return (row, col)

    #Task 3: remove the above code, call getAvailableMoves and choose one

    #Task 4: rewrite this function
    
          

"""Performs the computer's move"""
def computerPlay():
    global redTurn

    colour = red if redTurn else green
    
    move = getBestMove(board, colour)

    #Task 2: complete this function
    

# MAIN-------------------------------------------------
if __name__ == "__main__": #remove?
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

    #define some colours
    red = [255,0,0]
    green = [0,255,0]
    blue = [0,0,255]
    blank = [0,0,0]
    white = [255,255,255]

    # define the empty Tic Tac Toe grid
    grid=[blank,blank,white,blank,blank,white,blank,blank,
      blank,blank,white,blank,blank,white,blank,blank,
      white,white,white,white,white,white,white,white,
      blank,blank,white,blank,blank,white,blank,blank,
      blank,blank,white,blank,blank,white,blank,blank,
      white,white,white,white,white,white,white,white,
      blank,blank,white,blank,blank,white,blank,blank,
      blank,blank,white,blank,blank,white,blank,blank]

    # matrix representing the TTT grid
    board = [[red, blank, blank],
       [blank, green, blank],
       [blank, blank, blank]]


    #sense.show_message("Get ready!")
    # set grid
    sense.set_pixels(grid)
    drawBoard(board)

    # set position marker to top left corner
    marker=[0,0]
    sense.set_pixel(marker[0], marker[1], blue)

    #red (user) plays first
    redTurn = True

    print("about to pause")
    pause() #stop execution and wait for event


















#
