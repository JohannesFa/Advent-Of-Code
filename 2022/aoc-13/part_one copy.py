
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
text = open('input.txt', 'r').readlines()
test = True
if test:
    text = open('testinput.txt', 'r').readlines()
for i in range(len(text)):
    text[i] = text[i].strip()

valuedict = {"a": -1, "b": 0, "c": 1, "d": 2, "e": 3, "f": 4, "g": 5, "h": 6, "i": 7, "j": 8, "k": 9, "l": 10, "m": 11, "n": 12, "o": 13, "p": 14, "q": 15, "r": 16, "s": 17, "t": 18, "u": 19, "v": 20, "w": 21, "x": 22, "y": 23, "z": 24}

packetcombos = [[]]
for i in text:
    if i != "":
        packetcombos[-1].append(i.split(","))
    else:
        packetcombos.append([])


for packetcombo in range(len(packetcombos)):
    for packet in range(len(packetcombos[packetcombo])):
        for i in range(len(packetcombos[packetcombo][packet])):
            packetcombos[packetcombo][packet][i] = valuedict[packetcombos[packetcombo][packet][i]]
anwser = 0
anses = []


for i in range(len(packetcombos)):
    minlen = [len(packetcombos[i][0]), len(packetcombos[i][1])]
    minlen.sort()
    minlen = minlen[0]
    #print(len(packetcombos[i][0]))
    #print(len(packetcombos[i][1]))
    print("Minlen is", minlen)
    print("Packet 1 is", packetcombos[i][0])
    print("Packet 2 is", packetcombos[i][1])
    done = False
    if done == False:
        for num in range(minlen):
            if done == False:
                #print(len(packetcombos[i][1]))
                if packetcombos[i][0][num] > packetcombos[i][1][num]:
                    print(packetcombos[i][0][num], "is greater than", packetcombos[i][1][num])
                    done = True
                elif packetcombos[i][0][num] < packetcombos[i][1][num]:
                    print(packetcombos[i][0][num], "is less than", packetcombos[i][1][num])
                    print("Appending ", i+1)
                    done = True
                    anwser += i+1
                    anses.append(i+1)
        print("Ran out of numbers")
        if len(packetcombos[i][0]) == minlen and done == False:
            print("Packet 1 is less than packet 2")
            print("Appending ", i+1)
            anwser += i+1
            anses.append(i+1)
            
            
        

for i in packetcombos:
    print(i[0],"\n", i[1])
    print("\n")

print("Ans is", anwser)
print("Anses is", sum(list(dict.fromkeys(anses))))