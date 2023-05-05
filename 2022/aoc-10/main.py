text = open("input1.txt", "r").readlines()
import math
x = 1
cycel = -1

pixels = []
for i in range(6):
    pixels.append([])
    for j in range(40):
        pixels[i].append([])
for i in pixels:
    print(i)
anses = []
def check(cycel, x):
    global anses
    global pixels
    rowindex = cycel%40
    row = math.floor(cycel/40)
    if row < 6:
        value = ""
        if x ==rowindex or x-1 ==rowindex or x+1 ==rowindex:
            value = "#"
        else:
            value = "."
        print(row, rowindex)
        pixels[row][rowindex] = value

    
o = 1
for i in text:
    print(o)
    o += 1
    if "noop" in i:
        operation = "noop"
    else:
        i = i.strip()
        operation,num = i.split(" ")
        num = int(num) 
    if operation == "addx":
        cycel+=1
        check(cycel, x)
        cycel+=1
        
        check(cycel,x)
        x+=num

    elif operation == "noop":
        cycel+=1
        check(cycel,x)
    else:
        print("failed")
        exit()
    
print(" ",)
for i in pixels:
    for j in i:
        print(j, end="")
    print("")