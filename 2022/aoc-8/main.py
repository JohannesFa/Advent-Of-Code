import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
input = open('input.txt', 'r').readlines()
for i in range(len(input)):
    input[i] = input[i].strip()

listofvalues = []
dicofcords = {}
vis = {}
height = len(input)
width = len(input[0].strip())
#append all values to list
for i in range(len(input)):
    for j in range(len(input[i].strip())):
        dicofcords[f"{str(j)},{str(i)}"] = input[i].strip()[j]

totaltreesvis = 0

print(dicofcords)
print(width, height)
for yaxis in range(height):
    highestnum = -1
    for xaxis in range(width):
        currstr = f"{xaxis},{yaxis}"
        currentval = dicofcords[currstr]
        if int(currentval) > highestnum:
            highestnum = int(currentval)
            vis[currstr] = dicofcords[currstr]

for yaxis in range(height):
    highestnum = -1
    for xaxis in range(width):
        currstr = f"{width-xaxis-1},{yaxis}"
        currentval = dicofcords[currstr]
        if int(currentval) > highestnum:
            highestnum = int(currentval)
            vis[currstr] = dicofcords[currstr]

for xaxis in range(width):
    highestnum = -1
    for yaxis in range(height):
        currstr = f"{xaxis},{height-yaxis-1}"
        currentval = dicofcords[currstr]
        if int(currentval) > highestnum:
            highestnum = int(currentval)
            vis[currstr] = dicofcords[currstr]

for xaxis in range(width):
    highestnum = -1
    for yaxis in range(height):
        currstr = f"{xaxis},{yaxis}"
        currentval = dicofcords[currstr]
        if int(currentval) > highestnum:
            highestnum = int(currentval)
            vis[currstr] = dicofcords[currstr]


print(vis)
print(len(vis))