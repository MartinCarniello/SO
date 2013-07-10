'''
Created on 04/05/2013

@author: Carne
'''

class PCB():
    
    """Getters y Setters"""
    def getBase(self):
        return self.base
    
    def setBase(self, base):
        self.base = base
        
    def getLimit(self):
        return self.limit
    
    def setLimit(self, limit):
        self.limit = limit
    
    def setNumberOfInstructions(self, n):
        self.numberOfInstructions = n
        
    def setPC(self, p):
        self.pc = p
        
    def getNumberOfInstructions(self):
        return self.numberOfInstructions
        
    def getPC(self):
        return self.pc

    def setPID(self, p):
        self.pid = p
        
    def getPID(self):
        return self.pid


    """Constructor"""
    def __init__(self, pid, nInstructions=None, base=None, limit=None):
        self.setPC(0)
        self.setPID(pid)
        self.setNumberOfInstructions(nInstructions)
        self.base = base
        self.limit = limit
        
        
    def isEnded(self):
        return self.getPC() == self.getNumberOfInstructions()
        
    def nextInstruction(self):
        self.setPC(self.getPC() + 1)