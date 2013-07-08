'''
Created on 25/05/2013

@author: Carne
'''

class Process():
    def __init__(self, id, instructions):
        self.id = id
        self.instructions = instructions
        
    def getID(self):
        return self.id
    
    def getInstructions(self):
        return self.instructions