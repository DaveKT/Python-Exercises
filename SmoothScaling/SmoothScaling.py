#!/usr/local/bin/python3

# Author: 	David Kolet-Tassara
# Date:		22 FEB 2017
# Purpose:	Provide an example of linear interpolation and sine wave math to provide a
#			smooth transition between two values. This code will "draw" a verticle
#			histogram that demos the transition.
# Credit:	Tony DiCola, https://youtu.be/FAhLBSLfnuQ 

import time
import math
import serial

FREQUENCY = 1.0 	# How many times per second the cycle runs
MINSTARS = 0 		# Minimum number of stars in the cycle
MAXSTARS = 100 		# Maximum number of stars in the cycle


#https://en.wikipedia.org/wiki/Linear_interpolation
def lerp(x, x0, x1, y0, y1):
	return y0 + (x-x0)*((y1-y0)/(x1-x0))

while True:
	current = time.monotonic()

	#https://en.wikipedia.org/wiki/Sine_wave
	x = math.sin(2.0*math.pi*FREQUENCY*current)

	calcV = lerp(x, -1, 1, MINSTARS, MAXSTARS)
	
	for i in range(1, int(calcV)):
		print('x', end='', flush=True)
	print()

	time.sleep(.01)