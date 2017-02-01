#!/usr/bin/python

import serial
import sys
import argparse
import sqlite3

parser = argparse.ArgumentParser()
parser.add_argument("interface", help="serial interface to connect")
parser.add_argument("baud", help="baud rate for communication")
args = parser.parse_args()

#conn = sqlite3.connect("testSerialDB.db")
#c = conn.cursor()

try:
	ser = serial.Serial(args.interface, args.baud)
except:
	print "Failed to connect on {}, {}".format(args.interface, args.baud)
	sys.exit()

while True:
	input = ser.readline()
	input = input.strip("\r\n")
	data = input.split(",")
	print(data[1])
