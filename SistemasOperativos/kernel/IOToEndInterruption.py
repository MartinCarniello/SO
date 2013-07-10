'''
Created on 02/07/2013

@author: martin
'''

from kernel.Interruptions import Interruption

class IOToEndInterruption(Interruption):
    def interruptionMethod(self, kernel):
        """Saca el proceso de la memoria logica,
           manda el pcb a la cola de End, y
           restartea el dispositivo de IO."""
        kernel.removeProcessFromMemory(kernel.getIO().getPCB())
        kernel.sendPCBFromIOToEnd()
        kernel.restartIO()