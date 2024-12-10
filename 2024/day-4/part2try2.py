#By LazerK3
import os, re
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()
acords = []
matrix = []
for i in range(len(lines)):
    item = lines[i].strip()
    matrix.append(item)
    for j in range(len(item)):
        char = item[j]
        if char == "A":
            acords.append([j,i])

def grabCord(mat, x,y):
    return mat[y][x]
def checkIfValidCord(mat,x,y):
    xlen = len(mat[0])
    ylen = len(mat)
    if x < xlen and y < ylen:
        return True
    else:
        return False

def addcords(c1,c2):
    return [c1[0]+c2[0],c1[1]+c2[1]]
offsets = [[-1,-1],[-1,1],[1,-1],[1,1]]

counter = 0

for cord in acords:
    mcount = 0
    scount = 0
    items = []
    for offset in offsets:
        checkcord = addcords(cord,offset)
        if checkIfValidCord(matrix,checkcord[0],checkcord[1]):
            item = grabCord(matrix,checkcord[0],checkcord[1])
            items.append(item)
            if item == "M":
                mcount+=1
            elif item == "S":
                scount+=1
    
    if len(items) == 4 and items[0] != items[3]:
        if mcount == 2 and scount == 2:
            counter+=1

print(counter)