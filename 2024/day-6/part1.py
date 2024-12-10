#By LazerK3
import os, re, time
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

#usedobstructions = []      
map1 = []
for i in lines:
    item = i.strip()
    map1.append(item)
    #usedobstructions.append("."*len(item))


positions = {}
positionslist = []

def addcords(p1,p2):
    return(int(p1[0])+int(p2[0]),int(p1[1])+int(p2[1]))

def replaceInMap(map,cord,to):
    mapstring1 = map[cord[1]][:cord[0]]
    mapstring2 = map[cord[1]][(cord[0]+1):] 
    newsting = to.join([mapstring1,mapstring2])
    #print(f"Replacing from {map[cord[1]][cord[0]]} to {to} at {cord}")
    map[cord[1]] = newsting
    #showMatrix(map)
    return map
def takestep(map):
    global positions
    global positionslist
    #global usedobstructions
    directions = [">","<","^","v"]
    rotdict = {">":"v", "v":"<", "<":"^","^":">"}
    offsetdict = {">": (1,0), "v": (0,1), "<":(-1,0),"^":(0,-1)}
    direction = ""
    #map = replaceInMap(map, (39,-1),".")
    position = None
    #while True:
    for rowindex in range(len(map)):
        row = map[rowindex]
        for columnindex in range(len(row)):
            column = row[columnindex]
            if column in directions:
                direction = column
                position = (columnindex,rowindex)
                map = replaceInMap(map,(columnindex,rowindex),"X")
                
                positionslist.append((columnindex,rowindex))
    if direction != "":
        nextposition = addcords(position,offsetdict[direction])
        if checkIfValidCord(map, nextposition) == False:
            return [map, False]
        if map[nextposition[1]][nextposition[0]] == "#":
            map = replaceInMap(map, position,rotdict[direction])
            #usedobstructions = replaceInMap(usedobstructions, position, rotdict[direction])
        else:
            map = replaceInMap(map, nextposition, direction)
            positions[(columnindex,rowindex)] = 1
        
    else:
        print("WHat")
        exit()
    return [map, True]

def checkIfValidCord(mat,cord):
    x,y = cord
    xlen = len(mat[0])
    ylen = len(mat)
    if x < xlen and y < ylen and x >= 0 and y >= 0:
        return True
    else:
        return False   

def showMatrix(mat):
    print("")
    for ma in mat:
        print(ma)


t1 = time.time()
while True:
    map1, shouldContinue = takestep(map1)
    if shouldContinue == False:
        break
    #showMatrix(map1)
    #input("")
t2 = time.time()
showMatrix(map1)
#print(len(positions))
print(len(list(dict.fromkeys(positionslist))))
#showMatrix(usedobstructions)
#print(positions)

print(t2-t1)