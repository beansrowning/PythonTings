#!/usr/env/bin/microbit micropython
'''
    Move a pixel around the screen 
    31/5 - Removed pixel class, as it was not needed.
'''

from microbit import *


# returns -2 to 2 from -1024 to +1024, empirically calculated
def tilt(a):
    a = a + 1024  # range 0 to 2048
    a = min(a, 2048)
    a = max(a, 0)
    if a < 512:
        return -2
    if a < 853:
        return -1
    if a < 1194:
        return 0
    if a < 1536:
        return 1
    return 2

def GetInput():
    directionRaw = accelerometer.get_values()
    x = tilt(directionRaw[0])
    y = tilt(directionRaw[1])
    return x, y

def move(posx, posy, xdir, ydir):
    xt, yt = GetInput()
    if xt > 0:
        xdir = 1
    if xt < 0:
        xdir = -1
    if xt == 0:
        xdir = 0
    if yt > 0:
        ydir = 1
    if yt < 0:
        ydir = -1
    if yt == 0:
        ydir = 0
    posx = (posx + xdir) % 5
    posy = (posy + ydir) % 5
    return posx, posy, xdir, ydir

def draw(newx, newy):
    display.clear()
    display.set_pixel(newx, newy, 9)



try:
    
    # Start dot in the middle of the microbit with no movement
    pos = [2, 2, 0, 0]
    
    while True:
        pos = move(pos[0], pos[1], pos[2], pos[3])
        draw(pos[0], pos[1])
        sleep(500)

finally:
    reset()
