'''
Created on 04/05/2013

@author: Carne
'''
import unittest
from mockito import *
from scheduler.ReadyPriority import ReadyPriority
from pcb.PCB import PCB
from pcb.PCBPriority import PCBPriority

class TestReadyFIFO(unittest.TestCase):
    def testGetPCB(self):
        queue = ReadyPriority(mock(), mock())
        
        pcb1 = mock()
        when(pcb1).getPID().thenReturn(0)
        when(pcb1).getPriority().thenReturn(2)
        
        pcb2 = mock()
        when(pcb2).getPID().thenReturn(1)
        when(pcb2).getPriority().thenReturn(5)
        
        pcb3 = mock()
        when(pcb3).getPID().thenReturn(2)
        when(pcb3).getPriority().thenReturn(1)
        
        queue.put(pcb1)
        queue.put(pcb2)
        queue.put(pcb3)
        self.assertEqual(2, queue.get().getPID())
        self.assertEqual(0, queue.get().getPID())
        self.assertEqual(1, queue.get().getPID())
        
        
if __name__ == '__main__':
    unittest.main()