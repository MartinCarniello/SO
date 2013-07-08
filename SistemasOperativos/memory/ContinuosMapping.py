'''
Created on 10/06/2013

@author: usuario
'''

from memory.MemoryAllocation import MMU
from memory.MemoryBlock import FreeBlock
from memory.MemoryBlock import OccupedBlock
from memory.MemoryBlock import Block
from pcb.PCB import PCB

class ContinuosMapping(MMU):
    def __init__(self, freeBlocks, occupedBlocks, memory):
        MMU.__init__(self, memory)
        self.freeBlocks = freeBlocks
        self.occupedBlocks = occupedBlocks
        
    def getMemory(self):
        return self.memory
    
    def setMemory(self, memory):
        self.memory = memory

    def putFreeBlock(self, aFreeBlock):
        self.getFreeBlocks().put(aFreeBlock)

    def putOccupedBlock(self, anOccupedBlock):
        self.getOccupedBlocks().put(anOccupedBlock)

    def getFreeBlocks(self):
        return self.freeBlocks

    def getOccupedBlocks(self):
        return self.occupedBlocks

    def getSizeOfBiggestBlock(self):
        blockSize = 0

        for block in self.getFreeBlocks().getBlocks():
            if block.size() > blockSize:
                blockSize = block.size()

        return blockSize

    def getFreeSpace(self):
        freeSpace = 0

        for b in self.getFreeBlocks().getBlocks():
            freeSpace = freeSpace + b.size()

        return freeSpace

    def memoryCompact(self):

        firstBlock = self.getOccupedBlocks().getBlocks()[0]

        if firstBlock[1].getBase() != 0:

            sizeOfFirstBlock = firstBlock[1].size()

            base = 0
            limit = sizeOfFirstBlock - 1

            firstBlock[1].setBase(base)
            firstBlock[1].setLimit(limit)
            firstBlock[0].setBase(base)
            firstBlock[0].setLimit(limit)

        for block in self.getOccupedBlocks().getBlocks()[1:len(self.getOccupedBlocks())]:

            movement = block[1].getBase() - limit - 1

            newBase = block[1].getBase() - movement

            newLimit = block[1].getLimit() - movement

            block[1].setBase(newBase)

            block[1].setLimit(newLimit)

            limit = newLimit

            block[0].setBase(newBase)
            block[0].setLimit(newLimit)

        # newBlock = Block(limit, self.getMemory().size())
        # newFreeBlock = FreeBlock().put(newBlock)
        # self.setFreeBlocks(newFreeBlock)


    def load(self, blockList, pid):
        
        pcb = None
        
        memBlock = self.getFreeBlock(blockList.size())
        
        if memBlock != None:
            pcb = self.assignBlock(pid, memBlock, blockList)
        else:
            if self.getFreeSpace() >= blockList.size():
                self.memoryCompact()
                pcb = self.assignBlock(pid, memBlock, blockList)
                
        return pcb
                
    def assignBlock(self, pid, memBlock, blockList):

        memBase = memBlock.getBase()
        blockSize = blockList.size()

        if blockList.size() < memBlock.size():
            newFreeBlock = Block(memBase + blockSize, memBlock.getLimit())
            self.getFreeBlocks().put(newFreeBlock)
        
        self.getFreeBlocks().remove(memBlock)
        
        newOccupedBlock = Block(memBase, memBase + blockSize - 1)
        self.getOccupedBlocks().put(pid, newOccupedBlock)
        
        self.getMemory().assignInMemory(blockList, memBase)
        
        newPCB = PCB(pid, blockSize, memBase, memBase + blockSize - 1)
        
        return newPCB
    
    def fetchInstruction(self, pcb):
        
        instructionIndex = pcb.getBase() + pcb.getPC() 
        
        return self.getMemory().getMemoryFrames()[instructionIndex]



class FirstFit(ContinuosMapping):
    def getFreeBlock(self, size):
        for block in self.getFreeBlocks().getBlocks():
            if block.size() >= size:
                return block

class BestFit(ContinuosMapping):
    def getFreeBlock(self, blockSize):
        biggestBlockSize = self.getSizeOfBiggestBlock()
        block = None

        for b in self.getFreeBlocks().getBlocks():
            if b.size() <= biggestBlockSize and b.size() >= blockSize:
                biggestBlockSize = b.size()
                block = b

        return block

class WorstFit(ContinuosMapping):
    def getFreeBlock(self, blockSize):
        biggestBlockSize = self.getSizeOfBiggestBlock()
        b = None

        for block in self.getFreeBlocks().getBlocks():
            if block.size() == biggestBlockSize and block.size() >= blockSize:
                b = block
                break

        return b