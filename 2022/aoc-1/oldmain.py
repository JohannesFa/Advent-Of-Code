input = open("./input.txt", "r").readlines()

templist = []
listofthings = []


for line in input:
  if line == "\n":
    listofthings.append(templist)
    templist = []
  else:
    print(9)
    templist.append(int(str(line)))
    




newlist = []
for i in listofthings:
  temp = 0
  for j in i:
    temp += j

  newlist.append(temp)
    

newlist.sort()
print(newlist[-1] + newlist[-2] + newlist[-3])


