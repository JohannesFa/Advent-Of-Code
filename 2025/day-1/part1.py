#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()


current_num = 50
times_at_zero = 0

def ownmodulo(in_num, modwith,rotamount):
    global times_at_zero

    rotamount = abs(rotamount)

    new_num = in_num%modwith


    if in_num != new_num:
        print(f"From {in_num} to {new_num}")
        times_at_zero += 1
    return new_num


for i in lines:
    item = i.strip()
    #print(item)
    direction = item[0]
    amount = int(item[1:])
    if direction == "L":
        amount = -amount
    current_num += amount
    current_num = ownmodulo(current_num,100,amount)
    print(current_num)

print(f"Final num is {current_num}!")
print(f"Final num is {times_at_zero}!")

