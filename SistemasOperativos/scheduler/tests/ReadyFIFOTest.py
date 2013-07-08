'''
Created on 04/05/2013

@author: Carne
'''

import unittest
from mockito import *
from scheduler.ReadyFIFO import ReadyFIFO
from pcb.PCB import PCB

class TestReadyFIFO(unittest.TestCase):
    
    def setUp(self):
        
        self.pcb1 = mock()
        when(self.pcb1).getPID().thenReturn(0)
        when(self.pcb1).getNumberOfInstructions().thenReturn(2)
        
        self.pcb2 = mock()
        when(self.pcb2).getPID().thenReturn(1)
        when(self.pcb2).getNumberOfInstructions().thenReturn(5)
        
        self.pcb3 = mock()
        when(self.pcb3).getPID().thenReturn(2)
        when(self.pcb3).getNumberOfInstructions().thenReturn(1)
        
        self.cpu = mock()
                
        self.queue = ReadyFIFO(self.cpu, mock())
        self.queue.put(self.pcb1)
        self.queue.put(self.pcb2)
        self.queue.put(self.pcb3)
        
        
    def testGetPCB(self):        

        self.assertEqual(0, self.queue.get().getPID())
        self.assertEqual(1, self.queue.get().getPID())
        self.assertEqual(2, self.queue.get().getPID())
        
    def testContextSwitchIsOccuped(self):

        when(self.cpu).isOccuped().thenReturn(True)        
        
        self.queue.contextSwitch()
        
        verify(self.cpu).getPCB()
        verify(self.cpu).restart()
        verify(self.cpu).contextSwitch(self.pcb1)
        
        
    def testContextSwitchIsFree(self):
        
        when(self.cpu).isOccuped().thenReturn(False)
        
        self.queue.contextSwitch()
        
        verify(self.cpu).restart()
        verify(self.cpu).contextSwitch(self.pcb1)
        
        
if __name__ == '__main__':
    unittest.main()