import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
input = open('input.txt', 'r').readlines()
test = False
if test:
    input = open('testinput.txt', 'r').readlines()
for i in range(len(input)):
    input[i] = input[i].strip()

height = len(input)-2
width = len(input[0])-2

print("Height is ", height , "Width is ", width)

input = input[1:height+1]
for i in range(len(input)):
    input[i] = input[i][1:width+1]

blizzards = []

for i in range(height):
    blizzards.append([])
    for j in range(width):
        blizzards[i].append([input[i][j]])




def addvec(vec1, vec2):
    return(vec1[0]+ vec2[0], vec1[1], vec2[1])
def limitvec(vec):
    global width
    global height
    return [vec[0]%width, vec[1]%height]

arrowdic = {">": [1,0], "<": [-1,0], "^":[0,1], "v":[0,-1]}



def sim(bliz):
    itemoffset = 0

    newarr = []
    global height
    global width
    for i in range(height):
        newarr.append([])
        for j in range(width):
            newarr[i].append([])



    bliz = list(bliz)
    for row in range(len(bliz)):
        rowitem = bliz[row]
        for column in range(len(rowitem)):
            columnitem = rowitem[column]
            for item in range(len(columnitem)):
                itemitem =  bliz[row][column][item-itemoffset]
                if itemitem != ".":
                    vec2d = arrowdic[itemitem]
                    cords = [column, row]
                    newcords = addvec(vec2d, cords)
                    newcords = limitvec(newcords)
                    
                    newarr[newcords[1]][newcords[0]].append(itemitem)
            itemoffset=0

    return newarr

blizzards = sim(blizzards)





print("")
for i in blizzards:
    for j in i:
        if len(j) > 1:
            print(len(j), end="")
        elif len(j) != 0:
            print(j[0], end="")
        else:
            print(".", end="")
    print("")

"""
for line in input:
    print(line)
"""