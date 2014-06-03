from mecode import G
import numpy as np

# Robomama Outfile
#outfile = r"C:\Users\Lewis Group\Documents\GitHub\Muscular-Thin-Films\MTF_out-new.pgm"
outfile = r"/Users/busbees/Documents/Code/Muscular-Thin-Films\MTF_out-testing.txt"
g = G(
    direct_write=False,
    outfile=outfile,
    header=None,
    footer=None,
    #cal_data=cal_data,
    print_lines=False,
    )

    
def print_well(width, length, number_stacks, stack_height, speed, nozzle = 'A'):
    g.feed(speed)
    for i in range(number_stacks):
        g.rect(x = width,  y=length, direction = 'CW', start = 'LL')
        g.move(**{nozzle:stack_height})  
        
                      
#Insert Function Definitions below here

#g.feed(5)
#g.move(x=4, y=5)    
#g.rect(x=5, y=10, direction = 'CW', start = 'LL')        
            
                    
    
    
#    
    
    
print_well(width=5, length=5, number_stacks=10, stack_height = 0.2, speed=5, nozzle = 'Z')  
        
g.teardown()    