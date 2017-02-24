#!/usr/local/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("value", help="value to convert")
parser.add_argument("units", help="in, inches, ft, feet")

args=parser.parse_args()

def convertInches(x):
	print(str(float(x)/67)+" smoots")

def convertFeet(x):
	print(str((float(x)*12)/67)+" smoots")

def convertMeters(x):
	print(str((float(x)*39.3701)/67)+" smoots")

def convertMiles(x):
	print(str((float(x)*63360)/67)+" smoots")

def convertLeagues(x):
	print(str((float(x)*218740)/67)+" smoots")

#convertYards(x)
#convertFootballFields(x)
#convertAU(x)
#convertLightYear(x)
#convertCubit(x)

if args.units in ("in", "inches", "inch"):
	convertInches(args.value)
elif args.units in ("ft", "feet", "foot"):
	convertFeet(args.value)
elif args.units in ("meters", "m", "meter"):
	convertMeters(args.value)
elif args.units in ("miles", "mi", "mile"):
	convertMiles(args.value)
elif args.units in ("leagues", "league"):
	convertLeagues(args.value)
else:
	print("Units not recognized")