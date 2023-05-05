#pylint: disable=consider-using-enumerate,missing-function-docstring,consider-using-dict-items,invalid-name
import os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
input = open('input.txt', 'r').read().split('\n')
currentdirectory = "base:"
directories = {'base:':0}
dirs = ['base:']

for i in input:
    values = i.split(' ')
    if values[0] == "$":
        if values[1] == "cd":
            if values[2] == "..":
                currentdirectory = "base:"
            else:
                currentdirectory += "^" + values[2]
                directories[currentdirectory] = 0
                dirs.append(currentdirectory)
        elif values[1] == "ls":
            pass
        else:
            print("Not expecten, input is:",values[1])
            exit()
    elif values[0] == "dir":
        pass
    else:
        tempdir = currentdirectory
        print(len(dirs))
        found = False
        for i in dirs:
                if found == False:

                    if i.split(' ')[0] == currentdirectory:
                        dirs[dirs.index(i)] = " ".join(i.split(' '))+ " " + str(values[0])
                        found = True

        if found == False:
            print("not found")
            exit()

            
        while len(tempdir.split("^")) >= 2:
            directories[tempdir] = directories[tempdir]+(int(values[0]))
            
            te = tempdir.split("^")
            tempdir = "^".join(te[:len(te)-1])


for i in range(len(dirs)):
    tem = dirs[i].split(' ')
    acc = 0
    for j in range(len(tem)):

        currentvalue = tem.pop(acc)
        if currentvalue in tem:
            pass
        else:
            tem.insert(acc,currentvalue)
            acc+=1
    print("tem =",tem)
    dirs[i] = " ".join(tem)

print(directories)
over = 0
for i in directories:
    print(i, directories[i])
    if directories[i] < 100000:
        over+= directories[i]
over2 = 0

for i in range(len(dirs)):
    teml = dirs[i].split(" ")
    teml2 = 0
    for j in teml[1:]:
        teml2 += int(j)
    tempdir = teml[0]
    print("Before appending dir is", tempdir, "and len is", len(tempdir.split('^')))
    while len(tempdir.split("^")) > 2:
        te = tempdir.split("^")
        tempdir = "^".join(te[:len(te)-1])
        print("Appending to lower direcotry", tempdir, "and the current list is", dirs)
        for j in range(len(dirs)):
            spl = dirs[j].split(' ')
            if spl[0] == tempdir and len(spl) > 1:
                spl[1] = str(int(spl[1])+int(teml2))
                dirs[j] = str(" ".join(spl))

for i in range(len(dirs)):
    teml = dirs[i].split(" ")
    teml2 = 0
    for j in teml[1:]:
        teml2 += int(j)

    if teml2 <= 100000:
        over2+= teml2
for i in directories:
    print(i)
print("Split here------------------------------------------------------------------------")
for i in dirs:
    print(i)
print("over is:", over)
print("over2 is:", over2)