#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()



disk = []  
fileid = 0
onFileBlock = True
for i in lines[0]:
    item = i.strip()
    
    if onFileBlock:
        for j in range(int(item)):
            disk.append(fileid)
    else:
        for j in range(int(item)):
            disk.append(".")
    #print(onFileBlock)
    if onFileBlock:
        onFileBlock = False
        fileid += 1
    else:
        onFileBlock = True

#print(disk)



current = len(disk)-1
for ii in range(len(disk)):
    i = disk[ii]
    if i == ".":
        while True:
            if disk[current] != ".":
                disk[ii], disk[current] = disk[current], disk[ii]
                current -=1
                break
            else:
                current -=1
    if ii >= current:
        break





#Compute p1 answer
answer = 0
for ii in range(len(disk)):
    i = disk[ii]
    if i == ".":
        break
    else:
        answer += ii*int(i)





#print(disk)
print(answer)