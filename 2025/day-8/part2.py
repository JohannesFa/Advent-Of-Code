#By LazerK3
import os
from typing import Set
from collections import OrderedDict
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()
targetConnections = 1000

class Cord:

    def __init__(self, x, y, z):
        self.x = x  # Instance attribute
        self.y = y  # Instance attribute
        self.z = z

    def __repr__(self) -> str:
        return str((self.x, self.y, self.z))

    def __eq__(self, other):
        return isinstance(other, Cord) and (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __str__(self):
        return str((self.x, self.y, self.z))

    def distance(self, c2):
        distance = ((self.x-c2.x)**2+(self.y-c2.y)**2+(self.z-c2.z)**2)**0.5
        return distance
    
    def isNotConnected(self,c2,connections):
        selftoc2 = connections[self]
        c2toself = connections[c2]
        if c2 in selftoc2 or self in c2toself:
            return False
        else:
            return True

def listListLen(listList):
    sum = 0
    for listItem in listList:
        sum += len(listItem)
    return sum

def findListListIndex(item,listList: list[list]):
    #print(len(listList))
    for listItemIndex in range(len(listList)):
        listItem = listList[listItemIndex]
        if item in listItem:
            return listItemIndex
    print("Megaerror")
    exit()
    


cordslist = []
circutlist = []

cordsConnectionDictonatry = {}
for i in lines:
    item = i.strip()
    cord = list(map(int,item.split(",")))
    cordObject = Cord(cord[0],cord[1],cord[2])
    cordslist.append(cordObject)
    circutlist.append([cordObject])
    cordsConnectionDictonatry[cordObject] = []



distancesDict: dict[frozenset[Cord],float] = {}
for cord1 in cordslist:
    for cord2index in range(len(cordslist)):
        cord2 = cordslist[cord2index]
        if cord1 != cord2:
            distancesDict[frozenset([cord1,cord2])] = cord1.distance(cord2)

d2 = dict(
    sorted(distancesDict.items(), key=lambda item: item[1])
)

#print(d2)
connections = 0


for pair in d2:
    activeDist = d2[pair]
    #print(f"Key: {pair} Value:{activeDist}")
    c1,c2 = pair
    c1ListListIndex = findListListIndex(c1,circutlist)
    c2ListListIndex = findListListIndex(c2,circutlist)
    #print("Length of listlist", listListLen(circutlist))
    
    
    if (c1ListListIndex != c2ListListIndex) and connections < targetConnections:
        
        #print(f"adding c1:{c1} c2:{c2} to circut {circutlist[c1ListListIndex]} and {circutlist[c2ListListIndex]} \n")
        #print("before", circutlist)
        circutlist[c1ListListIndex] += circutlist[c2ListListIndex]
        circutlist.pop(c2ListListIndex)
        if len(circutlist) == 1:
            print("Distance is ", c1.x*c2.x)
            exit()
        #print("after", circutlist[c1ListListIndex])
    #elif connections < 10:
        #print(f"sklipping c1:{c1} c2:{c2} to circut {circutlist[c1ListListIndex]}")
        #print()

    #connections += 1
#print(circutlist)
circutlength = []
for circut in circutlist:
    #print(len(circut))
    circutlength.append(len(circut))

circutlength = sorted(circutlength)

#circutlist.sort(key=len, reverse=True)
ans = circutlength[-1]*circutlength[-2]*circutlength[-3]
print("Answer:", ans)
#for circut in circutlist:
#    print(circut)
    
#print(len(circutlist))