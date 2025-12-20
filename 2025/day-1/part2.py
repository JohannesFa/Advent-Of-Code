#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()


current_num = 50
times_at_zero = 0

def ownmodulo(in_num, modwith,rotamount):
    global times_at_zero
    sign = int(rotamount/abs(rotamount))
    
    for i in range(abs(rotamount)):
        in_num += sign
        in_num %= modwith
        if in_num == 0:
            times_at_zero += 1
    return in_num



for i in lines:
    item = i.strip()
    #print(item)
    direction = item[0]
    amount = int(item[1:])
    if direction == "L":
        amount = -amount
    #current_num += amount
    print(f"Start at {current_num}")
    current_num = ownmodulo(current_num,100,amount)
    print(f"End at {current_num} \n")
    print(current_num)

print(f"Final num is {current_num}")
print(f"Final num is {times_at_zero}")

