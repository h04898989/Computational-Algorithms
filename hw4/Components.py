# Components module
#

class Component:
    """
    Base class for all component types
    """
    def updateOutput(self):
        raise Exception('Error: Must override updateOutput method in derived classes!')
    
    def getOutput(self):
        return self.outputState


class LPFilter(Component):
    """
    Ideal LPFilter component
    """
    def __init__(self, alpha):
        self.alpha=alpha
        self.temp=0
        self.currentInput=0
        self.outputState=0
     
    def setInput(self, inputState):
        self.temp=self.outputState
        self.currentInput=inputState
        
    def updateOutput(self):
        try:
            self.outputState = self.alpha*self.currentInput+(1-self.alpha)*self.temp
        except Exception as info:
            print(info)
        
    def __str__(self):
        s=''
        s+='Input : ' + str(self.currentInput) + '\n'
        s+='Output: ' + str(self.outputState)
        return s


class PulseGen(Component):
    """
    Ideal Pulse Generator component
    """
    def __init__(self, loPulsePeriod, hiPulsePeriod):
        self.loPulsePeriod=loPulsePeriod
        self.hiPulsePeriod=hiPulsePeriod
        self.counter=-1
        self.outputState=1
     
    def updateOutput(self):
        #increment internal counter
        self.counter+=1
        
        # toggle the signal every clkHalfPeriod time steps
        if self.counter%(self.loPulsePeriod+self.hiPulsePeriod) != 0:
            if self.counter%(self.loPulsePeriod) == 0:
                self.outputState=(self.outputState+1)%2
        else:
            self.outputState=(self.outputState+1)%2
            self.counter=0 #reset counter
                       
    def __str__(self):
        s=''
        s+='clkHalfPeriod: ' + str(self.clkHalfPeriod) + '\n'
        s+='Output: ' + str(self.outputState)
        return s
