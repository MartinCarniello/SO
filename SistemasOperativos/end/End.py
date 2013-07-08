'''
Created on 27/04/2013

@author: Carne
'''

import Queue

class End():
    def __init__(self):
        self.queue = Queue.Queue()
        
    def getQueue(self):
        return self.queue
        
    def put(self, pcb):
        self.getQueue().put(pcb)
        
    def get(self):
        return self.getQueue().get()
        
    def size(self):
        return self.getQueue().qsize()
    
    def isEmpty(self):
        return self.getQueue().qsize() == 0