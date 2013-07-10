'''
Created on 06/07/2013

@author: martin
'''

from scheduler.ReadyPriority import ReadyPriority
from scheduler.ReadyFIFO import ReadyFIFO
from estructuraCpu.Cpu import Cpu
from temporizador.Clock import Clock
from EstructuraIO.IO import IO
from executionPolitic.Simple import Simple
from executionPolitic.RoundRobin import RoundRobin
from end.End import End
from kernel.Kernel import Kernel
from pcb.PCB import PCB
from pcb.PCBPriority import PCBPriority
from programaEInstrucciones.Instruction import Instruction
from memory.Memory import Memory
from process.Process import Process
from memory.ContinuosMapping import *
from memory.Memory import *
from memory.MemoryAllocation import *
from memory.MemoryBlock import *
from hdd.HardDisk import *
from shell.Shell import *
from shellAndConsoleExceptions.Exceptions import *
from consola.Consola import *

if __name__ == '__main__':
    
    freeBlock1 = Block(0, 49)
                
    freeBlocks = FreeBlock()
    freeBlocks.put(freeBlock1)
    

    occupedBlocks = OccupedBlock()
    

    memory = Memory(50)
           
    #Se puede elegir cualquiera de estas tres tecnicas
    
    firstFit = FirstFit(freeBlocks, occupedBlocks, memory)
    #bestFit = BestFit(freeBlocks, occupedBlocks, memory)
    #worstFit = WorstFit(freeBlocks, occupedBlocks, memory)
        
    ai1p1 = Instruction(True, "i1b1")
    ai2p1 = Instruction(True, "i2b1")
    ai3p1 = Instruction(False, "i3b1", 4)
    ai1p2 = Instruction(True, "i1b2")
    ai2p2 = Instruction(True, "i2b2")
    ai3p2 = Instruction(True, "i3b2")
    ai1p3 = Instruction(False, "i1b3", 5)
    ai2p3 = Instruction(True, "i2b3")
    ai3p3 = Instruction(True, "i3b3")
        
    page1a = [ai1p1, ai2p1, ai3p1]
    page2a = [ai1p2, ai2p2, ai3p2]
    page3a = [ai1p3, ai2p3, ai3p3]
        
    #Se puede poner la prioridad, pasandole por parametro al constructor un numero.
    #NOTA: La prioridad menor es mayor (EJ: 2 tiene mas prioridad que 3)
    #NOTA2: Si se le da prioridad, hay que cambiar la cola de ReadyFIFO por Priority.
    pagesProcessa = ProcessPages()
        
    pagesProcessa.getPages().append(page1a)
    pagesProcessa.getPages().append(page2a)
    pagesProcessa.getPages().append(page3a)
        
    bi1p1 = Instruction(True, "i1b2")
    bi2p1 = Instruction(True, "i2b2")
    bi1p2 = Instruction(True, "i1b3")
    bi2p2 = Instruction(True, "i2b3")
        
    page1b = [bi1p1, bi2p1]
    page2b = [bi1p2, bi2p2]
        
    #Se puede poner la prioridad, pasandole por parametro al constructor un numero.
    #NOTA: La prioridad menor es mayor (EJ: 2 tiene mas prioridad que 3)
    #NOTA2: Si se le da prioridad, hay que cambiar la cola de ReadyFIFO por Priority.
    pagesProcessb = ProcessPages() #Se puede poner la prioridad
        
    pagesProcessb.getPages().append(page1b)
    pagesProcessb.getPages().append(page2b)
    
    hdd = HDD()
    
    hdd.setPages({1: pagesProcessa, 2: pagesProcessb})
    
    #Si se eligio otro metodo de asignacion, hay que pasarle el mismo por parametro a la cpu.
    cpu = Cpu(firstFit)
    
    #La politica de ejecucion puede ser simple o round robin.
    #Si es round robin, se le pasa el quantum al constructor por parametro.
    policy = Simple()
    #policy = RoundRobin(2)
    
    #Si se le pusieron prioridad a las paginas del proceso, se debera seleccionar la cola con prioridad.
    scheduler = ReadyFIFO(cpu, policy)
    #scheduler = ReadyPriority(cpu, policy)
    
    #Si se eligio otro metodo de asignacion, hay que pasarle el mismo por parametro al dispositivo de IO.
    io = IO(firstFit)
    
    end = End()
    longTerm = LongTerm()
    longTerm.setHdd(hdd)
    
    #Si se eligio otro metodo de asignacion, hay que pasarle el mismo por parametro a la MMU.
    longTerm.setMmu(firstFit)

    clock = Clock()
    clock.addObserver(cpu)
    clock.addObserver(scheduler)

    consola = Console()

    kernel = Kernel(scheduler, cpu, io, end, clock, longTerm, consola.getShell())
            
    consola.run()