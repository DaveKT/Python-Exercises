#!/usr/local/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("n", help="The number to be factorialized", type=int)
args = parser.parse_args()

def factorial( n ):
    if n < 1:
       return 1 # base case

    else:
       returnNumber = n * factorial( n - 1 )  # recursive call
       return returnNumber

#TODO format the output value with commas
print(str(args.n) + '! = ' + str(factorial(args.n)))
