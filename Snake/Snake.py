# Implementing Snake game on SenseHat
# UCT Computer Science CSC4000W RaspPiSe project
# Ross van der Heyde
# 2 July 2018

import sense_hat
from sense_hat import ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time
from signal import pause

def down():
    pass

def up():
    pass

def left():
    pass

def right():
    pass

#MAIN
sense = sense_hat.SenseHat()

sense.low_light = True
sense.set_rotation(180)

sense.stick.direction_down = down
sense.stick.direction_up = up
sense.stick.direction_left = left
sense.stick.direction_right = right

sense.show_message("Snake hisssssssss")
