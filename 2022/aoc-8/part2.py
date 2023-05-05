#pylint: disable=consider-using-dict-items
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
input = open('input2.txt', 'r').readlines()
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
        dicofcords[f"{str(j)},{str(i)}"] = int(input[i].strip()[j])


print(dicofcords)

for y in range(len(input)):
    for x in range(len(input[y])):
        print("----")
        resultdown = 0
        for changer in range(y+1, height):
            if changer != height:
                resultdown +=1
                if int(input[changer][x]) >= int(input[y][x]):
                    print("break with val ",str(input[changer][x]),str(input[y][x]))
                    break
                else:
                    print("continue with val ",str(input[changer][x]),str(input[y][x]))
        print(resultdown, "at cordinates", y,x)
        print("----")
        resultup = 0
        for changer in reversed(range(y+1, height)):
            if changer != height:
                resultup +=1
                if int(input[changer][x]) >= int(input[y][x]):
                    print("break with val ",str(input[changer][x]),str(input[y][x]))
                    break
                else:
                    print("continue with val ",str(input[changer][x]),str(input[y][x]))
        print(resultup, "at cordinates", y,x)

