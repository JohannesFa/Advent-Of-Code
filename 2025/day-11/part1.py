#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

connectionDict = {}
for i in lines:
    item = i.strip()
    parent, children = item.split(": ")
    childrenList = children.split(" ")

    connectionDict[parent] = childrenList

connections = 0
def simOneLayer(parent):
    global connections
    childrenL = connectionDict[parent]
    for child in childrenL:
        if child == "out":
            connections += 1
            break
        else:
            simOneLayer(child)

simOneLayer("you")

print(connections)
