'''
Created on 02/07/2013

@author: martin
'''

from kernel.Interruptions import Interruption

class IOToEndInterruption(Interruption):
    def interruptionMethod(self, kernel):
        kernel.sendPCBFromIOToEnd()
        kernel.restartIO()