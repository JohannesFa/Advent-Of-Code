input = open('input.txt', 'r').readlines()
p1, p2 = [], []
for i in range(0, len(input)):
  plit = 0
  if input[i] == '\n':
    p1 += input[:i]
    p2 += input[i+1:]
    break

numbers = int(p1.pop(-1).strip()[-1])
listofcrates = []
for i in p1:
    tempitem = i.strip().split(',')

    listofcrates.append(tempitem)
#turn the 2d array by 90 degrees clockwise 
def rotate90(listt):
    listt = list(zip(*listt[::-1]))
    return listt
listofstacks = rotate90(listofcrates)



#remove all empty items or all tripple spaced items from the 2d array, sicnce the list is 2d you ned a for loop within a for loop
newlist = []
for i in listofstacks:
    tlist = []
    for j in i:
        if j != '':
            tlist.append(j)

    newlist.append(tlist)

for line in newlist:
    print(line)
def move(amount, fromm, too, listt):
    itemtomove = []
    tempi = listt[fromm][-amount:]
    for i in tempi:
        itemtomove.append(i)
    
    print(f"moving {itemtomove} from {fromm} to {too} with {amount}")
    for i in range(0,amount):
        listt[fromm].pop(-1)
    print(f"moving {itemtomove} from {fromm} to {too}")
    for i in itemtomove:
        listt[too].append(i)
    # remove the itemtomove from the list
    print("Current list is;", )
    for line in listt:
        print(line)

    #append itemtomove to begginning of list
    return listt
liftofinsructions = []
for i in p2:
    #print(f"moving {i.strip().split(' ')[0]} from {i.strip().split(' ')[1]} to {i.strip().split(' ')[2]}")
    liftofinsructions.append(i.strip().split(' '))
inn = 0
for i in liftofinsructions:
    inn += 1
    print(f"step {inn}")
    new = move(int(i[0]), int(i[1])-1, int(i[2])-1, newlist)
    listofstacks = new

print("final")
stro = ""
for line in listofstacks:
    print(line)

print("Awnser: ")
print(listofstacks)
for line in listofstacks:
    stro += str(line[-1][1])

print("Answer might be:", stro)


