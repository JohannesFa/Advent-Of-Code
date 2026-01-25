#By LazerK3
import os, re, numpy as np
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

linearrs = []
problems = []
opsarr = lines[-1]
print(opsarr)
for xIndex in range(len(opsarr)):
    currop = opsarr[xIndex]
    #print(currop)
    if opsarr[xIndex] != " ":
        #print()
        problems.append([currop])
    numrow = []
    for yIndex in range(len(lines)-1):
        num = lines[yIndex][xIndex]
        if num != " ":
            numrow.append(num)
    if len(numrow) != 0:
        problems[-1].insert(0,"".join(numrow))

print(problems)

opsum = 0
for problem in problems:
    operation = problem[-1]
    nums = problem[:-1]
    nums = list(map(int, nums))
    if operation == "+":
        opsum+= sum(nums)
    elif operation == "*":
        mulitem = nums[0]
        for num in nums[1:]:
            mulitem*=num
        opsum+=mulitem

print(opsum)
