#!/usr/bin/python3
#encoding:utf-8
# Author: Hannah Nicholas

import colorsys
import math
import time

import unicornhathd

unicornhathd.rotation(0)
unicornhathd.brightness(1.0)

# 255,  0,  0
# 255,255,  0
#   0,255,  0
#   0,255,255
#   0,  0,255
# 255,  0,255
# 255,  0,  0

def loopColours():
    for i in range (0,255):
        setPixels(255,i,0) 
        unicornhathd.show()

    for i in range (255,0, -1):
        setPixels(i,255,0) 
        unicornhathd.show()

    for i in range (0,255):
        setPixels(0,255,i) 
        unicornhathd.show()

    for i in range (255,0, -1):
        setPixels(0,i,255) 
        unicornhathd.show()

    for i in range (0,255):
        setPixels(i,0,255) 
        unicornhathd.show()

    for i in range (255,0, -1):
        setPixels(255,0,i) 
        unicornhathd.show()


def setPixels(r,g,b):
    for x in range (0,16):
        for y in range (0,16):
            unicornhathd.set_pixel(x,y,r,g,b)

try:
    while True:
        loopColours()

except KeyboardInterrupt:
    unicornhathd.off()