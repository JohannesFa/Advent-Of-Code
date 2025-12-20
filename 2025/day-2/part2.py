#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

def findDivisors(num):
    divisors = []
    for i in range(1,num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def splitToNPairs(num,divisor):
    numstr = str(num)
    numlen = len(numstr)
    pairs = []
    sectionSize = int(numlen/divisor)
    #print(f"Numstr {numstr} sectionsize {sectionSize} divisor {divisor}")
    for i in range(divisor):
        pair = ""
        #print(f" sectionindex is {i}")
        startingIndex = i*sectionSize
        for getIndex in range(startingIndex,startingIndex+sectionSize):
            #print(f"getIndex is {getIndex}")
            pair+=numstr[getIndex]
        pairs.append(pair)
    #print(pairs)
    return pairs

def checkIfInvalidPairs(pairs):
    if len(pairs) == 1:
        return False
    for pair in pairs:
        for pair2 in pairs:
            if pair != pair2:
                return False
    return True



def checkIfIsRepeating(num):
    divisors = findDivisors(len(str(num)))
    #print(f"Divisors {divisors}")


    for divisor in divisors:
        pairs = splitToNPairs(num,divisor)
        if checkIfInvalidPairs(pairs):
            return True
        
    return False

print(checkIfIsRepeating(23232323))
print("Done -------------")

idsum = 0
for i in lines:
    item = i.strip()
    for rangeText in item.split(","):
        lower,upper = map(int,rangeText.split("-"))
        for j in range(lower,upper+1):
            if checkIfIsRepeating(j):
                idsum += j

print(idsum)
