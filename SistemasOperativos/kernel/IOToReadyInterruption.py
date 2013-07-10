'''
Created on 02/07/2013

@author: martin
'''

from kernel.Interruptions import Interruption

class IOToReadyInterruption(Interruption):
    def interruptionMethod(self, kernel):
        """Envia el pcb a la cola de Ready,
           restartea el dispositivo de IO,
           y si la cpu no esta ejecutando 
           ningun proceso, hace un contextSwitch"""
        kernel.sendPCBToReady()
        kernel.restartIO()
        if not kernel.getCpu().isOccuped():
            kernel.contextSwitch()