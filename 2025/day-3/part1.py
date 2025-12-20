#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

voltagesum = 0

def findHighest(charArr1, charArr2):
    sortedArr1 = sorted(charArr1)
    sortedArr2 = sorted(charArr2)
    #print("Sortedarr",sortedArr1,sortedArr2)
    return sortedArr1[-1]+sortedArr2[-1]

def splitToPossible(charArr):
    highestFound = ""
    for i in range(1,len(charArr)):
        p1 = charArr[:i]
        p2 = charArr[i:]
        #print(p1,p2)
        tempHigh = findHighest(p1,p2)
        #print(tempHigh)
        if tempHigh > highestFound:
            highestFound = tempHigh
    return highestFound

for i in lines:
    item = i.strip()
    itemstr = str(item)
    itemarray = list(itemstr)
    #print("".join(itemarray))
    res = splitToPossible(itemarray)
    voltagesum += int(res)
    #print("H,nh",h,nh)
    #print(res)

print(voltagesum)

