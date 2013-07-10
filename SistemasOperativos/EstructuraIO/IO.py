'''
Created on 27/04/2013

@author: Carne
'''

import threading
import time
from kernel.IOToReadyInterruption import IOToReadyInterruption
from kernel.IOToEndInterruption import IOToEndInterruption
from EstructuraIO.Waiting import Waiting
import logging

class IO(threading.Thread):

    """Getters y Setters"""    
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

    
    """Constructor"""
    def __init__(self, mmu):
        threading.Thread.__init__(self)
        self.pcb = None
        self.kernel = None
        self.waiting = Waiting()
        self.running = True
        self.mmu = mmu

    
    def restart(self):
        self.setPCB(None)

    def startUp(self):
        """Hace un start del thread"""
        self.setRunning(True)
        self.start()

    def run(self):
        """Esta corriendo en un loop infinito, y cuando la cola de waiting tiene
           pcbs para ejecutarlos, los toma y los ejecuta. Levanta interrupciones
           cuando termina de ejecutar un ciclo, si el pcb no tiene mas instrucciones
           para ejecutar, envia el pcb a End, de lo contrario lo envia a Ready. Loguea
           la informacion de la ejecucion en un archivo en la carpeta src llamado
           executionLog.log"""
        while(self.getRunning()):
            if self.getKernel().isUserMode() and (not self.getWaiting().isEmpty()):
                self.setPCB(self.getWaiting().get())

                pcbID = self.getPCB().getPID()
                pcbPC = self.getPCB().getPC()

                ins = self.getMmu().fetchInstruction(self.getPCB())

                logging.basicConfig(filename='../executionLog.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

                logging.info("Se esta ejecutando la instruccion " + str(pcbPC) + " del proceso " + str(pcbID) + " en I/O")
                logging.info("El resultado es: " + ins.getResult())
                
                self.getPCB().nextInstruction()

                self.instructionExecute(ins)

                logging.info("Se termino de ejecutar la instruccion " + str(pcbPC) + " del proceso " + str(pcbID) + " en I/O")

                if self.getPCB().isEnded():
                    print("El proceso con ID " + str(pcbID) + " se ha terminado de ejecutar")
                    self.getKernel().handle(IOToEndInterruption())
                else:
                    self.getKernel().handle(IOToReadyInterruption())

    def instructionExecute(self, instruction):
        time.sleep(instruction.getTime())