'''
Created on 11/05/2013

@author: Carne
'''

class Interruption():
    def doIt(self, kernel):
        """Pasa a modo kernel para que todo los componentes
           dejen de procesar, hace lo que debe hacer,
           correspondiendo a una interrupcion en particular
           y vuelve a modo usuario"""
        kernel.turnToKernelMode()
        self.interruptionMethod(kernel)
        kernel.turnToUserMode()
        
    def interruptionMethod(self):
        pass