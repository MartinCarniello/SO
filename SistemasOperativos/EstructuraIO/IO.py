'''
Created on 27/04/2013

@author: Carne
'''

import threading
import time
from kernel.IOToReadyInterruption import IOToReadyInterruption
from kernel.IOToEndInterruption import IOToEndInterruption
from EstructuraIO.Waiting import Waiting
from time import gmtime, strftime

class IO(threading.Thread):
    def __init__(self, mmu):
        threading.Thread.__init__(self)
        self.pcb = None
        self.kernel = None
        self.waiting = Waiting()
        self.running = True
        self.mmu = mmu

    def getRunning(self):
        return self.running

    def setRunning(self, running):
        self.running = running

    def getWaiting(self):
        return self.waiting

    def getKernel(self):
        return self.kernel

    def setKernel(self, kernel):
        self.kernel = kernel

    def getPCB(self):
        return self.pcb

    def setPCB(self, pcb):
        self.pcb = pcb

    def getMmu(self):
        return self.mmu

    def restart(self):
        self.setPCB(None)

    def startUp(self):
        self.setRunning(True)
        self.start()

    def run(self):
        while(self.getRunning()):
            if self.getKernel().isUserMode() and (not self.getWaiting().isEmpty()):
                self.setPCB(self.getWaiting().get())

                pcbID = self.getPCB().getPID()
                pcbPC = self.getPCB().getPC()

                ins = self.getMmu().fetchInstruction(self.getPCB())

                print("Se esta ejecutando la instruccion " + str(pcbPC) + " del proceso " + str(pcbID) + " en I/O")
                print(strftime("%a, %d %b %Y %X +0000", gmtime()).rsplit()[4] + " El resultado es: " + ins.getResult())
                self.getPCB().nextInstruction()

                self.instructionExecute(ins)

                print("Se termino de ejecutar la instruccion " + str(pcbPC) + " del proceso " + str(pcbID) + " en I/O")

                if self.getPCB().isEnded():
                    self.getKernel().handle(IOToEndInterruption())
                else:
                    self.getKernel().handle(IOToReadyInterruption())

    def instructionExecute(self, instruction):
        time.sleep(instruction.getTime())