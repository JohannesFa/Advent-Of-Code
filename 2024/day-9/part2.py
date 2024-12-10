#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("test2.txt", "r").readlines()

def showDisk(disk):
    for line in disk:
        print(line, end="")
    print()

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

showDisk(disk)


currentnumber = None
currentlength = 0
for numberindex in range(len(disk)-1,-1,-1):
    number = disk[numberindex]

    #sets currentnumber if none is assigned
    if currentnumber == None:
        if number != ".":
            currentnumber = number
            currentlength += 1
    else:
        if number == currentnumber:
            currentlength += 1
    
    if numberindex-1>=0 and disk[numberindex-1] != currentnumber and currentnumber != None:
        #Has identified a sequence of numbers to be moved
        #look for free space
        #print(f"Sequence is {currentlength} of {currentnumber}")
        dotcounter = 0
        for characterindex in range(len(disk)):
            if characterindex >= numberindex:
                break
            else:
                character = disk[characterindex]
                if character == ".":
                    dotcounter += 1
                else:
                    dotcounter = 0
                if dotcounter == currentlength:
                    #print(dotcounter)
                    for replaceindex in range(dotcounter):
                        replacedottonum = characterindex-dotcounter+replaceindex+1
                        replacenumtodot = numberindex+replaceindex
                        disk[replacedottonum], disk[replacenumtodot] = disk[replacenumtodot], "."
                    #print(disk)
                    break
        currentnumber = None
        currentlength = 0
        showDisk(disk)


    
    

#Compute p1 answer
answer = 0
for ii in range(len(disk)):
    i = disk[ii]
    if i == ".":
        pass
    else:
        answer += ii*int(i)





showDisk(disk)
print(answer)