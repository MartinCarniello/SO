'''
Created on 04/05/2013

@author: Carne
'''

import threading
import time

class Clock(threading.Thread):

    def getRunning(self):
        return self.running

    def setRunning(self, value):
        self.running = value
        
    def getObservers(self):
        return self.observers
    
    def addObserver(self, observer):
        self.getObservers().append(observer)

    def __init__(self):
        threading.Thread.__init__(self)
        self.setRunning(True)
        self.observers = []
        
    def run(self):
        while(self.getRunning()):
            for observer in self.getObservers():
                observer.executionCycle()
                time.sleep(1)
        
    def startUp(self):
        self.start()