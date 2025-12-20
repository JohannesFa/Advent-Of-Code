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
    
stones = []


for i in lines:
    item = i.strip()
    item = item.split(" ")
    #print(item)
    for j in item:
        stones.append(int(j))

#print(stones)

for i in range(25):
    print(i)
    newstonelist = []
    for stone in stones:
        #print(stone)
        newstonelist+=getNewStones(stone)
    stones = newstonelist
    #print(stones)

print(len(stones))