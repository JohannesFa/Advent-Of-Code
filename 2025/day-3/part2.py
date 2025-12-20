#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

voltagesum = 0

def testRemoveToFindHighest(charArray13Lenth):
    #print(f"Got {len(charArray13Lenth)}")
    bestFound = []
    for i in range(1,len(charArray13Lenth)):
        newTestArr = charArray13Lenth[:i]+charArray13Lenth[i+1:]
        #print(len(newTestArr))
        if newTestArr > bestFound:
            bestFound = newTestArr
    #print(f"Ret {len(bestFound)}")
    return bestFound


#def findHighest(charArr1, charArr2):
#    sortedArr1 = sorted(charArr1)
#    sortedArr2 = sorted(charArr2)
#    #print("Sortedarr",sortedArr1,sortedArr2)
#    return sortedArr1[-1]+sortedArr2[-1]

#def splitToPossible(charArr):
#    highestFound = ""
#    for i in range(1,len(charArr)):
#        p1 = charArr[:i]
#        p2 = charArr[i:]
#        #print(p1,p2)
#        tempHigh = findHighest(p1,p2)
#        #print(tempHigh)
#        if tempHigh > highestFound:
#            highestFound = tempHigh
#    return highestFound

#def findLowest(charArr):
#    return sorted(charArr)[0]


def travelBackWards(charArr):
    currentNewArr = []
    for char in reversed(charArr):
        if len(currentNewArr) < 12:
            currentNewArr.insert(0,char)
        else:
            arrCopy = currentNewArr.copy()
            #arrCopy.remove(findLowest(currentNewArr))
            arrCopy.insert(0,char)
            newTestArr = testRemoveToFindHighest(arrCopy)
            if currentNewArr <= newTestArr:
                currentNewArr = newTestArr

    return "".join(currentNewArr)

for i in lines:
    item = i.strip()
    itemstr = str(item)
    itemarray = list(itemstr)
    #print("".join(itemarray))
    res = travelBackWards(itemarray)
    #print(res)
    voltagesum += int(res)
    #print("H,nh",h,nh)
    #print(res)

#print(testRemoveToFindHighest(['2', '3', '4', '3', '2', '3', '3', '3', '3', '4', '4', '4', '4', '7', '8']))
print(voltagesum)

