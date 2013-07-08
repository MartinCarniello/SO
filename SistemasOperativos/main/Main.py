'''
Created on 02/07/2013

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
    
    
    ins1p1 = Instruction(True, "resultado ins1p1")
    ins2p1 = Instruction(True, "resultado ins2p1")
    ins3p1 = Instruction(True, "resultado ins3p1")
    ins4p1 = Instruction(False, "resultado ins4p1", 10)
    instructionsP1 = [ins1p1, ins2p1, ins3p1, ins4p1]
    p1 = Process(1, instructionsP1)

    ins1p2 = Instruction(True, "resultado ins1p2")
    ins2p2 = Instruction(True, "resultado ins2p2")
    ins3p2 = Instruction(True, "resultado ins3p2")
    ins4p2 = Instruction(False, "resultado ins4p2", 5)
    instructionsP2 = [ins1p2, ins2p2, ins3p2, ins4p2]
    p2 = Process(2, instructionsP2)

    freeBlock1 = Block(0, 3)
    freeBlock2 = Block(6, 7)
    freeBlock3 = Block(10, 15)
        
    occupedBlock1 = Block(4, 5)
    occupedBlock2 = Block(8, 9)
    occupedBlock3 = Block(16, 20)
                
    freeBlocks = FreeBlock()
    freeBlocks.put(freeBlock1)
    freeBlocks.put(freeBlock2)
    freeBlocks.put(freeBlock3)

    pcb1 = PCB(0, 2)
    pcb2 = PCB(1, 8)
    pcb3 = PCB(2, 5)

    occupedBlocks = OccupedBlock()
    occupedBlocks.put(pcb1, occupedBlock1)
    occupedBlocks.put(pcb2, occupedBlock2)
    occupedBlocks.put(pcb3, occupedBlock3)

    hdd = HDD()

    memory = Memory()
    memory.putProcess(p1)
    memory.putProcess(p2)

    pcbP1 = PCB(1, len(p1.getInstructions()))
    pcbP2 = PCB(2, len(p2.getInstructions()))

    # pcbP1 = PCBPriority(pcbP1, 10)
    # pcbP2 = PCBPriority(pcbP2, 3)

    cpu = Cpu(memory)
    policy = Simple()
    # policy = RoundRobin(1)
    scheduler = ReadyFIFO(cpu, policy)
    # scheduler = ReadyPriority(cpu, policy)
    scheduler.put(pcbP1)
    scheduler.put(pcbP2)
    io = IO(memory)
    end = End()

    clock = Clock()
    clock.addObserver(cpu)
    clock.addObserver(scheduler)

    kernel = Kernel(scheduler, cpu, memory, io, end, clock)

    kernel.turnOn()