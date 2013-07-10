'''
Created on 08/06/2013

@author: martin
'''

class MMU():

    """Getters y Setters"""
    def getMemory(self):
        return self.memory

    def setMemory(self, memory):
        self.memory = memory
    
    
    """Constructor"""
    def __init__(self, mem):
        self.memory = mem


    def swapOut(self, programInstructions, pcb):
        pass

    def swapIn(self, blockList, pid):
        pass