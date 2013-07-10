'''
Created on 02/07/2013

@author: martin
'''

from kernel.Interruptions import Interruption

class TimeOutInterruption(Interruption):
    def interruptionMethod(self, kernel):
        """Hace un contextSwitch y restartea el
           Quantum de la politica de ejecucion"""
        kernel.contextSwitch()
        kernel.restartQuantum()