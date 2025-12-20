#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

def calcArea(c1,c2):
    dx = c1[0]-c2[0]+1
    dy = c1[1]-c2[1]+1
    return dx*dy

biggestArea = 0
cords = []   
for i in lines:
    item = i.strip()
    x,y = item.split(",")
    cords.append([int(x),int(y)])


for cord1 in cords:
    for cord2 in cords:
        area = calcArea(cord1,cord2)
        if area > biggestArea:
            biggestArea = area

print(biggestArea)