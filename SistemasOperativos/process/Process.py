'''
Created on 25/05/2013

@author: Carne
'''

class Process():
    
    """Getters y Setters"""
    def getID(self):
        return self.id
    
    def getInstructions(self):
        return self.instructions
    
    """Constructor"""
    def __init__(self, id, instructions):
        self.id = id
        self.instructions = instructions