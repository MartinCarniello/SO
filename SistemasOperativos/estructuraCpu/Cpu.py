'''
Created on 27/04/2013

@author: Carne
'''

from kernel.CPUToEndInterruption import CPUToEndInterruption
from kernel.CPUToIOInterruption import CPUToIOInterruption
import logging

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

                logging.basicConfig(filename='../executionLog.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
                logging.info('Se esta ejecutando la instruccion ' + str(pcbPC + 1) + ' del proceso ' + str(pcbID) + ' en CPU')
                logging.info("El resultado es: " + ins.getResult())
                
                self.getPCB().nextInstruction()

                if self.getPCB().isEnded():
                    logging.info("El proceso " + str(pcbID) + " ha terminado")
                    print("El proceso con ID " + str(pcbID) + " se ha terminado de ejecutar")

                    self.getKernel().handle(CPUToEndInterruption())

            else:
                logging.info("La instruccion " + str(pcbPC) + " del proceso " + str(pcbID) + " ha ido a ejecutarse en I/O")

                self.getKernel().handle(CPUToIOInterruption())



    def instructionExecute(self, instruction):
        pass