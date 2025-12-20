#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

lookforip1 = True
ip1 = []
ip2 = []

def checkIfValidPosition(c,maxwidth, maxheight):
    if c[0]>=maxwidth or c[1]>=maxheight or c[0]<0 or c[1]<0:
        return False
    else:
        return True
    
def addCords(c1,c2):
    return (c1[0]+c2[0],c1[1]+c2[1])

def displaywarehouse(boxes,walls,robotlocation,ip1):
    width = len(ip1[0])
    height = len(ip1)
    for y in range(height):
        for x in range(width):
        
            if (x,y) in boxes:
                print("O", end="")
            elif (x,y) in walls:
                print("#", end="")
            elif (x,y) == robotlocation:
                print("@", end="")
            else:
                print(".", end="")
        print("")

for i in lines:
    item = i.strip()
    if lookforip1:
        if item == "":
            lookforip1 = False
        else:
            ip1.append(item)
    else:
        ip2.append(item)
ip2 = "".join(ip2)
#print(ip1)
inputmap = {">": (1,0), "<": (-1,0), "^":(0,-1), "v": (0,1)}
walls = []
boxes = []
robotlocation = (None,None)
for rowindex in range(len(ip1)):
    row = ip1[rowindex]
    for itemindex in range(len(row)):
        item = row[itemindex]
        if item == "#":
            walls.append((itemindex,rowindex))
        elif item == "O":
            boxes.append((itemindex,rowindex))
        elif item == "@":
            #print(itemindex,rowindex)
            robotlocation = (itemindex,rowindex)

displaywarehouse(boxes,walls,robotlocation,ip1)
for move in ip2:
    #print("\n")
    #print(move)
    movecords = inputmap[move]
    newrobotlocation = addCords(robotlocation,movecords)
    #print(f"Old pos: {robotlocation} new: {newrobotlocation}")
    if newrobotlocation not in boxes and newrobotlocation not in walls:
        robotlocation = newrobotlocation
    elif newrobotlocation in boxes:
        boxlocation = newrobotlocation
        while True:
            newboxlocation = addCords(movecords,boxlocation)
            if newboxlocation not in boxes:
                if newboxlocation not in walls:
                    robotlocation = newrobotlocation
                    #print(newrobotlocation)
                    #print(boxes)
                    boxes.remove(newrobotlocation)
                    boxes.append(newboxlocation)
                    break
                else:
                    
                    break
            else:
                boxlocation = newboxlocation
    #displaywarehouse(boxes,walls,robotlocation,ip1)
#print(ip1,ip2)
sumofboxgps = 0
for box in boxes:
    sumofboxgps += box[0]+box[1]*100
#displaywarehouse(boxes,walls,robotlocation,ip1)
print(sumofboxgps)