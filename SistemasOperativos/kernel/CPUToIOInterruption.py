'''
Created on 02/07/2013

@author: martin
'''

from kernel.Interruptions import Interruption

class CPUToIOInterruption(Interruption):
    def interruptionMethod(self, kernel):
        """Manda el pcb a la cola de espera de IO,
           restartea el cuantum de la politica de
           ejecucion, restartea la cpu y hace un
           contextSwitch"""
        kernel.sendPCBToWaiting()
        kernel.restartQuantum()
        kernel.restartCPU()
        kernel.contextSwitch()