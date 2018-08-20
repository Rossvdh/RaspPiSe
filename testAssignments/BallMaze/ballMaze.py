# BallMaze game on SenseHat
# Raspberry Pi Sense HAT project
# Ross van der Heyde VHYROS001
# University of Cape Town Computer Science Honours CSC4000W

import sense_hat
from sense_hat import ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time
from signal import pause
import bm

def moveBallUp():
    """Move ball one LED towards the top of the matrix"""
    #the move ball methodss look like good candidates for an if statement
    #assignment. Downside is they are all basically the same
    #set previous current position of the ball to blank LED
    sense.set_pixel(ball[0], ball[1], [0,0,0])

    #set ball's new position, but do not set LED yet
    ball[1] = ball[1] + 1
    
    #test for type of move
    move = getMoveType(ball)
    if move == LEGAL:
        # legal move, so set LED of the ball's new position
        sense.set_pixel(ball[0], ball[1], ora)
    elif move == WALL:
        #move into wall
        #set ball's position back to current
        ball[1] = ball[1] - 1
        #set LED
        sense.set_pixel(ball[0], ball[1], ora)
    elif move == HOLE:
        #if move into hole, let the user see they move into the
        # hole before dying
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

def moveBallRight():
    """Move ball one LED to the right of the matrix"""
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

def moveBallLeft():
    """Move ball one LED to the left of the matrix"""
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


def getMoveType(ball):
    """Determines if the move is legal, into a wall, or results in
    a death or a win"""
    if not(0<= ball[0] <=7 and 0<= ball[1] <=7):
    #if ball[0] > 7 or ball[0] < 0 or ball[1] > 7 or ball[1] < 0:
        print("DIE")
        return DIE #out of bounds. you die
    elif maze[8*ball[1] + ball[0]] == red:
        print("HOLE")
        return HOLE #move into hole. you die
    elif maze[8*ball[1] + ball[0]] == blu:
        print("WALL")
        return WALL #move into wall. you can't move
    elif ball == end:
        print("WIN")
        return WIN #win
    else:
        print("LEGAL")
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
    global ballIsAlive, startTime
    totalTime = round(time.time() - startTime, 2)
    sense.set_pixel(end[0], end[1], ora)
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
    sense.set_pixel(ball[0], ball[1], ora)
    sense.set_pixel(end[0], end[1], gre)

    #start timer
    startTime = time.time()
    
    while ballIsAlive and playAgain:
        print("Ball:", ball)
        time.sleep(0.4)

        #read left/right angle, move ball accordingly
        gyro = sense.get_orientation_degrees()
        pitch = gyro["pitch"]
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
    """When the user presses the joystick middle button, stop starting
    a new game after the previous game ends"""
    if event.action == ACTION_RELEASED:
        global playAgain
        playAgain = False
        print("playAgain = False")


#-----------------------------------------------------
#read in maze from file
mazeFileName = "maze1.txt"
start, end, maze = bm.readMaze(mazeFileName)
ball = start

#set up senseHat
sense = sense_hat.SenseHat()
sense.low_light = True
sense.set_imu_config(True, True, True)
sense.stick.direction_middle = stopLooping

#start play
playAgain = True

while playAgain:
    ballIsAlive = True
    play()

sense.clear()
print("end")






#####
