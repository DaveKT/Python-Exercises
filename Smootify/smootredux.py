#!/usr/local/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("value", help="value to convert")
parser.add_argument("units", help="inches or feet.")

args=parser.parse_args()

u = args.units
u = u.replace(" ", "")
u = u.lower()

v = args.value

cv = {'inches': 1,
'in': 1,
'meters': 39.3701,
'miles': 63360,
'leagues': 218740,
'yards': 36,
'yrds': 36,
'footballfields': 3600,
'americanfootballfields': 3600,
'aff': 3600,
'au': 5889679950000,
'lightyear': 372461748000000000,
'lightyears': 372461748000000000,
'ly': 372461748000000000,
'cubit': 18,
'cubits': 18,
'hand': 4,
'hands': 4,
'kesselrun': 14578004300000000000,
'parsec': 1214833690000000000,
'parsecs': 1214833690000000000,
'planck': .000000000000000000000000000000000636310383,
'plancks': .000000000000000000000000000000000636310383,
'fathom': 72,
'fathoms': 72,
'towel': 2814,
'towels': 2814,
'kilometers': 39370.1,
'km': 39370.1,
'nauticalmile': 72913.4,
'chain': 792,
'rod': 198,
'furlong': 7920.02,
'furlongs': 7920.02,
'humanhair': 0.003149606,
'humanhairs': 0.003149606,
'lunardistance': 15136704000,
'feet': 12,
'foot': 12}

def convertToSmoot(x, y):
	print(str((float(x)*float(y)/67))+" smoots")
	#print("Hello World!")

if u in cv:
	convertToSmoot(cv[u], v)
else:
	print("Units aren't supported.")
