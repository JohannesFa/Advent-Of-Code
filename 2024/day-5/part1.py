#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

inputp1 = []
inputp2 = []
midway = False
for i in lines:
    item = i.strip()
    if item == "":
        midway = True
        continue
    if midway:
        inputp2.append(item)
    else:
        inputp1.append(item)

total = 0
invalidcounter = 0

for pageset in inputp2:
    active = True
    pages = pageset.split(",")
    pagesnotyetused = pages.copy()
    for page in pages:
        if active:
            for comparison in inputp1:
                n2,n1 = comparison.split("|")
                if n1==page:
                    if n2 in pagesnotyetused and active == True:
                        print(n1,n2,pagesnotyetused)
                        active = False
                        invalidcounter += 1
            #print(pagesnotyetused,page)
            pagesnotyetused.remove(page)

        
    if active:
        num = int(pages[int((len(pages)-1)/2)])
        print(f"Num {num}")
        total += num

print(total)
print(invalidcounter)
print(len(inputp2))