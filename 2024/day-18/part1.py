#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

size = 71
steps = 1024
xsize = size
ysize = size

def multiplycord(cord,mul):
    return (cord[0]*mul,cord[1]*mul)
def addCords(c1,c2):
    return (c1[0]+c2[0],c1[1]+c2[1])
def checkIfValidPosition(c,maxwidth, maxheight):
    if c[0]>=maxwidth or c[1]>=maxheight or c[0]<0 or c[1]<0:
        return False
    else:
        return True
def printpositions(positions, steppedpositions):
    global xsize
    global ysize
    bigstring = ""
    #print(positions)
    for j in range(ysize):
        for i in range(xsize):
            if (i,j) in positions:
                bigstring += "#"
            elif (i,j) in steppedpositions:
                bigstring += "O"
            else:
                bigstring+="."
        bigstring+="\n"
    print(bigstring)

cordinates = []    
for i in lines:
    item = i.strip()
    cords = item.split(",")
    cords = (int(cords[0]),int(cords[1]))
    cordinates.append(cords)
fallencordinates = []
for i in range(steps):
    fallencordinates.append(cordinates[i])

historiclocations = []
directions = [(0,1),(1,0),(-1,0),(0,-1)]
currentlocations = [(0,0)]
stepstaken = 0
while True:
    stepstaken+=1
    newlocations = []
    for location in currentlocations:
        for direction in directions:
            newdir = addCords(direction,location)
            if newdir == (xsize-1,ysize-1):
            #print(newlocations)
            #printpositions(fallencordinates,newlocations)
                print("exiting with", stepstaken, "steps")
                exit()
            if newdir not in currentlocations and newdir not in historiclocations and newdir not in newlocations and newdir not in fallencordinates and checkIfValidPosition(newdir,xsize,ysize):
                newlocations.append(newdir)
                
    historiclocations += currentlocations
    #printpositions(fallencordinates,newlocations)
    currentlocations = newlocations



print(fallencordinates)
#printpositions(fallencordinates)