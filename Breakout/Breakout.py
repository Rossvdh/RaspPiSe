# Implementing the breakout game on SenseHat
# Ross van der Heyde
# University of Cape Town Computer Science Honours
# 10 July 2018

import sense_hat
from sense_hat import ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time
from signal import pause
import random

def stopGame(event):
    """Stops the gameplay"""
    global keepPlaying
    keepPlaying = False;

# there's got to be a better way of doing this function
def moveBall():
    """Moves the ball. Deletes a brick if the ball hits one."""
    global ball, ballDir, grid
    if ballDir == NW:
        if grid[8*ball[1] + ball[0]] == ora:
            ballDir = SW
            grid[8*ball[1] + ball[0]] = blk
            ball[0]-=1
            ball[1]+=1

            if ball[0] < 0 :
                ballDir = SE
                ball[0]+=2
                #check for bounce on side of LED matrix
                if ball[0] <0:
                    ballDir = NE
                    ball[0]+=2

                #check for bounce on top edge of matrix
                if ball[1] < 0:
                    ballDir = SW
                    ball[1]+=2

            if ball[1] >= 7:
                die()
                return
            return
        
        #move up and left
        ball[0]-=1
        ball[1]-=1

        #check for bounce on side of LED matrix
        if ball[0] <0:
            ballDir = NE
            ball[0]+=2

        #check for bounce on top edge of matrix
        if ball[1] < 0:
            ballDir = SW
            ball[1]+=2

        #check for bounce on blue LED
        if grid[8*ball[1] + ball[0]] == blu:
            grid[8*ball[1] + ball[0]] = ora
            
    elif ballDir == NE:
        if grid[8*ball[1] + ball[0]] == ora:
            grid[8*ball[1] + ball[0]] = blk
            ballDir = SE
            ball[0]+=1
            ball[1]+=1

            if ball[0] > 7:
                ballDir = SW
                ball[0]-=2

            if ball[1] >= 7:
                die()
            return
            
        #move up and right
        ball[0]+=1
        ball[1]-=1

        if ball[0] > 7:
            ballDir = NW
            ball[0]-=2

        if ball[1] < 0:
            ballDir = SE
            ball[1]+=2

        #check for bounce on blue LED
        if grid[8*ball[1] + ball[0]] == blu:
            grid[8*ball[1] + ball[0]] = ora
        
    elif ballDir == SE:
        if grid[8*ball[1] + ball[0]] == ora:
            grid[8*ball[1] + ball[0]] = blk
            ballDir = NE
            ball[0]+=1
            ball[1]-=1
            return

        # check for bounce on bar
        if ball[1] == 6 and (bar[0][0] <= ball[0] <= bar[0][0] + 2):
            ballDir = NE
            ball[0]+=1
            ball[1]-=1

            if ball[0] > 7:
                ballDir = NW
                ball[0]-=2

            if ball[1] < 0:
                ballDir = SE
                ball[1]+=2
            return
            
        #down and right
        ball[0]+=1
        ball[1]+=1

        if ball[0] > 7:
            ballDir = SW
            ball[0]-=2

        if ball[1] >= 7:
            die()
            return

        #check for bounce on blue LED
        if grid[8*ball[1] + ball[0]] == blu:
            grid[8*ball[1] + ball[0]] = ora

    else: #SW
        if grid[8*ball[1] + ball[0]] == ora:
            grid[8*ball[1] + ball[0]] = blk
            ballDir = NW
            ball[0]-=1
            ball[1]-=1
            return

        # check for bounce on bar
        if ball[1] == 6 and (bar[0][0] <= ball[0] <= bar[0][0] + 2):
            ballDir = NW
            ball[0]-=1
            ball[1]-=1
            return
        
        #SW: down and left
        ball[0]-=1
        ball[1]+=1

        if ball[0] < 0 :
            ballDir = SE
            ball[0]+=2
            #check for bounce on side of LED matrix
            if ball[0] <0:
                ballDir = NE
                ball[0]+=2

            #check for bounce on top edge of matrix
            if ball[1] < 0:
                ballDir = SW
                ball[1]+=2

        if ball[1] >= 7:
            die()
            return

        #check for bounce on blue LED
        if grid[8*ball[1] + ball[0]] == blu:
            grid[8*ball[1] + ball[0]] = ora
            

