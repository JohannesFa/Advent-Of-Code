import os,sys
input = open("input.txt", "r").read().splitlines()

def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    sys.stdout = sys.__stdout__


blockPrint()
cords = []

headpos = [0, 0]
tailpos = [0, 0]
relpos = [0, 0]

up = [0,1]
down = [0,-1]
left = [-1, 0]
right = [1,0]

def addvec(vec1,vec2):
    newvec = [vec1[0] + vec2[0], vec1[1] + vec2[1]]
    return newvec

def subvec(vec1,vec2):
    newvec = [vec1[0] - vec2[0], vec1[1] - vec2[1]]
    return newvec

def clamp(num):
    if num > 1:
        num = 1
        print("clamped")
    elif num < -1:
        num = -1
        print("clamped")

    return num

def clampvec(vec):
    x = vec[0]
    y = vec[1]

    xnew = clamp(x)
    ynew = clamp(y)
    if  xnew != x:
        ynew = 0
    elif ynew != y:
        xnew = 0

    print("clampedvec")
    print(x)
    print(y)
    return [xnew, ynew]



for i in range(len(input)):
    input[i] = input[i].strip().split(" ")



for i in range(len(input)):
    move = input[i][0]
    amount = int(input[i][1])

    if move == "U":
        movevec2 = up
    elif move == "D":
        movevec2 = down
    elif move == "L":
        movevec2 = left
    elif move == "R":
        movevec2 = right

    
    
    for i in range(amount):
        print("\nBefore")
        headpos = addvec(headpos,movevec2)
        print("headpos")
        print(headpos)
        print("tailpos")
        print(tailpos)
        relpos = subvec(headpos,tailpos)
        print("relpos")
        print(relpos)
        relpos = clampvec(relpos)
        print("relpos after clamp")
        print(relpos)
        tailpos = subvec(headpos,relpos)
        print("tailpos")
        print(tailpos)
        cords.append(tailpos)


#remove all duplicates from cords list wihtout unhashable type error or using cords = list(dict.fromkeys(cords))

cords = [i for n, i in enumerate(cords) if i not in cords[n + 1:]]


enablePrint()
if [0,0] in cords:
    print("yes")
print(len(cords))


    
