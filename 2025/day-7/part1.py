#By LazerK3
import os,time

t1 = time.time()
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

nonnum = ["^",".","S"]

def replaceString(stri,item, index):
    curritem = stri[index]
    if curritem not in nonnum:
        #print("Olditem",item,curritem)
        item = str(int(curritem)+int(item))
        #print("New",item)

        return stri[:index]+[item]+stri[index+1:]
    else:
        return stri[:index]+[item]+stri[index+1:]

startpos = (0,0)

splitCount = 0

for ii in range(int(len(lines))-1,0,-2):
    #print(f"removing {ii}")
    reindex = len(lines) - ii-1
    lines.pop(ii)
    
    #i = lines[ii]



for ii in range(0,len(lines)):
    #print(ii)
    i = lines[ii]
    lines[ii] = list(i.strip())
    item = lines[ii]
    for chari in range(len(item)):
        #print(item)
        #print(chari)
        char = item[chari]
        if char == "S":
            #print("S")
            item = replaceString(item,"1",chari)
        if char == "^" and lines[ii-1][chari] not in nonnum:
            splitCount+=1
            #print(f"Shitting {char=} {chari=} {ii=}")
            item = replaceString(item,lines[ii-1][chari],chari-1)
            #item = replaceString(item,"x",chari)
            item = replaceString(item,lines[ii-1][chari],chari+1)
        if char != "^" and lines[ii-1][chari] not in nonnum:
            item = replaceString(item,lines[ii-1][chari],chari)
    lines[ii] = item

count2 = 0
#for line in lines:
    #count2+=line.count("x")
    #print(" ".join(line))


#print(f"{splitCount=}")

#print(f"{count2=}")

newCount = 0
for char in lines[-1]:
    if char not in nonnum:
        newCount +=int(char)

print(f"{newCount=}")

print("Time is: ", (time.time()-t1)*1000)