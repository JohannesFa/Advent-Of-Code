#By LazerK3
import os
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()

width = len(lines[0])
height = len(lines)

def isValidHeight(curheight):
    if curheight >= height:
        return False
    elif curheight < 0:
        return False
    else:
        return True

def isValidWidth(curWidth):
    if curWidth >= width:
        return False
    elif curWidth < 0:
        return False
    else:
        return True


accessableAllTime = 0
oldlines = []
while oldlines != lines:
    print("loop")
    accessable = 0
    oldlines = lines.copy()
    for ii in range(len(lines)):
        i = lines[ii]
        item = i.strip()
        for chari in range(len(item)):
            char = item[chari]
            #print(char)
            if char == "@":
                attcounter = 0
                for xoffset in range(-1,2):
                    for yoffset in range(-1,2):
                        xcheck = chari + xoffset
                        ycheck = ii + yoffset
                        #print(xcheck,ycheck)
                        if isValidHeight(ycheck) and isValidWidth(xcheck):
                            plalala = lines[ycheck][xcheck]
                            if plalala == "@":
                                attcounter+=1
                #print(attcounter)
                if attcounter < 5:
                    lines[ii] = lines[ii][:chari] + "." + lines[ii][chari+1:]
                    accessable += 1
    accessableAllTime += accessable



    



print(accessable)
print(accessableAllTime)

#print(width,height)
