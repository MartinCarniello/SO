'''
Created on 02/07/2013

@author: martin
'''

from kernel.Interruptions import Interruption

class CPUToEndInterruption(Interruption):
    def interruptionMethod(self, kernel):
        kernel.removeProcessFromMemory(kernel.getCpu().getPCB())
        kernel.sendPCBFromCPUToEnd()
        kernel.restartQuantum()
        kernel.restartCPU()
        kernel.contextSwitch()