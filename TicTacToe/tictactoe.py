# Tic tac Toe on SenseHat
# Ross van der Heyde VHYROS001
# Univeristy of Cape Town Computer Science Honours CSC4000W
# 10 May 2018

import random, time
import sense_hat
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause

sense = sense_hat.SenseHat()
redTurn = True

# colour is the colour to make the square
# row and col are the co-ords of the grid i.e. 0 - 2
def colourSquare(colour, row, col):
  row = int(row)
  col = int(col)
  sense.set_pixel(row,col,colour)
  sense.set_pixel(row+1,col,colour)
  sense.set_pixel(row,col+1,colour)
  sense.set_pixel(row+1,col+1,colour)


def pushed_up(event):
	"""What happens when the joystick is pushed up. The marker moves up
	to the next square"""
	print("up pushed. but move down")
	if event.action == ACTION_RELEASED:
		sense.set_pixel(marker[0], marker[1], sense.get_pixel(marker[0]+1, marker[1]))
		marker[1] = (marker[1] + 3) % 9
		sense.set_pixel(marker[0], marker[1], blue)

def pushed_down(event):
	"""What happens when the joystick is pushed up. The marker moves 
	down to square below the current one"""
	print("down pushed, but move up")
	if event.action == ACTION_RELEASED:
		sense.set_pixel(marker[0], marker[1], sense.get_pixel(marker[0]+1, marker[1]))
		marker[1] = (marker[1] - 3) % 9
		sense.set_pixel(marker[0], marker[1], blue)

def pushed_left(event):
	"""What happens when the joystick is pushed up. The marker moves to
	the square left of the current one"""
	print("left pushed, but move right")
	if event.action == ACTION_RELEASED:
		sense.set_pixel(marker[0], marker[1], sense.get_pixel(marker[0]+1, marker[1]))
		marker[0] = (marker[0] + 3) % 9
		sense.set_pixel(marker[0], marker[1], blue)

def pushed_right(event):
	print("right pushed, but move left")
	"""What happens when the joystick is pushed up. The marker moves to
	the square right of the current one"""
	if event.action == ACTION_RELEASED:
		sense.set_pixel(marker[0], marker[1], sense.get_pixel(marker[0]+1, marker[1]))
		marker[0] = (marker[0] - 3) % 9
		sense.set_pixel(marker[0], marker[1], blue)

def buttonPushed(event):
	"""What happens when the joystick is pushed up. The square is 
	coloured with the appropriate colour"""
	global redTurn
	print("button pushed")
	if event.action == ACTION_RELEASED:
		print("released")
		print("redTurn: ",redTurn,"x:", red,"marker[0]:",marker[0], ". marker[1]:",marker[1])
	
		if sense.get_pixel(marker[0], marker[1]+1) == [0,0,0]:
			if redTurn:
				redTurn = not redTurn
				colourSquare(red, marker[0], marker[1])
			else:
				redTurn = not redTurn
				colourSquare(green, marker[0], marker[1])


def isWinningRow():
	"""Check if a player has won on a row"""
	for i in [1,4,7]:
		if sense.get_pixel(1,i) == sense.get_pixel(4,i) == sense.get_pixel(7,i):
			return sense.get_pixel(1,i);
	return -1

def isWinningCol():
	"""Check if a player has won on a column"""
	for i in [1,4,7]:
		if sense.get_pixel(i,1) == sense.get_pixel(i,4) == sense.get_pixel(i,7):
			return sense.get_pixel(i,1)
	return -1

def isWinningDiag():
	"""Check if a player has won on one of the diagonals"""
	if sense.get_pixel(1,1) == sense.get_pixel(4,4) == sense.get_pixel(7,7):
		return sense.get_pixel(1,1)
	if sense.get_pixel(6,1) == sense.get_pixel(3,4) == sense.get_pixel(0,7):
		return sense.get_pixel(6,1)
	return -1
  
def getWinner():
	"""Determine which colour has won (if any)"""
	#check rows
	pixel = isWinningRow()
	print("check rows returns:", pixel)
	if pixel != -1:
		#theres a winning row
		if pixel == [0,252,0]:
			return green
		elif pixel == blank:
			pass
		else:
			return red
  
	pixel = isWinningCol()
	print("check cols returns:", pixel)
	if pixel != -1:
		if pixel == [0,252,0]:
			return green
		elif pixel == blank:
			pass
		else:
			return red
      
	pixel = isWinningDiag()
	print("check diags returns:", pixel)
	if pixel != -1:
		#theres a winning diag
		if pixel == [0,252,0]:
			return green
		elif pixel == blank:
			pass
		else:
			return red

      
	return blank

def checkTie():
	for i in [1, 4, 7]:
		for j in [1, 4, 7]:
			if sense.get_pixel(i,j) == blank:
				return False
	return True

def checkWinner():
	"""Checks if someone has won. Runs after every button action"""
	winner = getWinner()
	if winner == green:
		time.sleep(0.5)
		sense.show_message("Green Wins!")
		print("green wins")
		time.sleep(0.5)
		sense.set_pixels(grid)
	elif winner == red:
		time.sleep(0.5)
		sense.show_message("Red wins!")
		print("red wins")
		time.sleep(0.5)
		sense.set_pixels(grid)
	else:
		#check if tie
		if checkTie():
			print("tie")
			time.sleep(0.5)
			sense.show_message("Tie!")
			time.sleep(0.5)
			sense.set_pixels(grid)
		print("No winner yet")
	
  
#set functions for jotstick buttons
sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = buttonPushed
sense.stick.direction_any = checkWinner

#define some colours
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
blank = [0,0,0]
white = [255,255,255]

grid=[blank,blank,white,blank,blank,white,blank,blank,
  blank,blank,white,blank,blank,white,blank,blank,
  white,white,white,white,white,white,white,white,
  blank,blank,white,blank,blank,white,blank,blank,
  blank,blank,white,blank,blank,white,blank,blank,
  white,white,white,white,white,white,white,white,
  blank,blank,white,blank,blank,white,blank,blank,
  blank,blank,white,blank,blank,white,blank,blank]

sense.low_light = True;
sense.set_rotation(180)
sense.set_pixels(grid)
marker=[0,0]
sense.set_pixel(marker[0], marker[1], blue)
print("about to pause")
pause() #stop execution and wait for event
