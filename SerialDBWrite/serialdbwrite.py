#!/usr/bin/python

import serial
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("interface", help="serial interface to connect")
parser.add_argument("baud", help="baud rate for communication")
args = parser.parse_args()

try:
	ser = serial.Serial(args.interface, args.baud)
except:
	print "Failed to connect on {}, {}".format(args.interface, args.baud)
	sys.exit()

while True:
	print ser.read()
