'''
Created on 04/05/2013

@author: Carne
'''

from scheduler.Scheduler import Scheduler
import Queue

class ReadyPriority(Scheduler):
    def __init__(self, cpu, politica):
        Scheduler.__init__(self, cpu, politica)
        self.queue = Queue.PriorityQueue()

    def setQueue(self, q):
        self.queue = q

    def getQueue(self):
        return self.queue

    def put(self, pcb):
        self.getQueue().put((pcb.getPriority(), pcb))

    def get(self):
        return self.getQueue().get()[1]