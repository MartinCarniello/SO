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
        """Manda el PCB a Ready, si el kernel esta apagado, lo prende.
           Si esta prendido y la CPU no esta ejecutando ningun proceso,
           hace un contextSwitch"""
        kernel.sendPCBToReadyQueue(self.getPCB())
        if not kernel.getIsRunning():
            kernel.turnOn()
        else:
            if kernel.getCpu().getPCB() == None:
                kernel.contextSwitch()