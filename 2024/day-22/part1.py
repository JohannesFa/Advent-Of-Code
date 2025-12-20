#By LazerK3
import os,math
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()
            


def mix(secretnum, value):
    xor = secretnum ^ value #this is bitwise xor
    return xor

def prune(secretnum):
    return secretnum % 16777216


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
for i in lines:
    item = i.strip()
    currentsecret = int(item)
    for i in range(2000):
        currentsecret = getnext(currentsecret)
    totalof2000secrets +=currentsecret
    print(currentsecret)

print("------------")
print(totalof2000secrets)
