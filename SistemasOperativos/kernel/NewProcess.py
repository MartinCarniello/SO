'''
Created on 07/07/2013

@author: martin
'''

from kernel.Interruptions import Interruption

class NewProcess(Interruption):
    def __init__(self, pid):
        self.pid = pid
        
    def getPID(self):
        return self.pid
    
    def interruptionMethod(self, kernel):
        """Crea un nuevo proceso para enviarlo a la
           cola de Ready"""
        kernel.createNewProcess(self.getPID())