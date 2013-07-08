'''
Created on 04/05/2013

@author: Carne
'''

from executionPolitic.ExecutionPolitic import ExecutionPolitic
from kernel.TimeOutInterruption import TimeOutInterruption

class RoundRobin(ExecutionPolitic):
    def __init__(self, quantum, kernel=None):
        ExecutionPolitic.__init__(self, kernel)
        self.quantum = quantum
        self.actual = 0

    def getActual(self):
        return self.actual

    def setActual(self, value):
        self.actual = value

    def getQuantum(self):
        return self.quantum

    def nextActual(self):
        self.setActual(self.getActual() + 1)

    def restartQuantum(self):
        self.setActual(0)

    def executionCycle(self):
        self.nextActual()

        if self.getActual() == self.getQuantum():
            self.getKernel().handle(TimeOutInterruption())