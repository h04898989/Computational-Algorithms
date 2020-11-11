# Behave_Sim.py
#
# Example Main program for PC_Lab_04: Assignment #2
#
import optparse
import sys
import yaml

#import sim Components
from Components import Inverter, Oscillator

#simple function for plotting results on screen
#
def gen_plot(inputSignal,outputSignal):
    import matplotlib.pyplot as plt
    fig,ax=plt.subplots(1,1)
    timeAxis=list(range(len(inputSignal)))
    shftOutput=[sig+2 for sig in outputSignal] #let's offset the output signal for easier viewing
    plt.plot(timeAxis,inputSignal,linestyle='solid')
    plt.plot(timeAxis,shftOutput,linestyle='solid')
    plt.show()


# Main entry point
#
def main(argv=None):
    if argv is None:
        argv = sys.argv
        
    try:
        # get command-line options
        #
        print(argv)
        parser = optparse.OptionParser()
        parser.add_option("-i", "--infile", action="store", dest="infileName", help="Input filename", default=None)
        parser.add_option("-v", "--verbose", action="store_true", dest="verboseMode", help="verbose mode", default=False)
        (options, args) = parser.parse_args(argv)
        #load config data from yaml file
        yml_cfg={}
        if options.infileName != None:
            yml_cfg=yaml.safe_load(open(options.infileName))['Behave_Sim']
        else:
            raise Exception('Error: Input file required!')
        
        #set sim param's
        numTimeSteps=yml_cfg['numTimeSteps']
        clkHalfPeriod=yml_cfg['clkHalfPeriod']
        outfile=open(yml_cfg['outputFileName'],'w')

        #init oscillator and inverter objects
        osc1=Oscillator(clkHalfPeriod)
        inv1=Inverter()
        inv2=Inverter()
        inv3=Inverter()
        
        inputSequence=[]
        outputSequence=[]
        
        #This is the main time iteration loop,
        #  each iteration is one time increment
        for i in range(numTimeSteps):
            osc1.updateOutput()
            
            inv1.setInput(osc1.getOutput())
            inv1.updateOutput()
            
            inv2.setInput(inv1.getOutput())
            inv2.updateOutput()
            
            inv3.setInput(inv2.getOutput())
            inv3.updateOutput()
            
            #write input and output signals to output file
            outfile.write('{}\t{}\n'.format(osc1.getOutput(),inv3.getOutput()))
            
            #let's save the input/output sequences for plotting on-screen later...
            inputSequence.append(osc1.getOutput())
            outputSequence.append(inv3.getOutput())
            
                   
        #close the output file                 
        outfile.close()
        
        #plot results to screen
        gen_plot(inputSequence,outputSequence)
        
        if options.verboseMode:                    
            print('Main Completed!')
    
    except Exception as info:
        if 'options' in vars() and options.verboseMode:
            raise   #re-raise Exception, interpreter shows stack trace
        else:
            print(info)
    
if __name__ == '__main__':
    main()


#python Behave_Sim.py -i behave_cfg.yml --verbose
