#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()
            

def multiplycord(cord,mul):
    return (cord[0]*mul,cord[1]*mul)
def addCords(c1,c2):
    return (c1[0]+c2[0],c1[1]+c2[1])

time = 100
xsize = 101
ysize = 103

xbad = (xsize-1)/2
ybad = (ysize-1)/2

q1 = 0
q2 = 0
q3 = 0
q4 = 0

positions = []
for i in lines:
    item = i.strip()
    p,v = item.split(" ")
    p,v = p.split("=")[1].split(","), v.split("=")[1].split(",")
    p = (int(p[0]),int(p[1]))
    v = (int(v[0]),int(v[1]))
    movedpos = multiplycord(v,time)
    newpos = addCords(p,movedpos)
    tppos = (newpos[0]%xsize,newpos[1]%ysize)
    positions.append(tppos)
    if tppos[0] > xbad:
        if tppos[1] > ybad:
            q1+=1
        elif tppos[1] < ybad:
            q2+=1
    elif tppos[0] < xbad:
        if tppos[1] > ybad:
            q3+=1
        elif tppos[1] < ybad:
            q4+=1

print(q1,q2,q3,q4)
print(q1*q2*q3*q4)