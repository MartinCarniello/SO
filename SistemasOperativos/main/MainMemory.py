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
    #freeBlock2 = Block(31, 40)
    #freeBlock3 = Block(51, 56)
        
    #occupedBlock1 = Block(6, 30)
    #occupedBlock2 = Block(41, 50)
    #occupedBlock3 = Block(57, 59)
                
    freeBlocks = FreeBlock()
    freeBlocks.put(freeBlock1)
    #freeBlocks.put(freeBlock2)
    #freeBlocks.put(freeBlock3)
                
    occupedBlocks = OccupedBlock()
    #occupedBlocks.put(mock(), occupedBlock1)
    #occupedBlocks.put(mock(), occupedBlock2)
    #occupedBlocks.put(mock(), occupedBlock3)
        
    memory = Memory(50)
           
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
        
    pagesProcessa = ProcessPages()
        
    pagesProcessa.getPages().append(page1a)
    pagesProcessa.getPages().append(page2a)
    pagesProcessa.getPages().append(page3a)
        
    bi1p1 = Instruction(False, "i1b2", 10)
    bi2p1 = Instruction(True, "i2b2")
    bi1p2 = Instruction(True, "i1b3")
    bi2p2 = Instruction(True, "i2b3")
        
    page1b = [bi1p1, bi2p1]
    page2b = [bi1p2, bi2p2]
        
    pagesProcessb = ProcessPages()
        
    pagesProcessb.getPages().append(page1b)
    pagesProcessb.getPages().append(page2b)
    
    hdd = HDD()
    
    hdd.setPages({1: pagesProcessa, 2: pagesProcessb})
    
    cpu = Cpu(firstFit)
    policy = Simple()
    # policy = RoundRobin(1)
    scheduler = ReadyFIFO(cpu, policy)
    # scheduler = ReadyPriority(cpu, policy)
    io = IO(firstFit)
    end = End()
    longTerm = LongTerm()
    longTerm.setHdd(hdd)
    longTerm.setMmu(firstFit)

    clock = Clock()
    clock.addObserver(cpu)
    clock.addObserver(scheduler)

    consola = Console()

    kernel = Kernel(scheduler, cpu, io, end, clock, longTerm, consola.getShell())
            
    consola.run()