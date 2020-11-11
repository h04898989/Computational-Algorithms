# Behave_Sim.py
#
import optparse
import sys
import yaml

from Components import LPFilter, PulseGen

# plot
def gen_plot(inputSignal,outputSignal):
    import matplotlib.pyplot as plt
    fig,ax=plt.subplots(1,1)
    timeAxis=list(range(len(inputSignal)))
    shftOutput=[sig+2 for sig in outputSignal]
    plt.plot(timeAxis,inputSignal,linestyle='solid')
    plt.plot(timeAxis,shftOutput,linestyle='solid')
    plt.show()


# Main entry point
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
            yml_cfg = yaml.safe_load(open(options.infileName))['Behave_Sim']
        else:
            raise Exception('Error: Input file required!')
        
        #set sim param's
        numTimeSteps=yml_cfg['numTimeSteps']
        loPulsePeriod=yml_cfg['loPulsePeriod']
        hiPulsePeriod=yml_cfg['hiPulsePeriod']
        alpha=yml_cfg['alpha']
        
        outfile=open(yml_cfg['outputFileName'],'w')

        #init PulseGen and LPFilter objects
        pul1=PulseGen(loPulsePeriod, hiPulsePeriod)
        lpf1=LPFilter(alpha)
        
        inputSequence=[]
        outputSequence=[]
        
        #This is the main time iteration loop,
        #  each iteration is one time increment
        for i in range(numTimeSteps):
            pul1.updateOutput()
            
            lpf1.setInput(pul1.getOutput())
            lpf1.updateOutput()
            
            #write input and output signals to output file
            outfile.write('{}\t{}\n'.format(pul1.getOutput(),lpf1.getOutput()))
            
            #let's save the input/output sequences for plotting on-screen later...
            inputSequence.append(pul1.getOutput())
            outputSequence.append(lpf1.getOutput())
            
                   
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
