#By LazerK3
import os, re, numpy as np
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

linearrs = []
for i in lines:
    item = i.strip()
    res1 = re.split("  *",item)
    print(res1)
    linearrs.append(res1)

nparr = np.array(linearrs)
rotarr = np.rot90(nparr)
print(rotarr)
opsum = 0
for problem in rotarr:
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
