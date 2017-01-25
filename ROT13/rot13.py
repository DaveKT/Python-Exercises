#!/usr/local/bin/python3

#Author: David Kolet-Tassa

import argparse
import io


parser = argparse.ArgumentParser()
parser.add_argument("infile", help="A text file that will be encyphered with ROT13")
parser.add_argument("outfile", help="The desired name of the output file.")
args=parser.parse_args()

def rotate(intext):
	
	rot13 = str.maketrans(
		"ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    	"NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
	return str.translate(intext, rot13)



fi = open(args.infile, "r")
fo = open(args.outfile, "w")

for line in fi:
	fo.write(rotate(line))

fi.close()
fo.close()