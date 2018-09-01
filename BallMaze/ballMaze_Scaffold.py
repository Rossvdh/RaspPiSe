# BallMaze game on SenseHat
# The scaffolding code that would be provided to first year
# students
# Raspberry Pi Sense HAT project
# Ross van der Heyde VHYROS001
# University of Cape Town Computer Science Honours CSC4000W

# REVISED ASSIGNMENT

import sense_hat
from sense_hat import ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time
from signal import pause
import bm

# define types of moves. You will need these for
# determining the type of move
DIE = -2
HOLE = -1
WALL = 0
LEGAL = 1
WIN = 2
    
# define some colours
blue = [0,0,255]
red = [255,0,0]
green = [0,255,0]
white = [255,255,255]
orange = [255,200,0]
yellow = [255,255,0]
blank = [0,0,0]

def moveBallUp():
    """Move ball one LED towards the top of the matrix"""
    # set LED at ball's previous position to off 
    sense.set_pixel(ball[0], ball[1], blank)

    #set ball's new position
    ball[1] = ball[1] + 1

    # Task 4: get the type of move and perform the appropriate action(s)
    move = getMoveType(ball)
    
    sense.set_pixel(ball[0], ball[1], orange)
        
def moveBallDown():
    """Move ball one LED towards the bottom of the matrix"""
    sense.set_pixel(ball[0], ball[1], blank)
    
    ball[1] = ball[1] - 1

    # Task 4: get the type of move and perform the appropriate action(s)
    move = getMoveType(ball)
    
    sense.set_pixel(ball[0], ball[1], orange)

def moveBallRight():
    """Move ball one LED to the right of the matrix"""
    sense.set_pixel(ball[0], ball[1], blank)
    
    ball[0] = ball[0] - 1

    # Task 4: get the type of move and perform the appropriate action(s)
    move = getMoveType(ball)
    sense.set_pixel(ball[0], ball[1], orange)

def moveBallLeft():
    """Move ball one LED to the left of the matrix"""
    sense.set_pixel(ball[0], ball[1], blank)

    ball[0] = ball[0] + 1

    # Task 4: get the type of move and perform the appropriate action(s)
    move = getMoveType(ball)
    
    sense.set_pixel(ball[0], ball[1], orange)


def getMoveType(ball):
    """Determines if the move is legal, into a wall, or results in
    a death or a win"""
    # Task 3: complete this method
    pass
    

def die():
    """Ends the game (player looses because they fell off the grid
    or moved into a hole)"""
    global ballIsAlive
    time.sleep(0.5)
    sense.show_message(text_string="You died", text_colour=[255, 51, 0])
    ballIsAlive = False

def win():
    """Player wins the game (ball has successfully been moved to the target
    LED"""
    global ballIsAlive, startTime
    totalTime = round(time.time() - startTime, 2)
    sense.set_pixel(end[0], end[1], orange)
    time.sleep(0.5)
    sense.show_message(text_string="You win", text_colour=[51, 204, 51])
    sense.show_message("Time: "+ str(totalTime)+" s")
    bm.saveTime(totalTime, mazeFileName)
    ballIsAlive = False


def play():
    """Plays the game."""
    global ballIsAlive, ball, start, playAgain, startTime

    #countdown to start
    sense.show_letter("3")
    time.sleep(1)
    sense.show_letter("2")
    time.sleep(1)
    sense.show_letter("1")
    time.sleep(1)

    #display maze
    sense.set_pixels(maze)
    ball = list(start)
    sense.set_pixel(ball[0], ball[1], orange)
    sense.set_pixel(end[0], end[1], gre)

    #start timer
    startTime = time.time()
    
    while ballIsAlive and playAgain:
        time.sleep(0.4)

        #read pitch, move ball accordingly
        gyro = sense.get_orientation_degrees()
        pitch = gyro["pitch"]
        
        #Task 1: move the ball left or right depending on the pitch angle


        if ballIsAlive:
            #Task 2: read roll angle, move ball up or down
            pass

def stopLooping(event):
    """When the user press the joystick middle button, stop starting
    a new game"""
    if event.action == ACTION_RELEASED:
        global playAgain
        playAgain = False
        print("playAgain = False")


#-----------------------------------------------------
#MAIN
#set up senseHat
sense = sense_hat.SenseHat()
sense.low_light = True
sense.set_imu_config(True, True, True)
sense.stick.direction_middle = stopLooping

#read in maze from file
mazeFileName = "maze1.txt"
start, end, maze = bm.readMaze(mazeFileName)
ball = start

#start play
playAgain = True

while playAgain:
    ballIsAlive = True
    play()

sense.clear()
print("end end")






















#####
