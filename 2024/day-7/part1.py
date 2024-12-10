#By LazerK3
import os,math, threading
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()
threads = []
total = 0 

def checkIfValid(item):
    global total
    targetnumber, numbers = item.split(": ")
    targetnumber = int(targetnumber)
    numberslist = numbers.split(" ")
    currentitems = [int(numberslist[0])]
    for iindex in range(len(numberslist)-1):
        newitems = []
        for currentitem in currentitems:
            nextitem = int(numberslist[iindex+1])
            newitems.append(currentitem*nextitem)
            newitems.append(currentitem+nextitem)
            newitems.append(int(str(currentitem)+str(nextitem)))
        currentitems = newitems
    #print(currentitems, targetnumber)
    if targetnumber in currentitems:
        total += targetnumber

for i in lines:
    item = i.strip()
    
    threads.append(threading.Thread(target=checkIfValid, args=[item]))
    threads[-1].start()
    
for thread in threads:
    thread.join()



print(total)