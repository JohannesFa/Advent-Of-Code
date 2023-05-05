
import os,math,sys
sys.set_int_max_str_digits(1000000)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
text = open('input.txt', 'r').readlines()
test = False
if test:
    text = open('testinput.txt', 'r').readlines()
for i in range(len(text)):
    text[i] = text[i].replace("\n", "")

monkeys = [[]]
for line in text:
    if line != "":
        monkeys[-1].append(line)
    else:
        monkeys.append([])


for monkeynum in range(len(monkeys)):
    monkey = monkeys[monkeynum]
    monkeyindex = int(monkey[0][7])
    inventory = monkey[1].split("items: ")[1].split(",")
    operation = monkey[2].split("n: ")[1]
    test = int(monkey[3].split("divisible by")[1])
    truetarget = int(monkey[4].split("throw to monkey")[1])
    falsetarget = int(monkey[5].split("throw to monkey")[1])
    monkeys[monkeynum] = [monkeyindex, inventory, operation, test, truetarget, falsetarget, 0]

supmod = 1
for i in monkeys:
    supmod = supmod*i[3]

print(supmod)
for round in range(10000):
    print(round)
    for i in monkeys:
        #print(i)
        for old in i[1]:
            monkeys[i[0]][6]= monkeys[i[0]][6] + 1
            old = int(old)
            new = -1
            exec(i[2].strip())
            
            new = math.floor(new)
            #print(new)
            if new % i[3] == 0:
                #print("true")
                monkeys[i[4]][1].append(str(new%supmod))
            else:
                #print("false")
                monkeys[i[5]][1].append(str(new%supmod))
        monkeys[i[0]][1] = []
    """
    if round > 50:
        for i in monkeys:
            print(i)
        input()"""
        

for i in monkeys:
    print(i[6])


