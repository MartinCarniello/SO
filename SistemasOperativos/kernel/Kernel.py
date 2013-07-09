'''
Created on 11/05/2013

@author: Carne
'''

class Kernel():
    
    def getCpu(self):
        return self.cpu
    
    def getIO(self):
        return self.io
    
    def getEnd(self):
        return self.end
    
    def getScheduler(self):
        return self.scheduler
    
    def setKernelMode(self, value):
        self.kernelMode = value
        
    def getKernelMode(self):
        return self.kernelMode
        
    def isUserMode(self):
        return not self.getKernelMode()
    
    def isKernelMode(self):
        return self.getKernelMode()
    
    def getWaiting(self):
        return self.getIO().getWaiting()
    
    def getClock(self):
        return self.clock
    
    def getLongTerm(self):
        return self.longTerm
    
    def setLongTerm(self, longTerm):
        self.longTerm = longTerm
    
    def __init__(self, scheduler, cpu, io, end, clock, longTerm, shell):
        self.scheduler = scheduler
        scheduler.getExecutionPolitic().setKernel(self)
        self.cpu = cpu
        cpu.setKernel(self)
        self.io = io
        io.setKernel(self)
        self.end = end
        self.kernelMode = False
        self.clock = clock
        self.longTerm = longTerm
        longTerm.setKernel(self)
        self.isRunning = False
        self.shell = shell
        shell.setKernel(self)
        
    def getIsRunning(self):
        return self.isRunning
    
    def setIsRunning(self, value):
        self.isRunning = value
        
    def handle(self, interruption):
        interruption.doIt(self)
        
    def contextSwitch(self):
        self.getScheduler().contextSwitch()
        
    def restartQuantum(self):
        self.getScheduler().restartQuantum()
        
    def restartCPU(self):
        self.getCpu().restart()
        
    def restartIO(self):
        self.getIO().restart()
        
    def sendPCBFromCPUToEnd(self):
        self.getEnd().put(self.getCpu().getPCB())
        
    def sendPCBFromIOToEnd(self):
        self.getEnd().put(self.getIO().getPCB())
        
    def sendPCBToReady(self):
        self.getScheduler().put(self.getIO().getPCB())
        
    def sendPCBToWaiting(self):
        self.getWaiting().put(self.getCpu().getPCB())
        
    def sendPCBToReadyQueue(self, pcb):
        self.getScheduler().put(pcb)
        
    def createNewProcess(self, pid):
        self.getLongTerm().load(pid)
        
    def removeProcessFromMemory(self, pcb):
        self.getLongTerm().removeProcess(pcb)        
        
    def turnToKernelMode(self):
        self.setKernelMode(True)
        
    def turnToUserMode(self):
        self.setKernelMode(False)
        
    def turnOn(self):
        self.contextSwitch()
        self.getClock().startUp()
        self.getIO().startUp()
        self.setIsRunning(True)