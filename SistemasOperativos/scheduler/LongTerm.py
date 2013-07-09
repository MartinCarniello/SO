'''
Created on 06/07/2013

@author: martin
'''

from kernel.AddProcessToReadyQueue import AddProcessToReadyQueue
from shellAndConsoleExceptions.Exceptions import *

class LongTerm():
    
    def __init__(self):
        self.mmu = None
        self.hdd = None
        self.kernel = None
        
    def getKernel(self):
        return self.kernel
    
    def setKernel(self, kernel):
        self.kernel = kernel
        
    def getMmu(self):
        return self.mmu
    
    def setMmu(self, mmu):
        self.mmu = mmu
        
    def getHdd(self):
        return self.hdd
    
    def setHdd(self, hdd):
        self.hdd = hdd
        
    def load(self, pid):
        pcb = self.getMmu().load(self.getBlockList(pid), pid)
        
        if pcb != None:
            self.getKernel().handle(AddProcessToReadyQueue(pcb))
            
        else:
            raise NoSpaceInMemory

    def getBlockList(self, pid):
        return self.getHdd().getProcessPages(pid)
    
    def removeProcess(self, pcb):
        self.getMmu().removeProcess(pcb)