#Author: David Kolet-Tassara

#!/usr/local/bin/python3

import argparse
import hashlib

BLOCKSIZE=65536

parser = argparse.ArgumentParser()
parser.add_argument("hash", help="The precalculated SHA1 hash value reported by the author")
parser.add_argument("file", help="The file to verify")
args=parser.parse_args()

hasher = hashlib.sha1()
with open(args.file, 'rb') as file:
	buf = file.read(BLOCKSIZE)
	while len(buf) > 0:
		hasher.update(buf)
		buf = file.read(BLOCKSIZE)

calculatedDigest = hasher.hexdigest()

if calculatedDigest == args.hash:
	print("FILE OK")
	print("{} : Calculated Value".format(calculatedDigest))
	print("{} : User Provided Value".format(args.hash))
else:
	print("FILE CHECK FAILED")
	print("{} : Calculated Value".format(calculatedDigest))
	print("{} : User Provided Value".format(args.hash))
