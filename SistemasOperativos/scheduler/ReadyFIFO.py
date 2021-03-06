'''
Created on 04/05/2013

@author: Carne
'''

from scheduler.Scheduler import Scheduler
import Queue

class ReadyFIFO(Scheduler):

    """Getters y Setters"""    
    def setQueue(self, q):
        self.queue = q

    def getQueue(self):
        return self.queue

    
    """Constructor"""
    def __init__(self, cpu, politica):
        Scheduler.__init__(self, cpu, politica)
        self.queue = Queue.Queue()

    
    def put(self, pcb):
        self.getQueue().put(pcb)

    def get(self):
        return self.getQueue().get()