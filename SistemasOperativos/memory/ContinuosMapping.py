'''
Created on 10/06/2013

@author: usuario
'''

from memory.MemoryAllocation import MMU
from memory.MemoryBlock import FreeBlock
from memory.MemoryBlock import OccupedBlock
from memory.MemoryBlock import Block
from pcb.PCB import PCB
from pcb.PCBPriority import PCBPriority

class ContinuosMapping(MMU):
    def __init__(self, freeBlocks, occupedBlocks, memory):
        MMU.__init__(self, memory)
        self.freeBlocks = freeBlocks
        self.occupedBlocks = occupedBlocks
        
    def setFreeBlocks(self, freeBlocks):
        self.freeBlocks = freeBlocks
        
    def setOccupedBlocks(self, occupedBlocks):
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

        firstOccupedBlock = self.getOccupedBlocks().getBlocks()[0]

        if firstOccupedBlock[1].getBase() != 0:

            sizeOfFirstBlock = firstOccupedBlock[1].size()
            
            oldBase = firstOccupedBlock[1].getBase()

            base = 0
            limit = sizeOfFirstBlock - 1

            firstOccupedBlock[1].setBase(base)
            firstOccupedBlock[1].setLimit(limit)
            firstOccupedBlock[0].setBase(base)
            firstOccupedBlock[0].setLimit(limit)
            
            self.moveBlockInMemory(oldBase, base, limit)

        if self.getOccupedBlocks().size() > 1:
            
            for block in self.getOccupedBlocks().getBlocks()[1:self.getOccupedBlocks().size()]:
    
                oldBase = block[1].getBase()
    
                movement = block[1].getBase() - limit - 1
    
                newBase = block[1].getBase() - movement
    
                newLimit = block[1].getLimit() - movement
    
                block[1].setBase(newBase)
    
                block[1].setLimit(newLimit)
    
                limit = newLimit
    
                block[0].setBase(newBase)
                block[0].setLimit(newLimit)
                
                self.moveBlockInMemory(oldBase, newBase, newLimit)

        newBlock = Block(limit + 1, self.getMemory().getSize() - 1)
        newFreeBlock = FreeBlock()
        newFreeBlock.put(newBlock)
        self.setFreeBlocks(newFreeBlock)


    def moveBlockInMemory(self, oldBase, base, limit):
        b = base
        ob = oldBase
        
        while b <= limit:
            self.getMemory().getMemoryFrames()[b] = self.getMemory().getMemoryFrames()[ob]
            b += 1
            ob += 1
            
        

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
        priority = blockList.getPriority()

        if blockList.size() < memBlock.size():
            newFreeBlock = Block(memBase + blockSize, memBlock.getLimit())
            self.getFreeBlocks().put(newFreeBlock)
        
        self.getFreeBlocks().remove(memBlock)
        
        newOccupedBlock = Block(memBase, memBase + blockSize - 1)
        
        self.getMemory().assignInMemory(blockList, memBase)
        
        newPCB = PCB(pid, blockSize, memBase, memBase + blockSize - 1)
        
        if priority != None:
            newPCB = PCBPriority(newPCB, priority)
        
        self.getOccupedBlocks().put(newPCB, newOccupedBlock)
        
        return newPCB
    
    def fetchInstruction(self, pcb):
        
        instructionIndex = pcb.getBase() + pcb.getPC()
        
        return self.getMemory().getMemoryFrames()[instructionIndex]
    
    def removeProcess(self, pcb):
        
        occupedBlocks = OccupedBlock()
        
        for block in self.getOccupedBlocks().getBlocks():
            if block[1].getBase() != pcb.getBase():
                occupedBlocks.put(block[0], block[1])
                
        self.setOccupedBlocks(occupedBlocks)
                
                

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