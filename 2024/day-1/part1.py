#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

ll = []     
rl = []   
for i in lines:
    item = i.strip()
    item = i.split("   ")
    ll.append(int(item[0]))
    rl.append(int(item[1]))
ll.sort()
rl.sort()
dif = []
for i in range(len(ll)):
    dif.append(abs(ll[i]-rl[i]))

print(sum(dif))