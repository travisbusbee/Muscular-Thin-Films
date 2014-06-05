from mecode import G
import numpy as np

# Robomama Outfile
#outfile = r"C:\Users\Lewis Group\Documents\GitHub\Muscular-Thin-Films\MTF_out-new.pgm"
outfile = r"C:\Users\Wyss User\Desktop\Busbee\silver_lines.pgm"
g = G(
    direct_write=False,
    outfile=outfile,
    header=None,
    footer=None,
    #cal_data=cal_data,
    print_lines=False,
    )
    
pressure_box=3
fast=5
height=0.2
zero_height=3.11325
def lines(speed, num_lines, pressure, height_above_zero=height):
    g.feed(speed)
    g.set_pressure(pressure_box, pressure)
    for i in range(num_lines):

        g.abs_move(Z=(zero_height+height))
        g.toggle_pressure(pressure_box)
        g.dwell(0.25)
        g.move(x=50, y=0)
        g.toggle_pressure(pressure_box)
        g.move(Z=2)
        g.feed(15)
        g.move(x=-50, y=2)
        g.feed(speed)
            
def print_well(width, length, number_stacks, stack_height, speed, nozzle = 'A'):
    g.feed(speed)
    for i in range(number_stacks):
        g.rect(x = width,  y=length, direction = 'CW', start = 'LL')
        g.move(**{nozzle:stack_height})  
                  
#Insert Funcion Dfinitions below here

#g.feed(5)
#g.move(x=4, y=5)    
#g.rect(x=5, y=10, direction = 'CW', start = 'LL')        
g.write('ENABLE X Y U Z')         
lines(speed=5, pressure= 49,num_lines=10) 

    
#    
    
    
#print_well(width=5, length=5, number_stacks=10, stack_height = 0.2, speed=5, nozzle = 'Z')  
        
g.teardown()    