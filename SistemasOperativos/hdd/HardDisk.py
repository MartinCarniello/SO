'''
Created on 24/06/2013

@author: usuario
'''

from shellAndConsoleExceptions.Exceptions import IncorrectID

class HDD:
    
    """Getters y Setters"""
    def getPages(self):
        return self.pages
    
    def setPages(self, pages):
        self.pages = pages
    
    
    """Constructor"""
    def __init__(self):
        self.pages = {}
        
        
    def getProcessPages(self, pid):
        """Devuelve las paginas de un proceso asociado al pid.
           Si el pid no existe, levanta una excepcion."""
        if self.getPages().has_key(pid):
            return self.getPages()[pid]
        else:
            raise IncorrectID
        
    
class ProcessPages():

    """Getters y Setters"""    
    def getPriority(self):
        return self.priority
    
    def setPriority(self, priority):
        self.priority = priority
        
    def getPages(self):
        return self.pages

    def setPages(self, pages):
        self.pages = pages

    
    
    """Constructor"""
    def __init__(self, priority=None):
        self.pages = []
        self.priority = priority
        
            
    def getPage(self, nPage):
        return self.getPages()[nPage]
    
    def setPage(self, nPage, page):
        return self.getPages()[nPage].set(page)
    
    def size(self):
        """Devuelve el tamanho de entero del proceso, es decir
           la suma de todas las instrucciones, de todas las paginas"""
        instructionsSize = 0
        for page in self.getPages():
            instructionsSize += len(page)
            
        return instructionsSize