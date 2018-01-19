import random
from random import shuffle
import console
import pyRandomdotOrg

rnd=pyRandomdotOrg.clientlib("RandomizeList", "phi.fibonacci@gmail.com")
randomInt = rnd.IntegerGenerator(1, 1000000000)


a = []
console.clear()

#uncomment the line below to check randomInt value
#print(randomInt)

random.seed(randomInt)

while True:

    list = input("Enter names (comma separated): ")
    list = list.replace(" ", "")
    a = list.split(",")
    shuffle(a)

    for item in a:
        print(item)
    
    print()
    del a[:]
