# BallMaze game on SenseHat
# Raspberry Pi Sense HAT project
# Ross van der Heyde VHYROS001
# University of Cape Town Computer Science Honours CSC4000W

import sense_hat
from sense_hat import ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time
from signal import pause

def moveBallUp():
    """Move ball one LED towards the top of the matrix"""
    #the move ball methodss look like good candidates for an if statement
    #assignment. Downside is they are all basically the same
    sense.set_pixel(ball[0], ball[1], [0,0,0])
    ball[1] = ball[1] - 1
    
    #test for type of move
    move = getMoveType(ball)
    if move == LEGAL:
        sense.set_pixel(ball[0], ball[1], ora)
    elif move == WALL:
        ball[1] = ball[1] + 1
        sense.set_pixel(ball[0], ball[1], ora)
    elif move == HOLE:
        #if move into hole, let the user see they moveinto the hole before dying
        sense.set_pixel(ball[0], ball[1], [255,100,0])
        time.sleep(0.2)
        die()
    elif move == DIE:
        die()
    else:
        win()

        
def moveBallDown():
    """Move ball one LED towards the bottom of the matrix"""
    sense.set_pixel(ball[0], ball[1], [0,0,0])
    ball[1] = ball[1] + 1

    #test for type of move
    move = getMoveType(ball)
    if move == LEGAL:
        sense.set_pixel(ball[0], ball[1], ora)
    elif move == WALL:
        ball[1] = ball[1] - 1
        sense.set_pixel(ball[0], ball[1], ora)
    elif move == HOLE:
        #if move into hole, let the user see they moveinto the hole before dying
        sense.set_pixel(ball[0], ball[1], [255,100,0])
        time.sleep(0.2)
        die()
    elif move == DIE:
        die()
    else:
        win()

def moveBallRight():
    """Move ball one LED to the right of the matrix"""
    sense.set_pixel(ball[0], ball[1], [0,0,0])
    ball[0] = ball[0] + 1

    #test for type of move
    move = getMoveType(ball)
    if move == LEGAL:
        sense.set_pixel(ball[0], ball[1], ora)
    elif move == WALL:
        ball[0] = ball[0] - 1
        sense.set_pixel(ball[0], ball[1], ora)
    elif move == HOLE:
        #if move into hole, let the user see they moveinto the hole before dying
        sense.set_pixel(ball[0], ball[1], [255,100,0])
        time.sleep(0.2)
        die()
    elif move == DIE:
        die()
    else:
        win()

def moveBallLeft():
    """Move ball one LED to the left of the matrix"""
    sense.set_pixel(ball[0], ball[1], [0,0,0])
    ball[0] = ball[0] - 1
    
    #test for type of move
    move = getMoveType(ball)
    if move == LEGAL:
        sense.set_pixel(ball[0], ball[1], ora)
    elif move == WALL:
        ball[0] = ball[0] + 1
        sense.set_pixel(ball[0], ball[1], ora)
    elif move == HOLE:
        #if move into hole, let the user see they moveinto the hole before dying
        sense.set_pixel(ball[0], ball[1], [255,100,0])
        time.sleep(0.2)
        die()
    elif move == DIE:
        die()
    else:
        win()


def getMoveType(ball):
    """Determines if the move is legal, into a wall, or results in
    a death or a win"""
    #also a good candidate for if statment assignment
    if not(0<= ball[0] <=7 and 0<= ball[1] <=7):
        return DIE #out of bounds. you die
    elif maze[8*ball[1] + ball[0]] == red:
        return HOLE #move into hole. you die
    elif maze[8*ball[1] + ball[0]] == blu:
        return WALL #move into wall. you can't move
    elif ball == end:
        return WIN #win
    else:
        return LEGAL #normal legal move

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
    global ballIsAlive
    sense.set_pixel(end[0], end[1], ora)
    time.sleep(0.5)
    sense.show_message(text_string="You win", text_colour=[51, 204, 51])
    ballIsAlive = False

def play():
    """Plays the game."""
    global ballIsAlive, ball, start, playAgain

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
    sense.set_pixel(ball[0], ball[1], ora)
    sense.set_pixel(end[0], end[1], gre)
    
    while ballIsAlive and playAgain:
        print("Ball:", ball)
        time.sleep(0.4)

        #read left/right angle, move ball accordingly
        gyro = sense.get_orientation_degrees()
        pitch = gyro["pitch"]
        #these ifs also for assignment?
        if 185 < pitch < 355:
            moveBallLeft()
        elif 5 < pitch < 175:
            moveBallRight()

        #read top/bottom angle, move ball
        if ballIsAlive:
            gyro = sense.get_orientation_degrees()
            roll = gyro["roll"]
            if 185 < roll < 355:
                moveBallDown()
            elif 5 < roll < 175:
                moveBallUp()


def stopLooping(event):
    """When the user press the joystick middle button, stop starting
    a new game"""
    if event.action == ACTION_RELEASED:
        global playAgain
        playAgain = False
        print("playAgain = False")

def readMaze():
    """Reads a maze layout, including start and end points from
    a text file."""
    #provide this function in its entirety?
    mazeFile = open("maze5.txt")
    lines = mazeFile.readlines()
    mazeFile.close()

    #strip \n
    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n")

    #extract start position
    start = lines[0].split(",")
    start = list(map(int, start))
    del lines[0]

    #extract end position
    end = lines[0].split(",")
    end = list(map(int, end))
    del lines[0]

    #extract maze layout
    maze = []
    for line in lines:
        arr = line.split(" ")
        for i in arr:
            if i == "b":
                #blank LED
                maze.append(blk)
            elif i == "w":
                #wall
                maze.append(blu)
            elif i == "h":
                #h for hole
                maze.append(red)
            else:
                #target LED
                maze.append(gre)

    return start, end, maze


#-----------------------------------------------------
# define moves
DIE = -2
HOLE = -1
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

#read in maze from file
start, end, maze = readMaze()
ball = start

#set up senseHat
sense = sense_hat.SenseHat()
sense.low_light = True
sense.set_rotation(180)
sense.set_imu_config(True, True, True)
sense.stick.direction_middle = stopLooping

#start play
playAgain = True

while playAgain:
    ballIsAlive = True
    play()

sense.clear()
print("end end")

## this version works with the difference between the current angle and the
## previous. works but very jerky.   
##    if pitch - prevPitch < -2:
##        #move ball one way
##        moveBallLeft()
##    elif pitch - prevPitch > 2:
##        #move ball the other way
##        moveBallRight()
##
##    if ballIsAlive:
##        prevRoll = roll
##        roll = gyro["roll"]
##        if roll - prevRoll < -2:
##            #move ball one way
##            moveBallDown()
##        elif roll - prevRoll > 2:
##            #move ball the other way
##            moveBallUp()



























#####
