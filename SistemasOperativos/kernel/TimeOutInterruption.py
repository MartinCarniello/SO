'''
Created on 02/07/2013

@author: martin
'''

from kernel.Interruptions import Interruption

class TimeOutInterruption(Interruption):
    def interruptionMethod(self, kernel):
        kernel.contextSwitch()
        kernel.restartQuantum()