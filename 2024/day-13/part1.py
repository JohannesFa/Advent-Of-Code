#By LazerK3
import os,math
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

slots = [[]]
for i in lines:
    item = i.strip()
    if item == "":
        slots.append([])
    else:
        slots[-1].append(item)

costsum = 0


for slot in slots:
    abutton, bbutton, prizelocation = slot
    abutton = abutton.split(": ")[1].split(", ")
    bbutton = bbutton.split(": ")[1].split(", ")
    abuttonmove = (int(abutton[0].split("+")[1]), int(abutton[1].split("+")[1]))
    bbuttonmove = (int(bbutton[0].split("+")[1]), int(bbutton[1].split("+")[1]))
    prizelocation = prizelocation.split(": ")[1].split(", ")
    prizelocation = (int(prizelocation[0].split("=")[1]), int(prizelocation[1].split("=")[1]))
    a = (prizelocation[1]-(abuttonmove[1]/abuttonmove[0])*prizelocation[0])/((bbuttonmove[1]/bbuttonmove[0])-(abuttonmove[1]/abuttonmove[0]))
    bbuttontimes = a/bbuttonmove[0]
    abuttontimes = (prizelocation[0]-a)/abuttonmove[0]
    if math.isclose(bbuttontimes,round(bbuttontimes)) and math.isclose(abuttontimes,round(abuttontimes)):
        cost = abuttontimes*3+bbuttontimes
        print(f"Machine solved with A presses: {int(abuttontimes)}, B presses: {int(bbuttontimes)}, Cost: {int(cost)}")
        costsum += cost
    else:
        print(f"No valid solution for this machine {prizelocation}.")
print(costsum)
#print(len(slots))