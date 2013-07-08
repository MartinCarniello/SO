'''
Created on 24/06/2013

@author: usuario
'''

from shellAndConsoleExceptions.Exceptions import IncorrectID

class HDD:
    def __init__(self):
        self.pages = {}
        
    def getPages(self):
        return self.pages
    
    def setPages(self, pages):
        self.pages = pages
        
    def getProcessPages(self, pid):

        if self.getPages().has_key(pid):
            return self.getPages()[pid]
        else:
            raise IncorrectID
        
    
class ProcessPages():
    def __init__(self):
        self.pages = []
        
    def getPages(self):
        return self.pages

    def setPages(self, pages):
        self.pages = pages
        
    def getPage(self, nPage):
        return self.getPages()[nPage]
    
    def setPage(self, nPage, page):
        return self.getPages()[nPage].set(page)
    
    def size(self):
        
        instructionsSize = 0
        for page in self.getPages():
            instructionsSize += len(page)
            
        return instructionsSize