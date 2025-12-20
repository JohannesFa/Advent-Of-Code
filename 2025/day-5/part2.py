#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

ranges = []    
ids = []

def contains(num, rangee: range):
    if num >= rangee.start and num <= rangee.stop:
        return True
    else:
        return False

def listNotContains(listt,value):
    if listt.count(value) == 0:
        return True
    else:
        return False

foundEmpty = False
for i in lines:
    item = i.strip()
    if foundEmpty == False:
        if item == "":
            foundEmpty = True
        else:
            lower, upper = map(int,item.split("-"))
            ranges.append(range(lower,upper))
    else:
        ids.append(int(item))

while True:
    removedIndeces = []
    newRanges = []
    for r1Index in range(len(ranges)):
        for r2Index in range(len(ranges)):
            if r1Index != r2Index and listNotContains(removedIndeces,r1Index) and listNotContains(removedIndeces,r2Index):
                r1 = ranges[r1Index]
                r2 = ranges[r2Index]
                if contains(r2.start, r1):
                    newRanges.append(range(r1.start,max(r2.stop,r1.stop)))
                    removedIndeces+=[r1Index,r2Index]

    keepOldRanges = []
    for rangeIndex in range(len(ranges)):
        if listNotContains(removedIndeces,rangeIndex):
            keepOldRanges.append(ranges[rangeIndex])
    if len(newRanges) == 0:
        break
    ranges = keepOldRanges + newRanges

rangeCoverCount = 0

for rangee in ranges:
    if rangee.start > rangee.stop:
        print("Bigger",rangee)
    rangeCoverCount += rangee.stop-rangee.start+1
print(rangeCoverCount)