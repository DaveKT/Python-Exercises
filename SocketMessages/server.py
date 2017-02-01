#!/usr/bin/python

import socket

s = socket.socket()         
host = "localhost"
port = 22778
s.bind((host, port))

print("Listening...")
s.listen(5)

while True:
   c, addr = s.accept() 
   print 'Got connection from', addr
   c.send('Connection Successful')
   c.close()
