'''
Created on 08/06/2013

@author: martin
'''

class MMU():
    def __init__(self, mem):
        self.memory = mem

    def getMemory(self):
        return self.memory

    def setMemory(self, memory):
        self.memory = memory

    def swapOut(self, programInstructions, pcb):
        pass

    def swapIn(self, blockList, pid):
        pass