#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

nrOrSafeLevels = 0
for i in lines:
    item = i.strip()
    items = item.split(" ")
    dif = int(items[0])-int(items[1])
    if dif > 0:
        increasing = -1
    elif dif < 0:
        increasing = 1
    last = None
    safe = True
    for level in items:
        level = int(level)
        if last is not None:
            dif = (level-last)*increasing
            if dif > 3 or dif < 1:
                safe = False
        last = level
                
    if safe:
        nrOrSafeLevels+=1
        
print(nrOrSafeLevels)