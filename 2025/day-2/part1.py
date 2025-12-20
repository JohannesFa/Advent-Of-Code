#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

#def findDivisors(num):
#    divisors = []
#    for i in range(1,num+1):
#        if num % i == 0:
#            divisors.append(i)
#    return divisors
#
#def splitToNPairs(num,divisor):
#    numstr = str(num)
#    pairs = []
#    sectionSize = int(num/divisor)
#    print(f"Numstr {numstr} sectionsize {sectionSize}")
#    for i in range(divisor):
#        pair = ""
#        print(f" divisor is {divisor}")
#        for getIndex in range(i,i+sectionSize):
#            print(f"getIndex is {getIndex}")
#            pair+=numstr[getIndex]
#        pairs.append(pair)
#    return pairs
#
#
#def checkIfIsRepeating(num):
#    divisors = findDivisors(len(str(num)))
#
#    
#    for divisor in divisors:
#        pairs = splitToNPairs(num,divisor)


def checkIfIsRepeating(num):
    numstr = str(num)
    numlen = len(numstr)
    
    if numlen%2 != 0:
        return False
    else:
        midIndex = int(numlen/2)
        firstHalf = numstr[:midIndex]
        secondHalf = numstr[midIndex:]
        #print(f"firstHalf {firstHalf}")
        #print(secondHalf)
        #print(midIndex)
        if firstHalf == secondHalf:
            return True

    return False



print(checkIfIsRepeating(232323232323))
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
