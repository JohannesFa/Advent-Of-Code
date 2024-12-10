#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("samuelinput.txt", "r").readlines()

def checkIfUnsafe(items):
    last = None
    for i in range(len(items)):
        dif = int(items[0])-int(items[1])
        if dif > 0:
            increasing = -1
            break
        elif dif < 0:
            increasing = 1
            break
        else:
            return 1
    unsafetimes = 0
    for level in items:
        level = int(level)
        if last is not None:
            dif = (level-last)*increasing
            if dif > 3 or dif < 1:
                unsafetimes += 1
        last = level
    return unsafetimes

nrOrSafeLevels = 0
for i in lines:
    isBad = True
    item = i.strip()
    items = item.split(" ")
    verisions = []
    for j in range(len(items)):
        current = []
        for k in range(len(items)):
            if k != j:
                current.append(items[k])
            
        verisions.append(current)
    for versions in verisions:
        if checkIfUnsafe(versions) == 0:
            nrOrSafeLevels += 1
            isBad = False
            break
    if isBad:
        #print(items)
        #print(verisions)
        pass
    #unsafetimes2 = checkIfUnsafe(items[1:])


    #if unsafetimes <= 1 :
    #    nrOrSafeLevels+=1
    #else:
    #    print(item)
        
print(nrOrSafeLevels)