#By LazerK3
import os, numpy as np
os.chdir(os.path.dirname(__file__))
lines = open("tinput.txt", "r").readlines()


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
        if c1.x == c2.x:
            return True
        elif c1.y == c2.y:
            return False
        else:
            print("Gigga error")
            exit()


    def cordOnRange(self,cord):
        if self.YRange():
            if cord.x == self.c1.x:
                if cord.y in range(self.c1.y, self.c2.y):
                    return True
        return False

    
        


def calcArea(c1,c2):
    dx = c1[0]-c2[0]+1
    dy = c1[1]-c2[1]+1
    return dx*dy

cords = []   
for i in lines:
    item = i.strip()
    x,y = item.split(",")
    cords.append(Cord(int(x),int(y)))

cordRanges = []

cordsWrapped: list[Cord] = cords + [cords[0]]
p1 = 0
p2 = 0
print(cordsWrapped)
for cordIndex in range(1,len(cordsWrapped)):
    c1 = cordsWrapped[cordIndex-1]
    c2 = cordsWrapped[cordIndex+0]
    print(c1)
    p1 += c1.x*c2.y
    p2 -= c2.x*c1.y

print("Area is ", (p1+p2)/2)

#for cordIndex in range(1,len(cords)-1):
#    c1 = cords[cordIndex-1]
#    c2 = cords[cordIndex+0]
#    c3 = cords[cordIndex+1]
#
#    cordRanges.append(CordRange(c1,c2))
#    cordRanges.append(CordRange(c2,c3))

