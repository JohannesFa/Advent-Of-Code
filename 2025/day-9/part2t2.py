#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

def flipIfReverseRange(r1):
    if r1.start > r1.stop:
        r1 = range(r1.stop,r1.start)
        return r1
    return r1

def isInterSectingRange(r1:range,r2:range):
    r1 = flipIfReverseRange(r1)
    r2 = flipIfReverseRange(r2)

    if r2.start in r1:
        return True
    elif r1.start in r2:
        return True
    return False

def inRangeExcludingEdges(r1,n):
    r2 = range(r1.start+1,r1.stop)
    return n in r2

class Cord:

    def __init__(self, x, y):
        self.x: int = x 
        self.y: int = y  

    def __repr__(self) -> str:
        return str((self.x, self.y))

    def __eq__(self, other):
        return isinstance(other, Cord) and (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return str((self.x, self.y))
   
class CordRange:
    def __init__(self, c1: Cord, c2: Cord):
        self.c1 = c1 
        self.c2 = c2 

    def YRange(self):
        if self.c1.x == self.c2.x:
            return True
        elif self.c1.y == self.c2.y:
            return False
        else:
            print("Gigga error")
            exit()

    def intersectsWithSquare(self,p1,p2):
        if self.YRange():
            if isInterSectingRange(range(self.c1.y,self.c2.y),range(p1.y,p2.y)):
                squarerangeX = range(p1.x,p2.x)
                squarerangeX = flipIfReverseRange(squarerangeX)
                if inRangeExcludingEdges(squarerangeX,self.c1.x):
                    return True 
        else:
            if isInterSectingRange(range(self.c1.x,self.c2.x),range(p1.x,p2.x)):
                squarerangeY = range(p1.y,p2.y)
                squarerangeY = flipIfReverseRange(squarerangeY)
                if inRangeExcludingEdges(squarerangeY,self.c1.y):
                    return True
        return False

            

    #def cordOnRange(self,cord):
    #    if self.YRange():
    #        if cord.x == self.c1.x:
    #            if cord.y in range(self.c1.y, self.c2.y):
    #                return True
    #    else:
    #        if cord.y == self.c1.y:
    #            if cord.x in range(self.c1.y, self.c2.y):
    #                return True
    #    return False

print("Teststart \n")

cr1 = CordRange(Cord(10,20),Cord(20,20))
print("Yrange: ",cr1.YRange())
print("Intersecting",cr1.intersectsWithSquare(Cord(22,15),Cord(7,28)))

print("Teststart \n")

def calcArea(c1,c2):
    dx = abs(c1.x-c2.x)+1
    dy = abs(c1.y-c2.y)+1
    return dx*dy

def otherRangesInside(p1,p2,rangeList:list[CordRange]):
    for cordRange in rangeList:
        if cordRange.intersectsWithSquare(p1,p2):
            return True
    return False


def otherPointsInside(p1,p2, cordsList):
    p1x = p1.x
    p2x = p2.x
    p1y = p1.y
    p2y = p2.y
    if p1x > p2x:
        p1x,p2x = p2x,p1x
    if p1y > p2y:
        p1y,p2y = p2y,p1y
    xrange = range(p1x+1, p2x)
    yrange = range(p1y+1, p2y)
    for cord in cordsList:
        if cord.x in xrange and cord.y in yrange:
            return True
    return False

biggestArea = 0
biggestAreaCords = []
cords = []   
for i in lines:
    item = i.strip()
    x,y = item.split(",")
    cords.append(Cord(int(x),int(y)))

cordRanges = []

for cordIndex in range(1,len(cords)-1):
    c1 = cords[cordIndex-1]
    c2 = cords[cordIndex+0]
    c3 = cords[cordIndex+1]

    cordRanges.append(CordRange(c1,c2))
    cordRanges.append(CordRange(c2,c3))

cordRanges.append(CordRange(cords[0],cords[1]))


for cord1 in cords:
    for cord2 in cords:
        area = calcArea(cord1,cord2)
        if area > biggestArea and not otherRangesInside(cord1,cord2,cordRanges):
            biggestArea = area
            biggestAreaCords = [cord1,cord2]

print(biggestArea)
print(biggestAreaCords)