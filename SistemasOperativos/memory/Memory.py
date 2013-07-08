'''
Created on 25/05/2013

@author: Carne
'''

class Memory():

    def __init__(self, size):
        self.size = size
        self.memoryFrames = []
        
        i = 0
        
        while i < size:
            self.memoryFrames.append(None)
            i += 1
            
     
    def getMemoryFrames(self):
        return self.memoryFrames
     
    def setMemoryFrames(self, memory):
        self.memoryFrames = memory
        
    def getSize(self):
        return self.size
    
    def setSize(self, size):
        self.size = size
    
    def assignInMemory(self, blockList, memBase):
        
        index = memBase
        
        for block in blockList.getPages():
            for instruction in block:
                self.getMemoryFrames()[index] = instruction
                index += 1