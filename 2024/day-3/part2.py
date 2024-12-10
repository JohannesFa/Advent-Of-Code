#By LazerK3
import os,re
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()
newlines = []
all = ""
for i in lines:
    item = i.strip()
    all = all + "l" + item
all = "do()"+all #Don't would have otherwise turned off the begining

newall = ""
for lines in all.split("don't()"):
    valid = "l".join(lines.split("do()")[1:])
    newall += valid



def comp(match):
    match = str(match)
    a,b = match.replace("mul(", "").replace(")", "").split(",")
    return int(a)*int(b)
matches = re.findall("mul\(\d+,\d+\)", newall)

totalsum = 0
for match in matches:
    totalsum += comp(match)

print(totalsum)