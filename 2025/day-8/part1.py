#By LazerK3
import os
from typing import Set
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()


class Cord:

    def __init__(self, x, y, z):
        self.x = x  # Instance attribute
        self.y = y  # Instance attribute
        self.z = z

    def __repr__(self) -> str:
        return str((self.x, self.y, self.z))

    def __eq__(self, other):
        return isinstance(other, Cord) and (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __str__(self):
        return str((self.x, self.y, self.z))

    def distance(self, c2):
        distance = ((self.x-c2.x)**2+(self.y-c2.y)**2+(self.z-c2.z)**2)**0.5
        return distance
    
    def isNotConnected(self,c2,connections):
        selftoc2 = connections[self]
        c2toself = connections[c2]
        if c2 in selftoc2 or self in c2toself:
            return False
        else:
            return True




cordslist = []
cordsConnectionDictonatry = {}
for i in lines:
    item = i.strip()
    cord = list(map(int,item.split(",")))
    cordObject = Cord(cord[0],cord[1],cord[2])
    cordslist.append(cordObject)
    cordsConnectionDictonatry[cordObject] = []

#for cord in cordslist:
#    print(cord)

for cord1 in cordslist:
    smallestDistance = 10e10
    closestCord = None
    #print("Hello")
    for cord2index in range(len(cordslist)):
        cord2 = cordslist[cord2index]
        #print(cord2)
        if cord1 != cord2:
            distance = cord1.distance(cord2)
            #print(distance)
            #print(smallestDistance," ",distance)
            isNotConnected = cord1.isNotConnected(cord2,cordsConnectionDictonatry)
            #print(isNotConnected)
            if distance < smallestDistance and isNotConnected:
                smallestDistance = distance
                closestCord = cord2
    if closestCord == None:
        continue
    else:
        #print("Smalles distance is ", smallestDistance, "between ", cord1, closestCord)
        cordsConnectionDictonatry[closestCord].append(cord1)
        cordsConnectionDictonatry[cord1].append(closestCord)

#print(cordsConnectionDictonatry)
for connection in cordsConnectionDictonatry:
    print("Connection ", cordsConnectionDictonatry[connection], "and ", connection)
    print(len(cordsConnectionDictonatry[connection]),"\n")

def checkConnectionsNotInList(cord,allConnections):
    for connectedCord in cordsConnectionDictonatry[cord]:
        if connectedCord not in allConnections:
            allConnections.append(connectedCord)
            checkConnectionsNotInList(connectedCord,allConnections)


connectionSets = set()


for connection in cordsConnectionDictonatry:
    allConnections = [connection]
    checkConnectionsNotInList(connection,allConnections)
    connectionSets.add(frozenset(allConnections))
lenths = []
print("\n\n\n---------------------")
for setitem in connectionSets:
    print(setitem)
    print(len(setitem))
    lenths.append(len(setitem))

print("Total number of constellations: ", len(connectionSets))

print(sorted(lenths))