'''
Created on 06/07/2013

@author: martin
'''

from kernel.AddProcessToReadyQueue import AddProcessToReadyQueue
from shellAndConsoleExceptions.Exceptions import *

class LongTerm():
    
    """Getters y Setters"""
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
    
    """Constructor"""
    def __init__(self):
        self.mmu = None
        self.hdd = None
        self.kernel = None
        
        
    def load(self, pid):
        """Pide al hdd que le de la lista de paginas de un
           proceso con un id determinado. Se lo entrega a la
           mmu para que lo asigne en memoria. Si la mmu
           le retorna None, quiere decir que no habia memoria, 
           por eso levanta una excepcion"""
        pcb = self.getMmu().load(self.getBlockList(pid), pid)
        
        if pcb != None:
            self.getKernel().handle(AddProcessToReadyQueue(pcb))
            
        else:
            raise NoSpaceInMemory

    def getBlockList(self, pid):
        return self.getHdd().getProcessPages(pid)
    
    def removeProcess(self, pcb):
        self.getMmu().removeProcess(pcb)