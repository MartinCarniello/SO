'''
Created on 06/07/2013

@author: martin
'''

from kernel.Interruptions import Interruption

class AddProcessToReadyQueue(Interruption):
    
    def __init__(self, pcb):
        self.pcb = pcb
        
    def getPCB(self):
        return self.pcb
    
    def setPCB(self, pcb):
        self.pcb = pcb
    
    def interruptionMethod(self, kernel):
        kernel.sendPCBToReadyQueue(self.getPCB())
        if not kernel.getIsRunning():
            kernel.turnOn()
        else:
            if kernel.getCpu().getPCB() == None:
                kernel.contextSwitch()