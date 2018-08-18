# Module with some functions for tic-tac-toe introdution
# Ross van der Heyde VHYROS001
# University of Cape Town Computer Science Honours
# 11 August 2018

import sense_hat
import time

#define some colours
white = [255,255,255]
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
blank = [0,0,0]

sense = sense_hat.SenseHat()

def isWinningRow():
    """Check if a player has won on a row (i.e. there is a row that is 
    all the same colour.) Returns the colour of the row if there is a 
    winning row, else -1"""
    for i in [1,4,7]:
        if sense.get_pixel(1,i) == sense.get_pixel(4,i) == sense.get_pixel(7,i):
            #avoid returning blank wins if the "winning row" is a 
            #row of blank squares
            if sense.get_pixel(1,i) != blank:
                return sense.get_pixel(1, i)
    return -1

def isWinningCol():
    """Check if a player has won on a column i.e. there is a column that
    is all the same colour.) Returns the colour of the col if there is a 
    winning row, else -1"""
    for i in [1,4,7]:
        if sense.get_pixel(i,1) == sense.get_pixel(i,4) == sense.get_pixel(i,7):
            #avoid returning blank wins if the "winning column" is a 
            #column of blank squares
            if sense.get_pixel(i,1) != blank:
                return sense.get_pixel(i,1)
    return -1

def isWinningDiag():
    """Check if a player has won on one of the diagonals (i.e. there is 
    a diagonal that is all the same colour). Returns the colour of the 
    diagonal if it is a winning diagonal, else -1"""
    #check the top left to bottom right diagonal
    if sense.get_pixel(1,1) == sense.get_pixel(4,4) == sense.get_pixel(7,7):
        if sense.get_pixel(1,1) != blank:
            return sense.get_pixel(1,1)
            
    #check the top right to bottom left diagonal
    if sense.get_pixel(6,1) == sense.get_pixel(3,4) == sense.get_pixel(0,7):
        if sense.get_pixel(6,1) != blank:
            return sense.get_pixel(6,1)
    
    return -1
  
def getWinner():
    """Determine which colour has won (if any)"""
    """Determine which colour has won (if any)"""
    #check for a winning row
    pixel = isWinningRow()
    if pixel != -1:
        #there is a winning row
        if pixel == [0,252,0]: #sometimes the colours read from the LEDs
                                                #do not exactly match what they were set to.
                                                #more details in the API.
            return "green"
        elif pixel == [248, 0, 0]:
            return "red"

    #check for winning column
    pixel = isWinningCol()
    if pixel != -1:
        if pixel == [0,252,0]:
            return "green"
        elif pixel == [248, 0, 0]:
            return "red"

    #check for winning diagonal  
    pixel = isWinningDiag()
    if pixel != -1:
        #there is a winning diag
        if pixel == [0,252,0]:
            return "green"
        elif pixel == [248, 0, 0]:
            return "red"

    #no winner
    return "none"

def checkTie():
    """Checks if the game is a tie (no winner). If there is a blank 
    pixel, at least one square of the grid is not coloured yet and it is
     not a tie yet"""
    # it is only necessary to check one pixel in each grid square
    for i in [1, 4, 7]:
        for j in [1, 4, 7]:
            if sense.get_pixel(i,j) == blank:
                return False
              
    #all relevant pixels have been checked, no blanks found
    return True

def checkForResult():
    """Checks if someone has won. Runs after every button action"""
    print("checkWinner")
    winner = getWinner()
    
    if winner == "green":
        time.sleep(0.5)
        sense.show_message("Green Wins!")
        
        return True
    elif winner == "red":
        time.sleep(0.5)
        sense.show_message("Red wins!")
        return True
    elif checkTie():
        time.sleep(0.5)
        sense.show_message("Tie!")
        return True
    else:
        print("no result")
        return False
