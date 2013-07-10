'''
Created on 02/07/2013

@author: martin
'''

from kernel.Interruptions import Interruption

class CPUToEndInterruption(Interruption):
    def interruptionMethod(self, kernel):
        """Remueve el proceso de la memoria logica,
           manda el pcb a la cola de End, restartea
           el Quantum de la politica de ejecucion,
           restartea la cpu y hace un contextSwitch"""
        kernel.removeProcessFromMemory(kernel.getCpu().getPCB())
        kernel.sendPCBFromCPUToEnd()
        kernel.restartQuantum()
        kernel.restartCPU()
        kernel.contextSwitch()