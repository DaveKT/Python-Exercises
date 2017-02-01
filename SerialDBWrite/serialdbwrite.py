#!/usr/bin/python

import serial
import sys
import argparse
import sqlite3
import signal

x = ""
y = ""

parser = argparse.ArgumentParser()
parser.add_argument("interface", help="name of the serial interface")
parser.add_argument("baud", help="baud rate for communication")
args = parser.parse_args()

conn = sqlite3.connect("serialDBWriteTest.db")
c = conn.cursor()

try:
	ser = serial.Serial(args.interface, args.baud)
except:
	print "Failed to connect on {}, {}".format(args.interface, args.baud)
	sys.exit()


try:
	while True:
		input = ser.readline()
		input = input.strip("\r\n")
		data = input.split(",")
		x = data[0]
		y = data[1]
		qry = "insert into testTable (id, random) values ({}, {})".format(x, y)
		#print(qry)
		c.execute(qry)
		conn.commit()

		#use this query to fetch the last 10 records
		#select * from (select * from testTable order by id desc limit 10) order by id asc;

except KeyboardInterrupt:
		print("Interrupted. Stopping...")
		c.close()
		conn.close()
		sys.exit()