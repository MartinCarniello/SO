'''
Created on 04/05/2013

@author: Carne
'''

class ExecutionPolitic():
    
    """Getters y Setters"""
    def getKernel(self):
        return self.kernel
    
    def setKernel(self, kernel):
        self.kernel = kernel
        
    
    """Constructor"""
    def __init__(self, kernel=None):
        self.kernel = kernel
        
    def restartQuantum(self):
        pass