#By LazerK3
import os,threading
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

connectionDict = {}
for i in lines:
    item = i.strip()
    parent, children = item.split(": ")
    childrenList = children.split(" ")

    connectionDict[parent] = childrenList

connections = 0
def simOneLayer(parent, foundDac, foundFft):
    global connections
    childrenL = connectionDict[parent]
    for child in childrenL:
        if child == "out":
            if foundFft and foundDac:
                connections += 1
                break
        else:
            if child == "fft":
                foundFft = True
            elif child == "dac":
                foundDac = True
            simOneLayer(child,foundDac,foundFft)

simOneLayer("svr",False,False)

print(connections)
