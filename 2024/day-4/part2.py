#By LazerK3
import os, re
os.chdir(os.path.dirname(__file__))
lines = open("test.txt", "r").readlines()

fw = []    
bw = []    
for i in lines:
    item = i.strip()
    fw.append(item)
    bw.append(item[::-1])

def condence(mat):
    condencedmat = []
    for line in mat:
        tempstring = ""
        for item in line:
            tempstring += item
        condencedmat.append(tempstring)
    return condencedmat

def showMatrix(mat):
    print("")
    mat = condence(mat)
    for ma in mat:
        print(ma)
    
def grabCord(mat, x,y):
    return mat[y][x]

def checkIfValidCord(mat,x,y):
    xlen = len(mat[0])
    ylen = len(mat)
    if x < xlen and y < ylen:
        return True
    else:
        return False

def rotate45(mat):
    rotatedmat = []
    for i in range(max(len(mat),len(mat[0]))*2-1): #Goes trough the longest diagonal
        rotatedmat.append([])
        for j in range(i+1):
            x=j
            y=i-j
            if checkIfValidCord(mat,x,y):
                rotatedmat[-1].append(grabCord(mat,x,y))
    return rotatedmat
lru = rotate45(fw)
rlu = rotate45(bw)



def mirror(mat):
    mirrored = []
    for line in mat:
        mirrored.append(line[::-1])
    return mirrored

def count(mat):
    total = 0
    for line in mat:
        total += len(line)
    return total

rld = mirror(lru)
lrd = mirror(rlu)


def rotate90(mat):
    rotated = []
    for i in range(len(mat[0])):
        rotated.append([])
        for j in range(len(mat)):
            rotated[-1].append(mat[j][i])
    return rotated
down = rotate90(fw)
up = mirror(down)



if True:
    #showMatrix(fw)
    #showMatrix(bw)
    showMatrix(lru)
    showMatrix(rld)
    showMatrix(rlu)
    showMatrix(lrd)
    #showMatrix(down)
    #showMatrix(up)



listsofrotations = [fw,bw,condence(lru),condence(rld),condence(rlu),condence(lrd),condence(down),condence(up)]

xmascounter = 0
for rotation in listsofrotations:
    for dimension in rotation:
        dimension = str(dimension)
        xmascounter+= dimension.find("XMAS")
        


#print(xmascounter)

nlocationcounts = {}
listsofrotationsforp2 = [[condence(lru),"lru"],[condence(rld),"rld"],[condence(rlu),"rlu"],[condence(lrd),"lrd"]]
for rotationindex in range(len(listsofrotationsforp2)):
    rotation = listsofrotationsforp2[rotationindex][0]
    rotationchange = listsofrotationsforp2[rotationindex][1]
    for dimensionindex in range(len(rotation)):
        dimension = rotation[dimensionindex]
        for match in re.finditer("XMAS", dimension):
            xrot =  match.start(0)+1
            xmax = len(fw[0])-1
            ymax = len(fw)-1
            x = (dimensionindex+xrot)/2
            y = dimensionindex-xrot
            if rotationchange == "lrd":
                pass
            elif rotationchange == "rld":
                x = xmax-x
            elif rotationchange == "lru":
                y = ymax-y
            elif rotationchange == "rlu":
                x = xmax-x
                y = ymax-y

            cord = (float(x),float(y), rotationchange)
            if cord in nlocationcounts:
                nlocationcounts[cord] = nlocationcounts[cord] + 1
            else:
                nlocationcounts[cord] = 1

xmascounterp2 = 0
for key in nlocationcounts:
    if nlocationcounts[key] == 2:
        xmascounterp2+=1

print(nlocationcounts)
print(len(nlocationcounts))
print(xmascounterp2)

