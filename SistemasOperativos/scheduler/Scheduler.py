'''
Created on 27/04/2013

@author: Carne
'''

class Scheduler():

    """Getters y Setters"""    
    def getCpu(self):
        return self.cpu

    def getExecutionPolitic(self):
        return self.executionPolitic
    
    """Constructor"""
    def __init__(self, cpu, politic):
        self.cpu = cpu
        self.executionPolitic = politic
        
    
    def isEmpty(self):
        return self.getQueue().qsize() == 0

    def put(self):
        pass
    
    def get(self):
        pass
    
    def restartQuantum(self):
        self.getExecutionPolitic().restartQuantum()
    
    def contextSwitch(self):
        """Si la cpu esta ocupada, saca el pcb que
           tiene asociado y lo asocia en la cola de Ready.
           Restartea la cpu y si la cola de Ready no esta
           vacia, le envia un pcb a la cpu para que comience
           con la ejecucion"""
        if self.getCpu().isOccuped():
            self.put(self.getCpu().getPCB())
            
        self.getCpu().restart()
        
        if not self.isEmpty():
            self.getCpu().contextSwitch(self.get())
            
    def executionCycle(self):
        self.getExecutionPolitic().executionCycle()