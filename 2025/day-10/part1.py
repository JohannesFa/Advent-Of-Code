#By LazerK3
import os, copy
import threading
import time
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()



class MachineState:

    def __init__(self,lightsTarget, buttonsList, currentLights):
        self.lightsTarget = lightsTarget
        self.buttonsList = buttonsList
        self.currentLights = currentLights
    
    def flipLight(self, Flipindex, currentState):
        currentLight = currentState[Flipindex]
        newlightChar = ""
        if currentLight == ".":
            newlightChar = "#"
        else:
            newlightChar = "."
        lastitem = ""
        if Flipindex+1 >= len(currentState):
            pass
        else:
            lastitem = currentState[Flipindex+1:]
        #print("\nFlipping",Flipindex)
        #print(self.currentLights)
        currentState = currentState[:Flipindex] + newlightChar + lastitem
        #print("After")
        #print(self.currentLights)
        return currentState

    def inDone(self, currentState):
        #print("\n")
        #print(self.currentLights)
        #print(self.lightsTarget)
        if self.lightsTarget == currentState:
            return True
        else:
            return False

    def simulatePress(self, buttonIndex, currentState):
        
        for i in range(len(self.buttonsList[buttonIndex])):
            lightIndex = self.buttonsList[buttonIndex][i]
            #print("Pressing",lightIndex)
            currentState = self.flipLight(lightIndex, currentState)
        return currentState
        


        


machines = []
for i in lines:
    item = i.strip().split(" ")
    #print(item)
    lights = item[0]
    jotages = item[len(item)-1]
    buttons = item[1:len(item)-1] 
    lights = lights[1:len(lights)-1]
    buttonsList = []
    #print(buttons)
    for button in buttons:
        a = button[1:len(button)-1].split(",")
        #print(a)
        buttonsList.append(list(map(int,a)))
    machines.append(MachineState(lights,buttonsList,"."*len(lights)))

stepList = []

def simMachine(machine):
    step = 0
    #print("Machine ")
    #print(machine.currentLights)
    #machine.simulatePress(0)
    #print(machine.currentLights)
    machineStates = set([machine.currentLights])
    newMachineStates = set([])
    foundAnswer = False
    while not foundAnswer:
        #print("?")
        for machineState in machineStates:
            #print(len(machineStates))
            #print(machineState)
            for buttonIndex in range(len(machine.buttonsList)):
                
                newState = machine.simulatePress(buttonIndex,machineState)
                if machine.inDone(newState):
                    foundAnswer = True
                    break
                newMachineStates.add(newState)
        #print("--------------------------------------------------------\n--------------------------------------------------------n--------------------------------------------------------")
        #print(len(newMachineStates))
        #print(newMachineStates)
        machineStates = newMachineStates.copy()
        step += 1
    stepList.append(step)


threads = []
for machine in machines:
    t = threading.Thread(target=simMachine,args=(machine,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

    

print(sum(stepList))