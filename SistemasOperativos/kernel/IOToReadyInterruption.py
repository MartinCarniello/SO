'''
Created on 02/07/2013

@author: martin
'''

from kernel.Interruptions import Interruption

class IOToReadyInterruption(Interruption):
    def interruptionMethod(self, kernel):
        kernel.sendPCBToReady()
        kernel.restartIO()
        if not kernel.getCpu().isOccuped():
            kernel.contextSwitch()