#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()
            
order = [0,1,2,3,4,5,6,7,8,9]




map = []
for i in lines:
    item = i.strip()
    map.append([])
    for j in item:
        map[-1].append(int(j))


maxheight = len(map)
maxwidth = len(map[0])

def addcords(c1,c2):
    return (c1[0]+c2[0],c1[1]+c2[1])
def checkIfValidPosition(c):
    if c[0]>=maxwidth or c[1]>=maxheight or c[0]<0 or c[1]<0:
        return False
    else:
        return True

roots = []
for y in range(len(map)):
        yitem = map[y]
        for x in range(len(yitem)):
            xitem = yitem[x]
            if xitem == 0:
                roots.append((x,y))

directions = [(1,0),(0,1),(-1,0),(0,-1)]

score = 0
#print(f"Have roots {roots}")
for rootindex in range(len(roots)):
    root = roots[rootindex]
    newPositions = [root]
    for currentnumber in range(1,10):
        #print(f"\nBeggining with level {currentnumber}: ")
        positionsFound = []
        for position in newPositions:
            for direction in directions:
                    #print(position, direction)
                    testposition = addcords(position,direction)
                    if checkIfValidPosition(testposition) and testposition:
                        if map[testposition[1]][testposition[0]] == currentnumber:
                            positionsFound.append(testposition)
                            #print(f"Found match at {testposition} with value {map[testposition[1]][testposition[0]]} against {currentnumber}")
        newPositions = positionsFound
    score+=len(newPositions)

#print(newPositions)
print(score)
