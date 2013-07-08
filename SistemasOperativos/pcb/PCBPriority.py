'''
Created on 11/05/2013

@author: Carne
'''

class PCBPriority():
    def __init__(self, pcb, priority):
        self.pcb = pcb
        
        self.priority = priority
        
    def getPCB(self):
        return self.pcb
        
    def getPriority(self):
        return self.priority
    
    def getPID(self):
        return self.getPCB().getPID()
    
    def setPID(self, pid):
        self.getPCB().setPID(pid)
    
    def getPC(self):
        return self.getPCB().getPC()
    
    def setPC(self, pc):
        self.getPCB().setPC(pc)
    
    def isEnded(self):
        return self.getPC() == self.getNumberOfInstructions()
    
    def getNumberOfInstructions(self):
        return self.getPCB().getNumberOfInstructions()
    
    def setNumberOfInstructions(self, n):
        self.getPCB().setNumberOfInstructions(n)
        
    def nextInstruction(self):
        self.setPC(self.getPC() + 1)