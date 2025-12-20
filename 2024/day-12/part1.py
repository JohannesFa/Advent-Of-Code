#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()
mapsdict = {}
mapscorddict = {}
fillcharacter = "."
directions = [(0,1),(1,0),(-1,0),(0,-1)]

for i in lines:
    item = i.strip()
    for j in item:
        if j not in mapsdict.keys():
            mapsdict[j]=[]
            mapscorddict[j]=[]

def checkIfValidPosition(c,maxwidth, maxheight):
    if c[0]>=maxwidth or c[1]>=maxheight or c[0]<0 or c[1]<0:
        return False
    else:
        return True
    
def addCords(c1,c2):
    return (c1[0]+c2[0],c1[1]+c2[1])

def floodFill(map,cord):
    global fillcharacter
    global directions

    width = len(map[0])
    height = len(map)

    foundcordinates = [cord]
    shouldcontinue = True
    while shouldcontinue:
        currentfoundcords = []
        for basecord in foundcordinates:
            for direction in directions:
                activecord = addCords(direction,basecord)
                if checkIfValidPosition(activecord,width,height):
                    checkletter = map[activecord[1]][activecord[0]]
                    #print(checkletter)
                    if checkletter != fillcharacter:
                        if activecord not in foundcordinates and activecord not in currentfoundcords:
                            currentfoundcords.append(activecord)
        if len(currentfoundcords) == 0:
            shouldcontinue = False
        else:
            foundcordinates+=currentfoundcords
    return foundcordinates




for ii in range(len(lines)):
    i = lines[ii]
    item = i.strip()
    keys = mapsdict.keys()
    for letter in mapsdict:
        #print(mapsdict)
        mapsdict[letter].append([])
    for jj in range(len(item)):
        j = item[jj]
        activeletter = j
        mapsdict[activeletter][-1].append(activeletter)
        mapscorddict[activeletter].append((jj,ii))
        for notactiveletter in keys:
            if notactiveletter != activeletter:
                mapsdict[notactiveletter][-1].append(".")
areas = []
for mapkey in mapsdict:
    print(mapkey)
    currendcords = mapscorddict[mapkey].copy()
    
    while len(currendcords) != 0:
        foundarea = floodFill(mapsdict[mapkey],currendcords[0])
        print(currendcords)
        for cord in foundarea:
            print(cord)
            currendcords.remove(cord)
        areas.append(foundarea)

price = 0

for area in areas:
    areaarea = len(area)
    print(f"area is: {areaarea}")
    perimeter = 0
    for cord in area:
        for direction in directions:
            activecord = addCords(cord,direction)
            if activecord not in area:
                perimeter += 1
    price+=areaarea*perimeter

for mapkey in mapsdict:
    for line in mapsdict[mapkey]:
        for letter in line:
            print(letter, end="")
        print("")
    print("\n")



#print(floodFill(mapsdict["I"],(4,0)))
#print(floodFill(mapsdict["I"],mapscorddict["I"][3]))
#print(len(areas))
print(price)