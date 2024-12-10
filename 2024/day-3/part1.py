#By LazerK3
import os,re
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()
newlines = []
all = ""
for i in lines:
    item = i.strip()
    all = all + "l" + item

def comp(match):
    match = str(match)
    a,b = match.replace("mul(", "").replace(")", "").split(",")
    return int(a)*int(b)
matches = re.findall("mul\(\d+,\d+\)", all)

totalsum = 0
for match in matches:
    totalsum += comp(match)

print(totalsum)