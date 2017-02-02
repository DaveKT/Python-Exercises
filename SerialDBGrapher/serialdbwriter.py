#!/usr/local/bin/python3

import serial
import sys
import argparse
import sqlite3
import signal
from datetime import datetime, date

parser = argparse.ArgumentParser()
parser.add_argument("interface", help="name of the serial interface")
parser.add_argument("baud", help="baud rate for communication")
args = parser.parse_args()

conn = sqlite3.connect("serialDBGrapherTest.db")
c = conn.cursor()

try:
	ser = serial.Serial(args.interface, args.baud)
except:
	print("Failed to connect on {}, {}".format(args.interface, args.baud))
	sys.exit()

try:
	print("Writing to DB")
	while True:
		tempf = ser.readline()
		tempf = tempf.decode("utf-8")
		tempf = tempf.strip('\r\n')
		dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		qry = "insert into temperatureReadings (datetime, temp) values ('{}', {})".format(dt, tempf)
		#print(qry)
		c.execute(qry)
		conn.commit()

except KeyboardInterrupt:
		print("Interrupted. Stopping...")
		c.close()
		conn.close()
		sys.exit()