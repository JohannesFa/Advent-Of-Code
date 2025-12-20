#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

startlocation = (None,None)
endlocation = (None,None)
walls = [] 
for ii in range(len(lines)):
    i = lines[ii]
    item = i.strip()
    for jj in range(len(i)):
        j = i[jj]
        if j == "#":
            walls.append((jj,ii))
        elif j == "S":
            startlocation = (jj,ii)
        elif j == "E":
            endlocation = (jj,ii)

historiclocations = []
directions = [(0,1),(1,0),(-1,0),(0,-1)]
currentlocations = [(0,0)]
while True:
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