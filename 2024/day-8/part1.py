#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

def addcords(c1,c2):
    return (c1[0]+c2[0],c1[1]+c2[1])
def subtractcord(c1,c2):
    return (c1[0]-c2[0],c1[1]-c2[1])
frequencies = {}   
for lineindex in range(len(lines)):
    i = lines[lineindex]
    item = i.strip()
    for charindex in range(len(item)):
        char = item[charindex]
        if char != ".":
            if char not in frequencies:
                #print(char, frequenzies)
                frequencies[char] = [(charindex,lineindex)]
            else:
                #print(char, frequenzies)
                frequencies[char].append((charindex,lineindex))

antinodes = []
#print(frequencies)
for frequencykey in frequencies:
    frequency = frequencies[frequencykey]
    for cord in frequency:
        withoutcurrentcordlist = frequency.copy()
        withoutcurrentcordlist.remove(cord)
        for cord2 in withoutcurrentcordlist:
            #print(cord, cord2)
            differnece = subtractcord(cord2,cord)
            #print(differnece)
            n1 = addcords(cord2,differnece)
            n2 = subtractcord(cord,differnece)
            antinodes.append(n1)
            antinodes.append(n2)

antinodemap = []

#print(antinodes)
counter = 0
for ii in range(len(lines)):
    i = lines[ii].strip()
    antinodemap.append([])
    for j in range(len(i)):
        if (j,ii) in antinodes:
            antinodemap[-1].append("#")
            counter+= 1
            #print("#")
        else:
            antinodemap[-1].append(".")

for i in antinodemap:
    print(i)

print(counter)