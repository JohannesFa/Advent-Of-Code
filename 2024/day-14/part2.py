#By LazerK3
import os,matplotlib as plt, time
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()
            

def multiplycord(cord,mul):
    return (cord[0]*mul,cord[1]*mul)
def addCords(c1,c2):
    return (c1[0]+c2[0],c1[1]+c2[1])

#clock = 100
xsize = 101
ysize = 103

xbad = (xsize-1)/2
ybad = (ysize-1)/2



def printpositions(positions):
    global xsize
    global ysize
    bigstring = ""
    #print(positions)
    for i in range(xsize):
        for j in range(ysize):
            if (i,j) in positions:
                bigstring += "#"
            else:
                bigstring+="."
        bigstring+="\n"
    print(bigstring)
clock = 0
while True:
    q1 = 0
    q2 = 0
    shouldprint = False
    #q3 = 0
    #q4 = 0
    clock +=1
    positions = []
    for i in lines:
        item = i.strip()
        p,v = item.split(" ")
        p,v = p.split("=")[1].split(","), v.split("=")[1].split(",")
        p = (int(p[0]),int(p[1]))
        v = (int(v[0]),int(v[1]))
        movedpos = multiplycord(v,clock)
        newpos = addCords(p,movedpos)
        tppos = (newpos[0]%xsize,newpos[1]%ysize)
        positions.append(tppos)
        if tppos[1] > ybad*1.8:
            q1+=1
        if tppos[0] > xbad*1.8:
            q2+=1
    
    if q1 <30 and q2 < 30:
        print(clock)
        time.sleep(0.016)
        
        printpositions(positions)
        break
