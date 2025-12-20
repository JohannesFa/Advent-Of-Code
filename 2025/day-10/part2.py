#By LazerK3
import os, copy
import threading
from multiprocessing import Pool
import time
os.chdir(os.path.dirname(__file__))
lines = open("input.txt", "r").readlines()



class MachineState:

    def __init__(self,lightsTarget, buttonsList, currentLights,targetJotage):
        self.lightsTarget = lightsTarget
        self.buttonsList = buttonsList
        self.currentLights = currentLights
        
        self.targetJoltage = tuple(map(int,targetJotage))
        self.currentJotage = []
        for jolt in targetJotage:
            self.currentJotage.append(0)
    
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

    def evalCombo(self, currentState):
        evalList = self.currentJotage.copy()

        #print(evalList)
        for buttonIndex in range(len(self.buttonsList)):
            for increaseIndex in self.buttonsList[buttonIndex]:
                #print(increaseIndex)
                evalList[increaseIndex] = evalList[increaseIndex] + currentState[buttonIndex]
        return tuple(evalList)


    def inDone(self, currentState):
        #print("\n")
        #print(self.currentLights)
        #print(self.lightsTarget)
        if self.lightsTarget == currentState:
            return True
        else:
            return False
        
    def inDoneJolt(self, currentState):
        evaluated = self.evalCombo(currentState)

        if self.targetJoltage == evaluated:
            return True
        else:
            return False

    def simulatePress(self, buttonIndex, currentState):
        
        for i in range(len(self.buttonsList[buttonIndex])):
            lightIndex = self.buttonsList[buttonIndex][i]
            #print("Pressing",lightIndex)
            currentState = self.flipLight(lightIndex, currentState)
        return currentState
        
    def simulateJoltagePress(self, buttonIndex, currentState):

        currentState = list(currentState)
        #print(currentState)
        currentState[buttonIndex] = currentState[buttonIndex]+1
        return tuple(currentState)


        


machines = []
for i in lines:
    item = i.strip().split(" ")
    #print(item)
    lights = item[0]
    jotages = item[len(item)-1]
    #print(jotages)
    buttons = item[1:len(item)-1] 
    lights = lights[1:len(lights)-1]
    buttonsList = []
    #print(buttons)
    for button in buttons:
        a = button[1:len(button)-1].split(",")
        #print(a)
        buttonsList.append(list(map(int,a)))
    machines.append(MachineState(lights,buttonsList,"."*len(lights),jotages[1:len(jotages)-1].split(",")))

stepList = []



def simMachine(MachineState):
    step = 0

    machineStates = []
    print("Starting ", machine.currentJotage)

    firstMachineState = []
    for buttonI in range(len(machine.buttonsList)):
        firstMachineState.append(0)
    
    
    machineStates = set([tuple(firstMachineState)])

    print(machineStates)

    foundAnswer = False
    newMachineStates = set([])
    while not foundAnswer:
        for machineState in machineStates:
            for buttonIndex in range(len(machine.buttonsList)):
                
                newState = machine.simulateJoltagePress(buttonIndex,machineState)
                #print("New")
                #print(newState)
                #print(machine.targetJoltage) 
                #print(machine.evalCombo(newState))
                if machine.inDoneJolt(newState):
                    foundAnswer = True
                    break
                newMachineStates.add(newState)
        
        print(len(newMachineStates))
        #print(newMachineStates)
        machineStates = newMachineStates.copy()
        step += 1
    print("Finished")
    stepList.append(step)


#threads = []
for machine in machines[6:]:

    #print(machine.evalCombo([1,3,0,3,1,2]))
    #exit()
    simMachine(machine)
#    t = threading.Thread(target=simMachine,args=(machine,))
#    t.start()
#    threads.append(t)

#with Pool(processes=len(machines)) as pool:
#    results = pool.map(simMachine,machines)
#    print(results)

#for thread in threads:
#    thread.join()

    

print(sum(stepList))