#!/usr/local/bin/python3

# Author: David Kolet-Tassara

import argparse

parser = argparse.ArgumentParser(
	description='''This application converts values from supported units to Smoots. \n 
	Supported units include: \n
	inches, feet, yards, miles, American football fields, meters, leagues, fathoms,\n
	parsecs, astronomical units, light years, cubits, and hands.''')
parser.add_argument("value", help="value to convert")
parser.add_argument("units", help="inches, feet, meters, etc. See list above for supported units.")

args=parser.parse_args()

q=args.units
q=q.replace(" ", "")
q=q.lower()

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

def convertYards(x):
	print(str((float(x)*36)/67)+" smoots")

def convertFootballFields(x):
	print(str((float(x)*3600)/67)+" smoots")

def convertAU(x):
	print(str((float(x)*5889679950000)/67)+" smoots")

def convertLightYear(x):
	print(str((float(x)*372461748000000000)/67)+" smoots")

def convertCubit(x):
	print(str((float(x)*18)/67)+" smoots")

def convertHand(x):
	print(str((float(x)*4)/67)+" smoots")

def convertKesselRun(x): #12 Parsecs
	print(str((float(x)*14578004300000000000)/67)+" smoots")

def convertParsec(x):
	print(str((float(x)*1214833690000000000)/67)+" smoots")

def convertPlanck(x):
	print(str((float(x)*.000000000000000000000000000000000636310383)/67)+" smoots")

def convertFathom(x):
	print(str((float(x)*72)/67)+" smoots")

def convertTowel(x): #the question
	print(str((float(x)*2814)/67)+" smoots")

def convertKilometers(x):
	print(str((float(x)*39370.1)/67)+" smoots")

def convertNauticalMile(x):
	print(str((float(x)*72913.4)/67)+" smoots")

def convertChain(x):
	print(str((float(x)*792)/67)+" smoots")

def convertRod(x):
	print(str((float(x)*198)/67)+" smoots")

def convertFurlong(x):
	print(str((float(x)*7920.02)/67)+" smoots")

def convertHumanHair(x):
	print(str((float(x)*0.003149606)/67)+" smoots")

def convertLunarDistance(x):
	print(str((float(x)*15136704000)/67)+" smoots")


if q in ("in", "inches", "inch"):
	convertInches(args.value)
elif q in ("ft", "feet", "foot"):
	convertFeet(args.value)
elif q in ("meters", "m", "meter"):
	convertMeters(args.value)
elif q in ("miles", "mi", "mile"):
	convertMiles(args.value)
elif q in ("leagues", "league"):
	convertLeagues(args.value)
elif q in ("yard", "yards", "yrd", "yrds"):
	convertYards(args.value)
elif q in ("footballfields", "ff", "americanfootballfields", "aff"):
	convertFootballFields(args.value)
elif q in ("au", "astronomicalunits"):
	convertAU(args.value)
elif q in ("ly", "lightyears", "light-years"):
	convertLightYear(args.value)
elif q in ("cubits", "cubit"):
	convertCubit(args.value)
elif q in ("hand", "hands"):
	convertHand(args.value)
elif q in ("kesselrun", "kr", "solo", "han"):
	#despite rumors the record still stands
	convertKesselRun(args.value)
elif q in ("parsecs"):
	convertParsec(args.value)
elif q in ("pl", "planck"):
	convertPlanck(args.value)
elif q in ("fathom", "ftm"):
	convertFathom(args.value)
elif q in ("towel", "towels"):
	#don't leave home without it!
	convertTowel(args.value)
elif q in ("kilometers", "kilometer", "km"):
	convertKilometers(args.value)
elif q in ("nauticalmiles", "nauticalmile", "nm", "seamile"):
	convertNauticalMile(args.value)
elif q in ("chain", "chains"):
	convertChain(args.value)
elif q in ("rod", "rods"):
	convertRod(args.value)
elif q in ("furlong", "furlongs"):
	convertFurlong(args.value)
elif q in ("humanhair", "hh"):
	convertHumanHair(args.value)
elif q in ("lunardistance", "averagelunardistance", "ld"):
	convertLunarDistance(args.value)
else:
	print("Units not recognized")