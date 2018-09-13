#!/usr/bin/python

import serial
import sys
import argparse
import signal

parser = argparse.ArgumentParser()
parser.add_argument("interface", help="name of serial interface Arduino is connected to")
parser.add_argument("baud", help="baud rate for communication")
args = parser.parse_args()

try:
	ser = serial.Serial(args.interface, args.baud)
except:
	print "Failed to connect on {}, {}".format(args.interface, args.baud)
	sys.exit()

while True:
    input = ""
    input = ser.readline()
    if input:
        print input

    # TODO: add code to read from console and write to serial
    # TODO: convert to python3
