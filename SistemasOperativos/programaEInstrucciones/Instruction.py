'''
Created on 25/05/2013

@author: Carne
'''

class Instruction():
    def __init__(self, cpuInstruction, result, time=None):
        self.cpuInstruction = cpuInstruction
        self.result = result
        self.time = time
        
    def isCpuInstruction(self):
        return self.cpuInstruction
    
    def getResult(self):
        return self.result
    
    def getTime(self):
        return self.time