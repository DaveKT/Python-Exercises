#!/usr/bin/python

import socket

s = socket.socket()
host = "127.0.0.1" 
port = 22778

s.connect((host, port))
print s.recv(80)
s.close 