#pylint: disable=consider-using-enumerate
import os, sys
sys.setrecursionlimit(10000)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
input = open('input.txt', 'r').readlines()
currdir = ""
sumsize = 100000
sumsofoversize = 0
directories = []
default_dir = ""
def change_dir(path, currdir):
    if path == "..":
        currdir = default_dir
    else:
        if path != "/":
            currdir += " " + path
    return path


for i in range(0, len(input)):
    input[i] = input[i].strip()
    if input[i].startswith('$ cd'):
        input[i] = input[i].replace('$ cd ', '')
        currdir = change_dir(input[i], currdir)
        #directories.append(currdir)
    elif input[i].startswith('$ ls'):
        input[i] = input[i].replace('$ ls ', '')
        hasFoundAll = False
        numAhead = 0
        listoffoundfiles = []
        while hasFoundAll is not True:
            numAhead += 1
            if i + numAhead >= len(input):
                hasFoundAll = True
                break
            if input[i + numAhead].startswith('$'):
                hasFoundAll = True
                break
            elif input[i + numAhead].startswith('dir'):
                currdir += " " + ("" + input[i + numAhead].replace('dir ', '').strip())
                pass
            else:

                listoffoundfiles.append(input[i + numAhead].strip().split(' '))
        if len(listoffoundfiles) > 0:
            listofnums = []
            for i in listoffoundfiles:
                listofnums.append(i[0])
            listofnums.insert(0, currdir)
            directories.append(listofnums)
listofnames = []
print(directories)
"""
for i in range(0, len(directories)):
    listofnames.append(directories[i][0])
for i in range(0, len(directories)):
    for j in range(0, len(listofnames)):
        print(directories[i][0])
        if directories[i] == listofnames[j]:
            items = directories[i][1:]
            print(items)
            for k in items:
                    directories[i].append(k)
            directories.pop(i)
"""
def getotherpoints(littlelist):
    n = littlelist[0].split(' ')
    n = n[1:]
    for i in n:
        for j in range(len(directories)):
             if len(directories[j][0].split(' ')) != 1:
                if directories[j][0].split(' ')[0] == littlelist[0].split(' ')[0] or directories[j][0].split(' ')[1] == littlelist[0].split(' ')[1] or directories[j][0].split(' ')[0] == littlelist[0].split(' ')[1] or directories[j][0].split(' ')[1] == littlelist[0].split(' ')[0]:
                    print("overlapping", directories[j][0].split(' ')[0], "with", littlelist[0].split(' ')[0])
                else:
                    print("getting other points for", directories[j][0].split(' '), "and other is ", littlelist[0].split(' '))
                    getotherpoints(directories[j])
             if directories[j][0].split(' ')[0] == i:
                for k in directories[j][1:]:
                    littlelist.append(k)
                    print("appended", k, "to", littlelist[0])
    return littlelist
            



print(directories)
for i in directories:
    if len(i[0].split(' ')) != 1:
        i = getotherpoints(i)
    tempsum = 0
    for j in range(1, len(i)):
        tempsum += int(i[j])
    if tempsum <= sumsize:
        sumsofoversize += tempsum



print(sumsofoversize)