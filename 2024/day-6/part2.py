#By LazerK3
import os, time
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

print(len(lines))

#usedobstructions = []      
map1 = []
for i in lines:
    item = i.strip()
    map1.append(item)
    #usedobstructions.append("."*len(item))


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
def simulate(map):
    positionslist = []
    #global usedobstructions
    directions = [">","<","^","v"]
    rotdict = {">":"v", "v":"<", "<":"^","^":">"}
    offsetdict = {">": (1,0), "v": (0,1), "<":(-1,0),"^":(0,-1)}
    direction = None
    #map = replaceInMap(map, (39,-1),".")
    position = None

    for rowindex in range(len(map)):
            row = map[rowindex]
            for columnindex in range(len(row)):
                column = row[columnindex]
                if column in directions:
                    direction = column
                    position = (columnindex,rowindex)
                    map = replaceInMap(map,(columnindex,rowindex),"X")

    n = 0
    while n < 12000:
        n +=1
        #print(direction)
        nextposition = addcords(position,offsetdict[direction])
        if checkIfValidCord(map, nextposition) == False:
            return [map, n, positionslist,True]
        if map[nextposition[1]][nextposition[0]] == "#":
            map = replaceInMap(map, position,rotdict[direction])
            direction = rotdict[direction]
        else:
            map = replaceInMap(map, nextposition, direction)
            position = nextposition
            positionslist.append(nextposition)
    return [map,n,position,False]

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
directions = [">","<","^","v"]
t1 = time.time()

ValidLoopCounter = 0

for rowindex in range(len(map1)):
        row = map1[rowindex]
        for columnindex in range(len(row)):
            column = row[columnindex]
            if column not in directions and column != "#":
                print(columnindex, rowindex)
                #showMatrix(map1)
                dummymap, n, poslist, completed = simulate(replaceInMap(map1.copy(),(columnindex,rowindex),"#"))
                if completed == False:
                    ValidLoopCounter += 1


map1,n, positionslist, wowo = simulate(map1)
print(f"{n=}")
#showMatrix(map1)
#input("")
t2=time.time()
#showMatrix(map1)
unique = len(list(dict.fromkeys(positionslist)))
print(f"{unique=}")
#showMatrix(usedobstructions)
#print(positions)
print(f"time: {t2-t1}")
print(f"{ValidLoopCounter=}")