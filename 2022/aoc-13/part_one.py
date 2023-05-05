
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
text = open('input.txt', 'r').readlines()
test = True
if test:
    text = open('testinput.txt', 'r').readlines()
for i in range(len(text)):
    text[i] = text[i].strip()

def checklist(var, listofvals):
    if type(var) == list:
        for i in var:
            if type(i) == list:
                i = checklist(i, [])
                for j in i:
                    listofvals.append(j)

            else:
                listofvals.append(i)
    else:
        listofvals.append(var)
    print("not list", var)
    return listofvals

packetcombos = [[]]
for i in text:
    if i != "":
        exec("packetcombos[-1].append(i)")
    else:
        packetcombos.append([])
newpacketcombos = []
for packetcombo in range(len(packetcombos)):
    newpacketcombo = []
    for packet in range(len(packetcombos[packetcombo])):
        newpacket = []
        newpacket = checklist(packetcombos[packetcombo][packet], newpacket)
        newpacketcombo.append(newpacket)
    
    newpacketcombos.append(newpacketcombo)

packetcombos = newpacketcombos

for i in packetcombos:
    print(i[0],"\n", i[1])
    print("\n")