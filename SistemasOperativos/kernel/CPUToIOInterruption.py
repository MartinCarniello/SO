'''
Created on 02/07/2013

@author: martin
'''

from kernel.Interruptions import Interruption

class CPUToIOInterruption(Interruption):
    def interruptionMethod(self, kernel):
        kernel.sendPCBToWaiting()
        kernel.restartQuantum()
        kernel.restartCPU()
        kernel.contextSwitch()