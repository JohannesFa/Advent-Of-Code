#By LazerK3
import os
from math import log10
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

def removeLeadingZeros(stringnumber):
    for i in range(len(stringnumber)):
        if stringnumber[i] != "0":
            return stringnumber[i:]
    return 0
def getNewStones(stone):
    if stone != 0:
        stonelenth = len(str(stone))
    if stone == 0:
        return [1]
    elif stonelenth%2 == 0:
        stonetext = str(stone)
        halfstonelength = int(stonelenth/2)
        newstone1 = stonetext[:halfstonelength]
        newstone2 = stonetext[halfstonelength:]
        return [int(newstone1),int(removeLeadingZeros(newstone2))]
    else:
        return [stone*2024]
    
stonesdict = {}


for i in lines:
    item = i.strip()
    item = item.split(" ")
    #print(item)
    for j in item:
        stonesdict[int(j)] = 1

#print(stones)

for i in range(75):
    #print(i+1)
    newstonesdict = {}
    for stone in stonesdict:
        #print(stone)
        newstones = getNewStones(stone)
        for newstone in newstones:
            if newstone in newstonesdict:
                newstonesdict[newstone] += stonesdict[stone]
            else:
                newstonesdict[newstone] = stonesdict[stone]
    stonesdict = newstonesdict
    #print(stonesdict)

counter = 0
for stone in stonesdict:
    counter += stonesdict[stone]
print(len(stonesdict))
#print(stonesdict)
print(counter)