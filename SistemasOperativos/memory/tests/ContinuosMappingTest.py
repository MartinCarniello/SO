'''
Created on 21/06/2013

@author: martin
'''

from unittest import TestCase
from mockito import *
from memory.ContinuosMapping import *
from memory.MemoryBlock import *
from pcb.PCB import PCB
from memory.Memory import Memory
from programaEInstrucciones.Instruction import Instruction
from hdd.HardDisk import *

class TestContinuosMapping(TestCase):
    
    def setUp(self):
        freeBlock1 = Block(0, 5)
        freeBlock2 = Block(31, 40)
        freeBlock3 = Block(51, 56)
        
        occupedBlock1 = Block(6, 30)
        occupedBlock2 = Block(41, 50)
        occupedBlock3 = Block(57, 59)
                
        freeBlocks = FreeBlock()
        freeBlocks.put(freeBlock1)
        freeBlocks.put(freeBlock2)
        freeBlocks.put(freeBlock3)
                
        occupedBlocks = OccupedBlock()
        occupedBlocks.put(mock(), occupedBlock1)
        occupedBlocks.put(mock(), occupedBlock2)
        occupedBlocks.put(mock(), occupedBlock3)
        
        self.memory = Memory(60)
            
        self.firstFit = FirstFit(freeBlocks, occupedBlocks, self.memory)
        self.bestFit = BestFit(freeBlocks, occupedBlocks, self.memory)
        self.worstFit = WorstFit(freeBlocks, occupedBlocks, self.memory)
        
        self.ai1p1 = Instruction(True, "i1b1")
        ai2p1 = Instruction(True, "i2b1")
        ai3p1 = Instruction(True, "i3b1")
        ai1p2 = Instruction(True, "i1b2")
        ai2p2 = Instruction(True, "i2b2")
        ai3p2 = Instruction(True, "i3b2")
        ai1p3 = Instruction(True, "i1b3")
        ai2p3 = Instruction(True, "i2b3")
        self.ai3p3 = Instruction(True, "i3b3")
        
        page1a = [self.ai1p1, ai2p1, ai3p1]
        page2a = [ai1p2, ai2p2, ai3p2]
        page3a = [ai1p3, ai2p3, self.ai3p3]
        
        self.pagesProcessa = ProcessPages()
        
        self.pagesProcessa.getPages().append(page1a)
        self.pagesProcessa.getPages().append(page2a)
        self.pagesProcessa.getPages().append(page3a)
        
        self.bi1p1 = Instruction(True, "i1b2")
        bi2p1 = Instruction(True, "i2b2")
        bi1p2 = Instruction(True, "i1b3")
        self.bi2p2 = Instruction(True, "i2b3")
        
        page1b = [self.bi1p1, bi2p1]
        page2b = [bi1p2, self.bi2p2]
        
        self.pagesProcessb = ProcessPages()
        
        self.pagesProcessb.getPages().append(page1b)
        self.pagesProcessb.getPages().append(page2b)
    
    def testGetFreeBlockFirsFit(self):

        self.assertEqual(self.firstFit.getFreeBlock(3).getBase(), 0)
        self.assertEqual(self.firstFit.getFreeBlock(3).getLimit(), 5)
        
        self.assertEqual(self.firstFit.getFreeBlock(7).getBase(), 31)
        self.assertEqual(self.firstFit.getFreeBlock(7).getLimit(), 40)
        
        
        
    def testFreeBlockBestFit(self):
                
        self.assertEqual(self.bestFit.getFreeBlock(5).getBase(), 51)
        self.assertEqual(self.bestFit.getFreeBlock(5).getLimit(), 56)
        
    
    def testFreeBloockWorstFit(self):
        
        self.assertEqual(self.worstFit.getFreeBlock(2).getBase(), 31)
        self.assertEqual(self.worstFit.getFreeBlock(2).getLimit(), 40)
        
    def testLoadFirstFit(self):
        
        pcb1 = self.firstFit.load(self.pagesProcessa, 1)
        
        self.assertEqual(pcb1.getPID(), 1)
        self.assertEqual(pcb1.getBase(), 31)
        self.assertEqual(pcb1.getLimit(), 39)
        
        self.assertEqual(self.memory.getMemoryFrames()[31], self.ai1p1)
        self.assertEqual(self.memory.getMemoryFrames()[39], self.ai3p3)
        
        
        pcb2 = self.firstFit.load(self.pagesProcessb, 2)
        
        self.assertEqual(pcb2.getPID(), 2)
        self.assertEqual(pcb2.getBase(), 0)
        self.assertEqual(pcb2.getLimit(), 3)
        
        self.assertEqual(self.memory.getMemoryFrames()[0], self.bi1p1)
        self.assertEqual(self.memory.getMemoryFrames()[3], self.bi2p2)
        
    def testLoadBestFit(self):
        
        pcb1 = self.bestFit.load(self.pagesProcessa, 1)
        
        self.assertEqual(pcb1.getPID(), 1)
        self.assertEqual(pcb1.getBase(), 31)
        self.assertEqual(pcb1.getLimit(), 39)
        
        self.assertEqual(self.memory.getMemoryFrames()[31], self.ai1p1)
        self.assertEqual(self.memory.getMemoryFrames()[39], self.ai3p3)
        
        pcb2 = self.bestFit.load(self.pagesProcessb, 2)
        
        self.assertEqual(pcb2.getPID(), 2)
        self.assertEqual(pcb2.getBase(), 51)
        self.assertEqual(pcb2.getLimit(), 54)
        
        self.assertEqual(self.memory.getMemoryFrames()[51], self.bi1p1)
        self.assertEqual(self.memory.getMemoryFrames()[54], self.bi2p2)
        
    def testLoadWorstFit(self):
        
        pcb1 = self.worstFit.load(self.pagesProcessa, 1)
        
        self.assertEqual(pcb1.getPID(), 1)
        self.assertEqual(pcb1.getBase(), 31)
        self.assertEqual(pcb1.getLimit(), 39)
        
        self.assertEqual(self.memory.getMemoryFrames()[31], self.ai1p1)
        self.assertEqual(self.memory.getMemoryFrames()[39], self.ai3p3)
        
        pcb2 = self.worstFit.load(self.pagesProcessb, 2)
        
        self.assertEqual(pcb2.getPID(), 2)
        self.assertEqual(pcb2.getBase(), 0)
        self.assertEqual(pcb2.getLimit(), 3)
        
        self.assertEqual(self.memory.getMemoryFrames()[0], self.bi1p1)
        self.assertEqual(self.memory.getMemoryFrames()[3], self.bi2p2)
        
    def testMemoryCompact(self):
        
        i1p1 = Instruction(True, "i1p1")
        i2p1 = Instruction(True, "i2p1")
        i3p1 = Instruction(True, "i3p1")
        
        i1p2 = Instruction(True, "i1p2")
        i2p2 = Instruction(True, "i2p2")
        
        i1p3 = Instruction(True, "i1p3")
        i2p3 = Instruction(True, "i2p3")
        i3p3 = Instruction(True, "i3p3")
        i4p3 = Instruction(True, "i4p3")
        
        freeBlock1 = Block(0, 5)
        freeBlock2 = Block(9, 31)
        freeBlock3 = Block(34, 40)
        freeBlock4 = Block(45, 59)
        
        occupedBlock1 = Block(6, 8)
        occupedBlock2 = Block(32, 33)
        occupedBlock3 = Block(41, 44)
                
        freeBlocks = FreeBlock()
        freeBlocks.put(freeBlock1)
        freeBlocks.put(freeBlock2)
        freeBlocks.put(freeBlock3)
        freeBlocks.put(freeBlock4)
        
        pcb1 = PCB(1, 3, 6, 8)
        pcb2 = PCB(2, 2, 32, 33)
        pcb3 = PCB(3, 4, 41, 44)
                
        occupedBlocks = OccupedBlock()
        occupedBlocks.put(pcb1, occupedBlock1)
        occupedBlocks.put(pcb2, occupedBlock2)
        occupedBlocks.put(pcb3, occupedBlock3)
        
        memory = Memory(60)
        
        memory.getMemoryFrames()[6] = i1p1
        memory.getMemoryFrames()[7] = i2p1
        memory.getMemoryFrames()[8] = i3p1
        
        memory.getMemoryFrames()[32] = i1p2
        memory.getMemoryFrames()[33] = i2p2

        memory.getMemoryFrames()[41] = i1p3
        memory.getMemoryFrames()[42] = i2p3
        memory.getMemoryFrames()[43] = i3p3
        memory.getMemoryFrames()[44] = i4p3

        firstFit = FirstFit(freeBlocks, occupedBlocks, memory)

        firstFit.memoryCompact()
        
        #print(memory.getMemoryFrames()[0])
        #print(pcb1.getBase())
        #print(pcb1.getLimit())
        #print(pcb2.getBase())
        #print(pcb2.getLimit())
        #print(pcb3.getBase())
        #print(pcb3.getLimit())
        
        #print("Bloques")
        #print("libres")
        #print(firstFit.getFreeBlocks().getBlocks()[0].getBase())
        #print(firstFit.getFreeBlocks().getBlocks()[0].getLimit())
        #print("ocupados")
        #print(firstFit.getOccupedBlocks().getBlocks()[0][1].getBase())
        #print(firstFit.getOccupedBlocks().getBlocks()[0][1].getLimit())
        #print(firstFit.getOccupedBlocks().getBlocks()[1][1].getBase())
        #print(firstFit.getOccupedBlocks().getBlocks()[1][1].getLimit())
        #print(firstFit.getOccupedBlocks().getBlocks()[2][1].getBase())
        #print(firstFit.getOccupedBlocks().getBlocks()[2][1].getLimit())