#!/usr/env/bin/microbit micropython
# move a pixel

from microbit import *


class dot(object):

    def __init__(self):
        self.pos = [2, 2]

    # returns -2 to 2 from -1024 to +1024, empirically calculated
    def tilt(self, a):
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

    def GetInput(self):
        directionRaw = accelerometer.get_values()
        x = self.tilt(directionRaw[0])
        y = self.tilt(directionRaw[1])
        return x, y

    def move(self, posx, posy, xdir, ydir):
        xt, yt = self.GetInput()
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

    def draw(self, newx, newy):
        display.clear()
        display.set_pixel(newx, newy, 9)


pixel = dot()
try:
    xint = 1
    yint = 0
    pos = pixel.move(pixel.pos[0], pixel.pos[1], xint, yint)
    pixel.draw(pos[0], pos[1])
    sleep(500)

    while True:
        pos = pixel.move(pos[0], pos[1], pos[2], pos[3])
        pixel.draw(pos[0], pos[1])
        sleep(500)

finally:
    reset()
