'''
Created on 10/06/2013

@author: usuario
'''

class Block():
    
    """Getters y Setters"""
    def getBase(self):
        return self.base
    
    def getLimit(self):
        return self.limit
    
    def setBase(self, base):
        self.base = base
        
    def setLimit(self, limit):
        self.limit = limit
    
    """Constructor"""
    def __init__(self, base, limit):
        self.base = base
        self.limit = limit
        
    
    def size(self):
        return self.getLimit() - self.getBase() + 1
    
class FreeBlock():

    """Getters y Setters"""
    def getBlocks(self):
        return self.blocks
    
    """Constructor"""
    def __init__(self):
        self.blocks = []
        

    
    def put(self, aBlock):
        self.getBlocks().append(aBlock)
        
    def remove(self, aBlock):
        self.getBlocks().remove(aBlock)
        
    def get(self, index):
        return self.getBlocks()[index]
        
    def size(self):
        return len(self.getBlocks())
    
class OccupedBlock():
    
    """Getters y Setters"""
    def getBlocks(self):
        return self.blocks
    
    """Constructor"""
    def __init__(self):
        self.blocks = []
        
    
    def put(self, pcb, aBlock):
        self.getBlocks().append((pcb, aBlock))
        
    def get(self, pid):
        for block in self.getBlocks():
            if pid == block[0]:
                return block
    
    def getPCB(self):
        return self.pcb
    
    def size(self):
        return len(self.getBlocks())