'''
Created on 27/04/2013

@author: Carne
'''

from kernel.CPUToEndInterruption import CPUToEndInterruption
from kernel.CPUToIOInterruption import CPUToIOInterruption
from time import gmtime, strftime

class Cpu():

    def getPCB(self):
        return self.pcb

    def setPCB(self, pcb):
        self.pcb = pcb

    def getMmu(self):
        return self.mmu

    def getKernel(self):
        return self.kernel

    def setKernel(self, kernel):
        self.kernel = kernel

    def setOccuped(self, value):
        self.occuped = value

    def isOccuped(self):
        return self.occuped

    def __init__(self, mmu):
        self.occuped = False
        self.kernel = None
        self.pcb = None
        self.mmu = mmu

    def restart(self):
        self.setPCB(None)
        self.setOccuped(False)

    def contextSwitch(self, pcb):
        self.setPCB(pcb)
        self.setOccuped(True)

    def executionCycle(self):
        if self.isOccuped() and self.getKernel().isUserMode():

            pcbID = self.getPCB().getPID()
            pcbPC = self.getPCB().getPC()

            ins = self.getMmu().fetchInstruction(self.getPCB())

            if ins.isCpuInstruction():
                # self.instructionExecute(ins)
                print("Se esta ejecutando la instruccion " + str(pcbPC + 1) + " del proceso " + str(pcbID) + " en CPU")
                print(strftime("%a, %d %b %Y %X +0000", gmtime()).rsplit()[4] + " El resultado es: " + ins.getResult())
                self.getPCB().nextInstruction()

                if self.getPCB().isEnded():
                    print("El proceso " + str(pcbID) + " ha terminado")
                    self.getKernel().handle(CPUToEndInterruption())

            else:
                print("La instruccion " + str(pcbPC) + " del proceso " + str(pcbID) + " ha ido a ejecutarse en I/O")
                self.getKernel().handle(CPUToIOInterruption())



    def instructionExecute(self, instruction):
        pass