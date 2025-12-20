#By LazerK3
import os,math
os.chdir(os.path.dirname(__file__))
lines = open("test.txt", "r").readlines()
            


def mix(secretnum, value):
    xor = secretnum ^ value #this is bitwise xor
    return xor

def prune(secretnum):
    return secretnum % 16777216

def getSequenceIndex(sequence, monkeysequence):
    for i in range(len(sequence)):
        if i >= 3:
            if monkeysequence == sequence[i-3:i+1]:
                return i+1
    #print("wtf")
    #exit()

def findBestSequence(sequence, differences):
    prices = []
    for price in sequence:
        if price not in prices:
            prices.append(price)
    prices.sort(reverse=True)
    for price in prices:
        for itemindex in range(len(sequence)):
            item = sequence[itemindex]
            if item == price:
                if itemindex >= 4:
                    foundmonkeysequence = differences[itemindex-4:itemindex]
                    fmsindex = getSequenceIndex(differences,foundmonkeysequence)
                    print(f"Testing fms: {fmsindex} against {itemindex} with fms {foundmonkeysequence}")
                    if fmsindex == itemindex:
                        print(f"found match with sequence {sequence}, differences {differences}, foundmonkeysq {foundmonkeysequence}, {fmsindex=}, {itemindex=}, {sequence[itemindex]}")
                        return itemindex
    print("returned nothing")
    exit()
def getnext(secret):
    step1p1 = secret*64
    step1p2 = mix(step1p1,secret)
    step1p3 = prune(step1p2)
    step2p1 = math.floor(step1p3/32)
    step2p2 = mix(step1p3,step2p1)
    step2p3 = prune(step2p2)
    step3p1 = step2p3 * 2048
    step3p2 = mix(step3p1,step2p3)
    step3p3 = prune(step3p2)
    return step3p3

totalof2000secrets = 0
totalprice = 0

allsequences = {}
for n1 in range(-9,10):
    for n2 in range(-9,10):
        for n3 in range(-9,10):
            for n4 in range(-9,10):
                allsequences[(n1,n2,n3,n4)] = []

for i in lines:
    item = i.strip()
    currentsecret = int(item)
    previouslastdigit = -1
    difference = None
    sequence = str(currentsecret)[-1]
    differences = []
    for i in range(2000-1):
        #print(currentsecret)
        currentsecret = getnext(currentsecret)
        lastdigit = str(currentsecret)[-1]
        if previouslastdigit != -1:
            difference = int(lastdigit)-previouslastdigit
            differences.append(difference)
        else:
            differences.append(int(lastdigit)-int(sequence))
        previouslastdigit = int(lastdigit)
        sequence += lastdigit
    
    #foundindex = findBestSequence(sequence,differences)
    #price = int(sequence[foundindex])
    #price = 0
    for testseqq in allsequences:
        testseq = list(testseqq)
        indexresult = getSequenceIndex(differences,testseq)
        if indexresult != None:
            price = int(sequence[indexresult])
            print(price,testseq)
            allsequences[testseqq].append(price)



bananapricesumlist = []
for seq in allsequences:
    assval = allsequences[seq]
    if assval != []:
        bananapricesumlist.append(sum(assval))
        print(assval)


    #totalprice += 
    #totalof2000secrets +=currentsecret
    #print(currentsecret)


print("Result-----")
print(max(bananapricesumlist))