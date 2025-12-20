#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("tinput.txt", "r").readlines()

ranges = []    
ids = []

def contains(num, rangee: range):
    if num >= rangee.start and num <= rangee.stop:
        return True
    else:
        return False


foundEmpty = False
for i in lines:
    item = i.strip()
    if foundEmpty == False:
        if item == "":
            foundEmpty = True
        else:
            lower, upper = map(int,item.split("-"))
            ranges.append(range(lower,upper))
    else:
        ids.append(int(item))


freshCounter = 0

for idd in ids:
    for rangee in ranges:
        print(f"{idd:} {rangee:}")
        if contains(idd,rangee):
            print("Passed")
            freshCounter += 1
            break
print(ids)
print(freshCounter)



