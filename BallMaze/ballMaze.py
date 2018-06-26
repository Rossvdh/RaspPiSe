# BallMaze game on SenseHat
# Raspberry Pi Sense HAT project
# Ross van der Heyde VHYROS001
# University of Cape Town Computer Science Honours CSC4000W

import sense_hat
from sense_hat import ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time
from signal import pause

def pushed_up(event):
    if event.action == ACTION_RELEASED:
        sense.set_pixel(marker[0], marker[1], maze[8*marker[1] + marker[0]])
        marker[1] = marker[1] +1
        
        #test for type of move
        move = getMoveType(marker)
        if move == LEGAL:
            sense.set_pixel(marker[0], marker[1], ora)
        elif move == WALL:
            marker[1] = marker[1] - 1
            sense.set_pixel(marker[0], marker[1], ora)
        elif move == DIE:
            die()
        else:
            win()

        
def pushed_down(event):
    if event.action == ACTION_RELEASED:
        sense.set_pixel(marker[0], marker[1], maze[8*marker[1] + marker[0]])
        marker[1] = marker[1] - 1
        #test for type of move
        move = getMoveType(marker)
        if move == LEGAL:
            sense.set_pixel(marker[0], marker[1], ora)
        elif move == WALL:
            marker[1] = marker[1] + 1
            sense.set_pixel(marker[0], marker[1], ora)
        elif move == DIE:
            die()
        else:
            win()

def pushed_right(event):
    if event.action == ACTION_RELEASED:
        sense.set_pixel(marker[0], marker[1], maze[8*marker[1] + marker[0]])
        marker[0] = marker[0] - 1
        
        #test for type of move
        move = getMoveType(marker)
        if move == LEGAL:
            sense.set_pixel(marker[0], marker[1], ora)
        elif move == WALL:
            marker[0] = marker[0] + 1
            sense.set_pixel(marker[0], marker[1], ora)
        elif move == DIE:
            die()
        else:
            win()

def pushed_left(event):
    if event.action == ACTION_RELEASED:
        sense.set_pixel(marker[0], marker[1], maze[8*marker[1] + marker[0]])
        marker[0] = marker[0] + 1

        #test for type of move
        move = getMoveType(marker)
        if move == LEGAL:
            sense.set_pixel(marker[0], marker[1], ora)
        elif move == WALL:
            marker[0] = marker[0] - 1
            sense.set_pixel(marker[0], marker[1], ora)
        elif move == DIE:
            die()
        else:
            win()

def buttonPushed(event):
    pass

def getMoveType(marker):
    if not(0<= marker[0] <=7 and 0<= marker[1] <=7):
        return DIE #out of bounds move. you die
    elif maze[8*marker[1] + marker[0]] == blu:
        return WALL #move into wall. you can't move
    elif marker == end:
        return WIN #win
    else:
        return LEGAL #normal legal move

def die():
    time.sleep(0.5)
    sense.show_message("You died")
    #restart
    marker = start
    sense.set_pixels(maze)
    sense.set_pixel(marker[0], marker[1], ora)

def win():
    sense.set_pixel(end[0], end[1], ora)
    time.sleep(0.5)
    sense.show_message("You win")
    #restart
    marker = start
    sense.set_pixels(maze)
    sense.set_pixel(marker[0], marker[1], ora)
    
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
sense.set_imu_config(False, True, False)  # gyro only

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = buttonPushed

sense.set_pixels(maze)

start = [0,7]
end = [7,0]
marker = start
sense.set_pixel(marker[0], marker[1], ora)

print("paused")
pause()

      
##while True:
##    time.sleep(0.5)
##    accel = sense.get_orientation_degrees()
##    print("pitch: ", accel["pitch"])
##    #print("roll: ", accel["roll"])





























#####
