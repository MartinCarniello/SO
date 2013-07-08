'''
Created on 11/05/2013

@author: Carne
'''

class Interruption():
    def doIt(self, kernel):
        kernel.turnToKernelMode()
        self.interruptionMethod(kernel)
        kernel.turnToUserMode()
        
    def interruptionMethod(self):
        pass