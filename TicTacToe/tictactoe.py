# Tic tac Toe on SenseHat
# Ross van der Heyde VHYROS001
# Univeristy of Cape Town Computer Science Honours CSC4000W
# 10 May 2018

import random, time
import sense_hat
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause

sense = sense_hat.SenseHat()
xTurn = True
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
  if event.action == ACTION_RELEASED:
    sense.set_pixel(marker[0], marker[1], sense.get_pixel(marker[0]+1, marker[1]))
    marker[1] = (marker[1] -3) % 9
    sense.set_pixel(marker[0], marker[1], u)

def pushed_down(event):
  if event.action == ACTION_RELEASED:
    sense.set_pixel(marker[0], marker[1], sense.get_pixel(marker[0]+1, marker[1]))
    marker[1] = (marker[1] +3) % 9
    sense.set_pixel(marker[0], marker[1], u)

def pushed_left(event):
  if event.action == ACTION_RELEASED:
    sense.set_pixel(marker[0], marker[1], sense.get_pixel(marker[0]+1, marker[1]))
    marker[0] = (marker[0] -3) % 9
    sense.set_pixel(marker[0], marker[1], u)

def pushed_right(event):
  if event.action == ACTION_RELEASED:
    sense.set_pixel(marker[0], marker[1], sense.get_pixel(marker[0]+1, marker[1]))
    marker[0] = (marker[0] +3) % 9
    sense.set_pixel(marker[0], marker[1], u)

def buttonPushed(event):
  global xTurn
  print("button pushed")
  if event.action == ACTION_RELEASED:
    print("released")
    print("xTurn: ",xTurn,"x:", x,"marker[0]:",marker[0], ". marker[1]:",marker[1])
    
  if sense.get_pixel(marker[0], marker[1]+1) == [0,0,0]:
    if xTurn:
      xTurn = not xTurn
      colourSquare(x, marker[0], marker[1])
    else:
      xTurn = not xTurn
      colourSquare(o, marker[0], marker[1])


def isWinningRow():
  for i in range(0,3):
    if sense.get_pixel(i,1) == sense.get_pixel(i,4) == sense.get_pixel(i,7):
      return [i,1];
  return -1

def isWinningCol():
  for i in range(0,3):
    if sense.get_pixel(1,i) == sense.get_pixel(4,i) == sense.get_pixel(7,1):
      return [1,i]
  return -1

def isWinningDiag():
  if sense.get_pixel(1,1) == sense.get_pixel(4,4) == sense.get_pixel(7,7):
    return [1,1]
  if sense.get_pixel(1,6) == sense.get_pixel(4,3) == sense.get_pixel(7,1):
    return [1,6]
  return -1
  
def getWinner():
  #check rows
  pixel = isWinningRow()
  if pixel != -1:
    #theres a winning row
    if pixel == [255,0,0]:
      # x (red) is winner
      return x
    else:
      return o
  
  pixel = isWinningCol()
  if pixel != -1:
    #theres a winning row
    if pixel == [255,0,0]:
      # x (red) is winner
      return x
    else:
      return o  
      
  pixel = isWinningDiag()
  if pixel != -1:
    #theres a winning row
    if pixel == [255,0,0]:
      # x (red) is winner
      return x
    else:
      return o
      
  return b

def checkWinner():
  if getWinner == x:
    time.sleep(0.3)
    sense.set_pixels([x, x, x, x, x, x, x, x,
      x, b, b, b, b, b, b, x,
      x, b, x, x, x, x, b, x,
      x, b, x, b, b, x, b, x,
      x, b, x, b, b, x, b, x,
      x, b, x, x, x, x, b, x,
      x, b, b, b, b, b, b, x,
      x, x, x, x, x, x, x, x])
  elif getWinner == o:
    time.sleep(0.3)
    sense.set_pixels([o, o, o, o, o, o, o, o,
      o, b, b, b, b, b, b, o,
      o, b, o, o, o, o, b, o,
      o, b, o, b, b, o, b, o,
      o, b, o, b, b, o, b, o,
      o, b, o, o, o, o, b, o,
      o, b, b, b, b, b, b, o,
      o, o, o, o, o, o, o, o])
  else:
    return
  time.sleep(1)
  sense.set_pixels(grid)

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = buttonPushed
sense.stick.direction_any = checkWinner

x = [255,0,0]
o = [0,255,0]
u = [0,0,255]
b = [0,0,0]
w = [255,255,255]

grid=[b,b,w,b,b,w,b,b,
  b,b,w,b,b,w,b,b,
  w,w,w,w,w,w,w,w,
  b,b,w,b,b,w,b,b,
  b,b,w,b,b,w,b,b,
  w,w,w,w,w,w,w,w,
  b,b,w,b,b,w,b,b,
  b,b,w,b,b,w,b,b]

sense.low_light = True;
sense.set_pixels(grid)
marker=[0,0]
sense.set_pixel(marker[0], marker[1], u)
print("about to pause")
pause() #stop execution and wiat for event
