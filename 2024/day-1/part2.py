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
apperances = {}
for i in range(len(ll)):
    if ll[i] not in apperances:
        apperances[ll[i]] = rl.count(ll[i])

print(apperances)

sumofvals = 0
for i in ll:
    if i in apperances:
        sumofvals += apperances[i]*i
    

print(sumofvals)