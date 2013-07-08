'''
Created on 04/05/2013

@author: Carne
'''

import Queue

class Waiting():
    def __init__(self):
        self.queue = Queue.Queue()
        
    def getQueue(self):
        return self.queue
        
    def put(self, pcb):
        self.getQueue().put(pcb)
        
    def get(self):
        return self.getQueue().get()
        
    def isEmpty(self):
        return self.getQueue().qsize() == 0