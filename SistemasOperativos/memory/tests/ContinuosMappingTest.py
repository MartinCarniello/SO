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