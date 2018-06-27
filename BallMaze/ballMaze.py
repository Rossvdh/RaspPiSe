# BallMaze game on SenseHat
# Raspberry Pi Sense HAT project
# Ross van der Heyde VHYROS001
# University of Cape Town Computer Science Honours CSC4000W

import sense_hat
from sense_hat import ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time
from signal import pause

def moveBallUp():
    sense.set_pixel(ball[0], ball[1], [0,0,0])
    ball[1] = ball[1] - 1
    
    #test for type of move
    move = getMoveType(ball)
    if move == LEGAL:
        sense.set_pixel(ball[0], ball[1], ora)
    elif move == DIE:
        die()
    elif move == WALL:
        ball[1] = ball[1] + 1
        sense.set_pixel(ball[0], ball[1], ora)
    else:
        win()

        
def moveBallDown():
    sense.set_pixel(ball[0], ball[1], [0,0,0])
    ball[1] = ball[1] + 1

    #test for type of move
    move = getMoveType(ball)
    if move == LEGAL:
        sense.set_pixel(ball[0], ball[1], ora)
    elif move == DIE:
        die()
    elif move == WALL:
        ball[1] = ball[1] - 1
        sense.set_pixel(ball[0], ball[1], ora)
    else:
        win()

def moveBallRight():
    sense.set_pixel(ball[0], ball[1], [0,0,0])
    ball[0] = ball[0] + 1

    #test for type of move
    move = getMoveType(ball)
    if move == LEGAL:
        sense.set_pixel(ball[0], ball[1], ora)
    elif move == WALL:
        ball[0] = ball[0] - 1
        sense.set_pixel(ball[0], ball[1], ora)
    elif move == DIE:
        die()
    else:
        win()

def moveBallLeft():
    sense.set_pixel(ball[0], ball[1], [0,0,0])
    ball[0] = ball[0] - 1
    
    #test for type of move
    move = getMoveType(ball)
    if move == LEGAL:
        sense.set_pixel(ball[0], ball[1], ora)
    elif move == WALL:
        ball[0] = ball[0] + 1
        sense.set_pixel(ball[0], ball[1], ora)
    elif move == DIE:
        die()
    else:
        win()


def getMoveType(ball):
    if not(0<= ball[0] <=7 and 0<= ball[1] <=7):
        return DIE #out of bounds move. you die
    elif maze[8*ball[1] + ball[0]] == blu:
        return WALL #move into wall. you can't move
    elif ball == end:
        return WIN #win
    else:
        return LEGAL #normal legal move

def die():
    global keepPlaying
    time.sleep(0.5)
    sense.show_message("You died")
    #restart
##    ball = start
##    sense.set_pixels(maze)
##    sense.set_pixel(ball[0], ball[1], ora)
    keepPlaying = False

def win():
    global keepPlaying
    sense.set_pixel(end[0], end[1], ora)
    time.sleep(0.5)
    sense.show_message("You win")
    #restart
##    ball = start
##    sense.set_pixels(maze)
##    sense.set_pixel(ball[0], ball[1], ora)
    keepPlaying = False
    
# define moves
DIE = -1
WALL = 0
LEGAL = 1
WIN = 2
    
# define some colours
blu = [0,0,255]
red = [255,0,0]
gre = [0,255,0]
whi = [255,255,255]
ora = [255,200,0]
yel = [255,255,0]
blk = [0,0,0]

#define a maze
maze = [blk, blk, blk, blk, blu, blk, blk, gre,
	blk, blk, blk, blk, blu, blk, blk, blk,
	blu, blu, blk, blk, blu, blu, blk, blk,
	blk, blk, blk, blk, blk, blu, blk, blk,
	blk, blk, blk, blk, blk, blk, blk, blk,
	blk, blk, blk, blk, blk, blk, blk, blu,
	blk, blk, blk, blu, blk, blk, blu, blu,
	blk, blk, blk, blu, blk, blk, blk, blk]

sense = sense_hat.SenseHat()
sense.low_light = True
sense.set_rotation(180)
sense.set_imu_config(True, True, True)

sense.set_pixels(maze)

start = [0,7]
end = [7,0]
ball = start
sense.set_pixel(ball[0], ball[1], ora)

gyro = sense.get_orientation_degrees()
prevPitch = gyro["pitch"]
pitch = gyro["pitch"]

prevRoll = gyro["roll"]
roll = gyro["roll"]

keepPlaying = True

while keepPlaying:
    time.sleep(0.1)
    gyro = sense.get_orientation_degrees()
    prevPitch = pitch
    pitch = gyro["pitch"]

    if pitch - prevPitch < -2:
        #move ball one way
        moveBallLeft()
    elif pitch - prevPitch > 2:
        #move ball the other way
        moveBallRight()

    if keepPlaying:
        prevRoll = roll
        roll = gyro["roll"]
        if roll - prevRoll < -2:
            #move ball one way
            moveBallDown()
        elif roll - prevRoll > 2:
            #move ball the other way
            moveBallUp()

print("end")



























#####
