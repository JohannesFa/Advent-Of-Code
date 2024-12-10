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

tobeordered = []

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
                        #print(n1,n2,pagesnotyetused)
                        active = False
                        invalidcounter += 1
            #print(pagesnotyetused,page)
            pagesnotyetused.remove(page)

        
    if active:
        num = int(pages[int((len(pages)-1)/2)])
        #print(f"Num {num}")
        total += num
    else:
        tobeordered.append(pageset)

def checkIfOrdered(pages):
    global inputp1
    active = True
    pages
    pagesnotyetused = pages.copy()
    for page in pages:
        if active:
            for comparison in inputp1:
                n2,n1 = comparison.split("|")
                if n1==page:
                    if n2 in pagesnotyetused and active == True:
                        #print(n1,n2,pagesnotyetused)
                        return [False, n1,n2]
                        active = False
            #print(pagesnotyetused,page)
            pagesnotyetused.remove(page)

    return [True,None,None]
ordered = []

p2total = 0

for pageset in tobeordered:
    pages = pageset.split(",")
    done = False
    while not done:
        done, n1,n2 = checkIfOrdered(pages)
        if done:
            break
        n1p, n2p = pages.index(n1),pages.index(n2)
        pages[n1p], pages[n2p] = pages[n2p], pages[n1p]

    ordered.append(pages)
    num = int(pages[int((len(pages)-1)/2)])
    #print(f"Num {num}")
    p2total += num

#print(ordered)
print(p2total)