def die():
    global alive
    alive = False
    print("die")

def refreshMatrix():
    """Updates the LED matrix"""
    sense.set_pixels(grid)

    for i in bar:
        sense.set_pixel(i[0], i[1], whi)

    sense.set_pixel(ball[0], ball[1], gre)

def moveBarRight(event):
    """Move the bounce bar one LED right"""
    if event.action == ACTION_RELEASED:
        global bar

        for i in bar:
            sense.set_pixel(i[0], i[1], blk)

        # for when rotation has been set to something else
        # (mostly just for my convenience)
        if sense.rotation== 0:
            for i in reversed(bar):
                i[0]+=1

                if i[0] > 7:
                    i[0]-=1
                    break
        else:
            for i in bar:
                i[0]-=1

                if i[0] < 0:
                    i[0]+=1
                    break
                
        for i in bar:
            sense.set_pixel(i[0], i[1], whi)
            
def moveBarLeft(event):
    """Move the bounce bar one LED left"""
    if event.action == ACTION_RELEASED:
        global bar

        # set old position of bar to blanks
        for i in bar:
            sense.set_pixel(i[0], i[1], blk)
        
        if sense.rotation== 0:
            for i in bar:
                i[0]-=1

                if i[0] < 0:
                    i[0]+=1
                    break
        else:
            #start at the right end of the bar as that point will go
            # out of bounds first (if it goes out of bounds)
            for i in reversed(bar):
                i[0]+=1

                if i[0] > 7:
                    i[0]-=1
                    break
        # move immediately for smooth movement
        for i in bar:
            sense.set_pixel(i[0], i[1], whi)

#set up the senseHat stuff
sense = sense_hat.SenseHat()

sense.low_light = True
sense.set_rotation(180) # for my convenience
##sense.stick.direction_down = down
##sense.stick.direction_up = up
sense.stick.direction_left = moveBarLeft
sense.stick.direction_right = moveBarRight
sense.stick.direction_middle = stopGame

blu = [0,0,255]
red = [255,0,0]
gre = [0,255,0]
whi = [255,255,255]
ora = [255,200,0]
yel = [255,255,0]
blk = [0,0,0]

#constants for the ball's direction
NE = 0
NW = 1
SE = 2
SW = 3



keepPlaying = True
alive = True


while keepPlaying:
    # countdown
    sense.show_letter("3")
    time.sleep(1)
    sense.show_letter("2")
    time.sleep(1)
    sense.show_letter("1")
    time.sleep(1)


    #display initial block
    grid = [blu, blu, blu, blu, blu, blu, blu, blu,
            blu, blu, blu, blu, blu, blu, blu, blu,
            blu, blu, blu, blu, blu, blu, blu, blu,
            blk, blk, blk, blk, blk, blk, blk, blk,
            blk, blk, blk, blk, blk, blk, blk, blk,
            blk, blk, blk, blk, blk, blk, blk, blk,
            blk, blk, blk, blk, blk, blk, blk, blk,
            blk, blk, blk, blk, blk, blk, blk, blk]
    sense.set_pixels(grid)

    #display bar
    # make the bar and ball start at a random place?
    bar = [[2,7], [3,7], [4,7]]
    for i in bar:
        sense.set_pixel(i[0], i[1], whi)

    #display ball
    ball = [3,6]
    sense.set_pixel(ball[0], ball[1], gre)
    ballDir = NW
    alive = True
    
    while alive:
        time.sleep(0.4)
        moveBall()
        refreshMatrix()
    sense.show_message("You died", text_colour=[255,51,0])
    sense.clear()

print("end end")










#
