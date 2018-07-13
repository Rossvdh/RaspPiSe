# Tic tac Toe on SenseHat
# Ross van der Heyde VHYROS001
# Univeristy of Cape Town Computer Science Honours CSC4000W
# 10 May 2018

import random, time
import sense_hat
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause


# colour is the colour to make the square. array of 3 values bewteen 0 and 255
# corresponding to red, green and blue
# row and col are the co-ords of the grid i.e. 0 - 2
def colourSquare(colour, row, col):
  row = int(row)#row and col might be floats
  col = int(col)
  sense.set_pixel(row, col, colour)
  sense.set_pixel(row+1, col, colour)
  sense.set_pixel(row, col+1, colour)
  sense.set_pixel(row+1, col+1, colour)


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
		print("redTurn: ",redTurn,"x:", red,"marker[0]:",marker[0], ". marker[1]:",marker[1])
	
		if sense.get_pixel(marker[0], marker[1]+1) == [0,0,0]:
			if redTurn:
				redTurn = not redTurn
				colourSquare(red, marker[0], marker[1])
			else:
				redTurn = not redTurn
				colourSquare(green, marker[0], marker[1])
		
		checkWinner()


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
	#check for a winning row
	pixel = isWinningRow()
	print("pixel:", pixel)
	if pixel != -1:
		#there is a winning row
		if pixel == [0,252,0]: #sometimes the colours read from the LEDs
							#do not exactly match what they were set to.
							#more details in the API.
			return green
		elif pixel == [248, 0, 0]:
			return red

	#check for winning column
	pixel = isWinningCol()
	print("pixel:", pixel)
	if pixel != -1:
		if pixel == [0,252,0]:
			return green
		elif pixel == [248, 0, 0]:
			return red
    
    #check for winning diagonal  
	pixel = isWinningDiag()
	print("pixel:", pixel)
	if pixel != -1:
		#there is a winning diag
		if pixel == [0,252,0]:
			return green
		elif pixel == [248, 0, 0]:
			return red
    
    #no winner
	return blank

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

def checkWinner():
	"""Checks if someone has won. Runs after every button action"""
	winner = getWinner()
	print("winner: ", winner)
	if winner == green:
		time.sleep(0.5)
		sense.show_message("Green Wins!")
		
		playAgain()
	elif winner == red:
		time.sleep(0.5)
		sense.show_message("Red wins!")
		playAgain()
	elif checkTie():
		time.sleep(0.5)
		sense.show_message("Tie!")
		playAgain()

def playAgain():
  time.sleep(0.5)
  sense.set_pixels(grid)
  sense.set_pixel(marker[0], marker[1], blue)


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


# define the Tic Tac Toe grid
grid=[blank,blank,white,blank,blank,white,blank,blank,
  blank,blank,white,blank,blank,white,blank,blank,
  white,white,white,white,white,white,white,white,
  blank,blank,white,blank,blank,white,blank,blank,
  blank,blank,white,blank,blank,white,blank,blank,
  white,white,white,white,white,white,white,white,
  blank,blank,white,blank,blank,white,blank,blank,
  blank,blank,white,blank,blank,white,blank,blank]


sense.show_message("Get ready!")
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
