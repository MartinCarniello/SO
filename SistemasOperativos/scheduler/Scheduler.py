'''
Created on 27/04/2013

@author: Carne
'''

class Scheduler():
    
    def __init__(self, cpu, politic):
        self.cpu = cpu
        self.executionPolitic = politic
        
    def getCpu(self):
        return self.cpu

    def isEmpty(self):
        return self.getQueue().qsize() == 0

    def put(self):
        pass
    
    def get(self):
        pass
    
    def getExecutionPolitic(self):
        return self.executionPolitic
    
    def restartQuantum(self):
        self.getExecutionPolitic().restartQuantum()
    
    def contextSwitch(self):
        if self.getCpu().isOccuped():
            self.put(self.getCpu().getPCB())
            
        self.getCpu().restart()
        
        if not self.isEmpty():
            self.getCpu().contextSwitch(self.get())
            
    def executionCycle(self):
        self.getExecutionPolitic().executionCycle()