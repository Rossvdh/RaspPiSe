# Module with ttt functions to make scaffolding easier (I hope)
# Ross van der Heyde VHYROS001
# UCT Computer Science Honours
# 1 August 2018

import time

# "constants"
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
blank = [0,0,0]
white = [255,255,255]

def isWinningRow(board):
    """Check if a player has won on a row (i.e. there is a row that is 
    all the same colour.) Returns the colour of the row if there is a 
    winning row, else -1"""
    for row in board:
        print("Check row. row:",row)
        if row[0] == row[1] == row[2] and row[0] != blank:
            return row[0]
    return -1

def isWinningCol(board):
    """Check if a player has won on a column i.e. there is a column that
    is all the same colour.) Returns the colour of the col if there is a 
    winning row, else -1"""
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != blank:
            return board[0][col]
    return -1

def isWinningDiag(board):
    """Check if a player has won on one of the diagonals (i.e. there is 
    a diagonal that is all the same colour). Returns the colour of the 
    diagonal if it is a winning diagonal, else -1"""
    
    #check the top left to bottom right diagonal
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != blank:
            return board[0][0]
            
    #check the top right to bottom left diagonal
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] != blank:
            return board[0][2]
    
    return -1

def getWinner(board):
    """Determine which colour has won (if any)"""
    #check for a winning row
    pixel = isWinningRow(board)
    print("pixel:", pixel)
    if pixel != -1:
        #there is a winning row
        if pixel == green:
            return "green"
        elif pixel == red:
            return "red"

    #check for winning column
    pixel = isWinningCol(board)
    print("pixel:", pixel)
    if pixel != -1:
        if pixel == green:
            return "green"
        elif pixel == red:
            return "red"

    #check for winning diagonal  
    pixel = isWinningDiag(board)
    print("pixel:", pixel)
    if pixel != -1:
        #there is a winning diag
        if pixel == green:
            return "green"
        elif pixel == red:
            return "red"

    #no winner
    return "none"


def checkTie(board):
    """Checks if the game is a tie (no winner). If there is a blank 
    pixel, at least one square of the grid is not coloured yet and it is
    not a tie yet"""
    # it is only necessary to check one pixel in each grid square
    for row in range(3):
        for col in range(3):
            if board[row][col] == blank:
                return False
    #all squares have been checked, no blanks found
    return True

#board is a 3X3 matrix
def checkForWinner(board):
    """Checks if someone has won. Runs after every button action"""
    winner = getWinner(board)
    print("winner: ", winner)
    if winner == "green":
        time.sleep(0.5)
        
        return "green"
    elif winner == "red":
        time.sleep(0.5)
        return "red"
    elif checkTie(board):
        time.sleep(0.5)
        return "tie"
    else:
        return "none"
