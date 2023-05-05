#pylint: disable=consider-using-enumerate
import os, rich

#create console with rich
console = rich.get_console()
#print green text
os.chdir(os.path.dirname(os.path.abspath(__file__)))
input = open('input.txt', 'r').readlines()
test = False
debug = True
if test:
    input = open('testinput.txt', 'r').readlines()
for i in range(len(input)):
    input[i] = input[i].strip()
width = len(input[0])
height = len(input)
print("thhe width is: " + str(width) + " and the height is: " + str(height))
console.input("Press [bold green]ENTER[/bold green] to continue...")

if debug:
    print("The input is: ")
    for line in input:
        print(line)

up = "^"
down = "v"
left = "<"
right = ">"
empty = "."
wall = "#"

arrayofblizzards = []


def addbackborder(arrayofblizzards):
    
    for line in range(len(arrayofblizzards)):
        if line == 0:
            for item in range(len(arrayofblizzards[line])):
                arrayofblizzards[line][item].append(wall)
        elif line == len(arrayofblizzards) - 1:
            for item in range(len(arrayofblizzards[line])):
                arrayofblizzards[line][item].append(wall)
        for item in range(len(arrayofblizzards[line])):
            if item == 0 and line != 0 and line != len(arrayofblizzards) - 1:
                arrayofblizzards[line][item].append(wall)
            elif item == len(arrayofblizzards[line]) - 1 and line != 0 and line != len(arrayofblizzards) - 1:
                arrayofblizzards[line][item].append(wall)
    return arrayofblizzards

def simulate(inputarray):
    empty = []
    for line in range(len(inputarray)):
        empty.append([])
        for item in range(len(inputarray[line])):
            empty[-1].append([])
    for line in range(len(inputarray)):
        for item in range(len(inputarray[line])):
            if debug:
                print(inputarray[line][item])
            #if len (inputarray[line][item]) == 0:
            #    print("empty")
            #    empty[line][item].append(empty)
            for direction in inputarray[line][item]:
                if direction != empty:
                    if debug:
                        pass
                        #print("direction: " + direction)
                    if direction == up:
                        if wall not in inputarray[line - 1][item] :
                            empty[line - 1][item].append(up)
                            if debug:
                                print("up")
                        else:
                            empty[-2][item].append(up)
                            if debug:
                                print("up to bottom")
                    elif direction == down:
                        if wall not in inputarray[line + 1][item]:
                            empty[line + 1][item].append(down)
                            if debug:
                                print("down")
                        else:
                            empty[1][item].append(down)
                            if debug:
                                print("down to top")
                    elif direction == left:
                        if wall not in inputarray[line][item - 1]:
                            empty[line][item - 1].append(left)
                            if debug:
                                print("left")
                        else:
                            empty[line][-2].append(left)
                            if debug:
                                print("left to right")
                    elif direction == right:
                        if wall not in inputarray[line][item + 1]:
                            empty[line][item + 1].append(right)
                            if debug:
                                print("right")
                        else:
                            empty[line][1].append(right)
                            if debug:
                                print("right to left")
                    elif direction == empty:
                        empty[line][item].append(empty)
                        if debug:
                            print("empty")
    if debug:
        print(empty)
    return empty

def removeempty(inputarray):
    for line in range(len(inputarray)):
        for item in range(len(inputarray[line])):
            for direction in inputarray[line][item]:
                if len (inputarray[line][item]) != 1:
                    if direction == empty:
                        inputarray[line][item].remove(empty)
    return inputarray

def checkifempty(inputarray, row, column):
    if row < 0 or column < 0 or row >= height or column >= width:
        
        print("Error: invalid row and column with ", row, column)
        return False
    elif row == 0 and column == 1:
        return True
    elif row == height-1 and column == width-2:
        return True
    for  direc in onlydirections:
        if direc in inputarray[row][column]:
            return False
    return True

def possiblemoves(inputarray, row, column):
    possiblemoves = []
    if checkifempty(inputarray, row - 1, column):
        possiblemoves.append([row-1, column])
    if checkifempty(inputarray, row + 1, column):
        possiblemoves.append([row+1, column])
    if checkifempty(inputarray, row, column - 1):
        possiblemoves.append([row, column-1])
    if checkifempty(inputarray, row, column + 1):
        possiblemoves.append([row, column+1])
    if checkifempty(inputarray, row, column):
        possiblemoves.append([row, column])
    return possiblemoves

directions = [up, down, left, right, empty, wall]
onlydirections = [up, down, left, right, wall]
for line in input:
    arrayofblizzards.append([])
    for charindex in range(len(line)):
        char = line[charindex]
        arrayofblizzards[-1].append([empty])
        if char not in directions:
            print("Error: invalid character in input")
            exit()
        if char != empty:
            arrayofblizzards[-1][-1].append(char)
if debug:
    print("The output is: ")
for line in arrayofblizzards:
    if debug:
        print(line)
if debug:
    print("After removing empty result is: ")
    print(removeempty(arrayofblizzards))
if debug:
    print("The result is: ")
    print("simulating")
entrencecords = [0, 1]
exitcords = [height-1, width-2]
arrayofcords = []
arrayofcords.append(entrencecords)



for i in range(40):
    arrayofblizzards = simulate(arrayofblizzards)
    arrayofblizzards = addbackborder(arrayofblizzards)
    offset = 0
    for cord in range(len(arrayofcords)):
        moves = possiblemoves(arrayofblizzards, int(arrayofcords[cord-offset][0]), int(arrayofcords[cord-offset][1]))
        if len(moves) == 0:
            if debug:
                print("no moves found")
            arrayofcords.remove(arrayofcords[cord-offset])
            offset += 1
        else:
            for move in moves:
                arrayofcords.append(move)
    offset2 = 0
    for cord in range(len(arrayofcords)):
        currentcord = arrayofcords.pop(cord-offset2)
        if currentcord not in arrayofcords:
            arrayofcords.append(currentcord)
        else:
            offset2 += 1
    
    if debug:    
        print(arrayofcords)
    print("step ", i+1)
    for lineindex in range(len(arrayofblizzards)):
        line = arrayofblizzards[lineindex]
        for charindex in range(len(line)):
            char = arrayofblizzards[lineindex][charindex]
            if len(char) == 0:
                #console.print(".", style="on green", end="")
                print(".", end="")
                #print with background color green
            elif len(char) == 1:
                #console.print(char[0], style="on red", end="")
                print(char[0], end="")
            else:
                console.print(str(len(char)), style="on red", end="")
        print("\n", end="")

    #shows which cords are in the arrayofcords list in the console    
    emptysystem = []
    for i in range(height):
        emptysystem.append([])
        for j in range(width):
            if [i-1, j] in arrayofcords:
                console.print(" ", style="on green", end="")
            else:
                console.print(" ", style="on red", end="")
        print("\n", end="")
    



    if exitcords in arrayofcords:
        print("exit found at ", str(i+1))
        break

arrayofblizzards = removeempty(arrayofblizzards)

"""
for lineindex in range(len(arrayofblizzards)):
    line = arrayofblizzards[lineindex]
    for charindex in range(len(line)):
        char = arrayofblizzards[lineindex][charindex]
        if len(char) == 0:
            console.print(".", style="on green", end="")
            #print with background color green
        elif len(char) == 1:
            console.print(char[0], style="on red", end="")
        else:
            console.print(str(len(char)), style="on red", end="")
    print("\n", end="")
p"""

print(arrayofcords)

print(exitcords)

