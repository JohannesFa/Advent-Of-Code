
import os, rich,math
import matplotlib.pyplot as plt
console = rich.get_console()



os.chdir(os.path.dirname(os.path.abspath(__file__)))
text = open('input.txt', 'r').readlines()
test = False
if test:
    text = open('testinput.txt', 'r').readlines()
for i in range(len(text)):
    text[i] = text[i].strip()

valuedict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "S": 1, "E": 27}

max = 255/12

height = len(text)
width = len(text[0])

def pprint():
    global text
    for i in text:
        for j in i:
            number = valuedict[j]
            if number == 30:
                rgb = "rgb(255,255,255)"
            elif number == 31:
                rgb = "rgb(0,0,255)"
            else:
                total = round(max*number)
                r = 0
                g = 0
                b = 0
                if total >= 510:
                    r = 255
                    g = 255
                    b = total % 255
                elif total >= 255:
                    r = 255
                    g = total % 255
                    b = 0
                else:
                    r = total % 255
                    g = 0
                    b = 0
                
                rgb = f"rgb({r},{g},{b})"
            console.print(j, style=rgb, end="")
        print("")


cords = []
goalcord = []
for ys in range(len(text)):
    for xs in range(len(text[ys])):
        if text[ys][xs] == "S":
            cords.append([xs,ys])
        elif text[ys][xs] == "E":
            goalcord = [xs, ys]

print(cords, goalcord)

def addvec(vec1, vec2):
    return([vec1[0]+vec2[0], vec1[1]+vec2[1]])

def chechoutside(cord):
    global width
    global height

    if cord[0] < 0 or cord[0] > width-1:
        return False
    elif cord[1] < 0 or cord[1] > height-1:
        return False
    else:
        return True

up = [0,1]
down = [0,-1]
left = [-1,0]
right = [1,0]
def getval(cord, text):
    return text[cord[1]][cord[0]]

def grannar(cord):
    up = [0,1]
    down = [0,-1]
    left = [-1,0]
    right = [1,0]

    cordup = addvec(cord, up)
    corddown = addvec(cord, down)
    cordleft = addvec(cord, left)
    cordright = addvec(cord, right)
    cordlist = []
    if chechoutside(cordup):
        cordlist.append(cordup)
    if chechoutside(corddown):
        cordlist.append(corddown)
    if chechoutside(cordleft):
        cordlist.append(cordleft)
    if chechoutside(cordright):
        cordlist.append(cordright)
    return cordlist
result = []




def findanwser(cords):
    global result

    if len(cords) == 0:
        return

    fig, ax = plt.subplots()
    ax.scatter([1],[0])
    plt.show(block=False)

    lastarr = cords
    step = 0
    while True:
        step += 1

        bragrannarlist = []
        for cord in cords:
            value = valuedict[text[cord[1]][cord[0]]]
            cordgrannar = grannar(cord)
            #print(cordgrannar)
            bragrannar = []
            for granne in cordgrannar:
                if valuedict[getval(granne, text)]-value <= 1:
                    bragrannar.append(granne)
                    
            bragrannarlist.append(bragrannar)
        for bragrannar in bragrannarlist:
            for granne in bragrannar:
                cords.append(granne)
        
        #print(cords)
        #Remove dupes
        tempcords = []
        for i in cords:
            if i not in tempcords:
                tempcords.append(i)
        cords = tempcords
        
        

        if goalcord in cords:
            print("Vicotory at step", step)
            result.append(step)
            return

        
        highest = -1
        for i in cords:
            val = getval(i, text)
            num = int(valuedict[val])
            if num > highest:
                highest = num
        
        print("Highest is", highest)
        xes = []
        yes = []
        for i in cords:
            xes.append(i[0])
            yes.append(i[1])

        
        if step > 100 and step <250:
            newcords = []
            for cord in cords:
                if cord[0] > round(width*0.4):
                    newcords.append(cord)
            cords = newcords

        if step > 250:
            newcords = []
            for cord in cords:
                if cord[0] > round(width*0.7):
                    newcords.append(cord)
            cords = newcords



        ax.clear()
        ax.scatter(xes,yes)
        ax.set(xlim=(0,width), ylim = (0, height))
        ax.invert_yaxis()
        plt.draw()
        plt.pause(0.03)
        print("Cords length is", len(cords))
        print("At step", step)
        


for ko in range(height):
    cords = [[0,ko]]
    findanwser(cords)



print(result)


#pprint()
print(len(text)*len(text[0]))

input("Press enter to exit")