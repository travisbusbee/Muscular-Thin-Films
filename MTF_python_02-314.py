from mecode import *
import os
xdiff=(-0.2, -0.2, -0.2, -0.4)
ydiff=(-0.2, -0.2, -0.2, -0.4)
allignment_x=(483, 379, 275, 171)
allignment_y=(217, 217, 217, 217)
zero=(80, 80, 80, 80)

wire_width = 1.75
cantilever_width = 3.5
inset=(cantilever_width-wire_width)/2
pressure_box = 9
extra = 1.5

cantilever_position = ((11.93, -16.1), (17.68, -16.1), (25.43, -16.1), (31.18, -16.1), (38.93, -16.1), (44.68, -16.1), (52.43, -16.1), (58.18, -16.1), (11.93, -34.45), (17.68, -34.45), (25.43, -34.45), (31.18, -34.45), (38.93, -34.45), (44.68, -34.45), (52.43, -34.45), (58.18, -34.45))
pin_position = ((6.6, -3), (12.6, -3), (12.6, -3), (18.6, -3), (24.6, -3), (30.6, -3), (30.6, -3), (36.6, -3), (42.6, -3), (48.6, -3), (48.6, -3), (54.6, -3), (60.6, -3), (66.6, -3), (66.6, -3), (72.6, -3), (3, -47.56), (9, -47.56), (9, -47.56), (15, -47.56), (21, -47.56), (27, -47.56), (27, -47.56), (33, -47.56), (39, -47.56), (45, -47.56), (45, -47.56), (51, -47.56), (57, -47.56), (63, -47.56), (63, -47.56), (69, -47.56))
#pin_wire = [(cantilever_position[i][0]+inset, cantilever_position[i][1]+extra) for i in range(8)] + [(cantilever_position[i][0]+inset, cantilever_position[i][1]-extra) for i in range(8, 16)]

base_height=(0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01)
base_pressure=(21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21)
base_speed=(5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
base_over = 0.4375

wire_height=(0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02)
wire_pressure=(21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21)
wire_speed=(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)

basetop_height=(0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04)
basetop_pressure=(21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21)
basetop_speed=(5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)

top_height=(0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09)
top_over=(0.035, 0.035, 0.035, 0.035, 0.035, 0.035, 0.035, 0.035, 0.035, 0.035, 0.035, 0.035, 0.035, 0.035, 0.035, 0.035)
top_pressure=(21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21)
top_speed=(5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)

electrode_height=0.05
electrode_pressure = 40


def meander_2tails(x, y, z, spacing, orientation, tail, speed):
    feed(15)
    move(x=-tail)
    feed(speed)
    abs_move(A=z)
    write('DO0.0=1')
    dwell(0.25)
    move(x=tail)
    meander(x, y, spacing=0.4375, orientation='y')
    move(x=tail)
    write('DO0.0=0')
    move(A=3)
    
def meander_tops(x, y, spacing, z, speed, orientation = 'y'):   
    feed(speed)
    abs_move(C=z)
    write
    write('DO0.0=1')
    dwell(0.25)
    meander(x, y, spacing, orientation = 'y')
    write('DO0.0=0')
    move(C=3) 
      
        
def print_wires(z, speed, extra, tail, width, length, k):
    inset= (3.5-width)/2
    feed(15)
    move(x=(-tail+inset), y=extra)
    feed(speed)
    abs_move(B=z)
    write('DO0.0=1')
    dwell(0.25)
    move(x=tail)
    move(y=-(length+extra))
    move(x=width)
    move(y=(length+extra))
    space = cantilever_position[1][0] - cantilever_position[0][0]
    move(x=(space-3.5+(2*inset)))
    move(y=-(length+extra))
    move(x=width)
    move(y=(length+extra))
    move(x=tail)
    move(B=3)
    
def nozzle_change(nozzles = 'ab'):
    feed(40)
    home()
    write(';----------nozzle change------------')
    if nozzles=='ab':
        abs_move(A=-1)
        move(x=(allignment_x[1]-allignment_x[0]-(xdiff[1]-xdiff[0])), y=(allignment_y[0]-allignment_y[1]+(ydiff[0]-ydiff[1])))
    elif nozzles=='ac':
        abs_move(A=-1)
        move(x=(allignment_x[2]-allignment_x[0]-(xdiff[2]-xdiff[0])), y=(allignment_y[0]-allignment_y[2]+(ydiff[0]-ydiff[2])))    
    elif nozzles=='ad':
        abs_move(A=-1)
        move(x=(allignment_x[3]-allignment_x[0]-(xdiff[3]-xdiff[0])), y=(allignment_y[0]-allignment_y[3]+(ydiff[0]-ydiff[3])))
    elif nozzles=='ba':
        abs_move(A=-1)
        move(x=(allignment_x[0]-allignment_x[1]-(xdiff[0]-xdiff[1])), y=(allignment_y[1]-allignment_y[0]+(ydiff[1]-ydiff[0])))
    elif nozzles=='bc':
        abs_move(A=-1)
        move(x=(allignment_x[2]-allignment_x[1]-(xdiff[2]-xdiff[1])), y=(allignment_y[1]-allignment_y[2]+(ydiff[1]-ydiff[2])))
    elif nozzles=='bd':
        abs_move(A=-1)
        move(x=(allignment_x[3]-allignment_x[1]-(xdiff[3]-xdiff[1])), y=(allignment_y[1]-allignment_y[3]+(ydiff[1]-ydiff[3])))
    elif nozzles=='ca':
        abs_move(A=-1)
        move(x=(allignment_x[0]-allignment_x[2]-(xdiff[0]-xdiff[2])), y=(allignment_y[2]-allignment_y[0]+(ydiff[2]-ydiff[0])))
    elif nozzles=='cb':
        abs_move(A=-1)
        move(x=(allignment_x[1]-allignment_x[2]-(xdiff[1]-xdiff[2])), y=(allignment_y[2]-allignment_y[1]+(ydiff[2]-ydiff[1])))
    elif nozzles=='cd':
        abs_move(A=-1)
        move(x=(allignment_x[3]-allignment_x[2]-(xdiff[3]-xdiff[2])), y=(allignment_y[2]-allignment_y[3]+(ydiff[2]-ydiff[3])))
    elif nozzles=='da':
        abs_move(A=-1)
        move(x=(allignment_x[0]-allignment_x[3]-(xdiff[0]-xdiff[3])), y=(allignment_y[3]-allignment_y[0]+(ydiff[3]-ydiff[0])))
    elif nozzles=='db':
        abs_move(A=-1)
        move(x=(allignment_x[1]-allignment_x[3]-(xdiff[1]-xdiff[3])), y=(allignment_y[3]-allignment_y[1]+(ydiff[3]-ydiff[1])))
    elif nozzles=='dc':
        abs_move(A=-1)
        move(x=(allignment_x[2]-allignment_x[3]-(xdiff[2]-xdiff[3])), y=(allignment_y[3]-allignment_y[2]+(ydiff[3]-ydiff[2])))
    else:
        write('; ---------- input a real nozzle change input...ya idiot--------')
###################################################################
# Generates Code for first layer of cantilevers
#########################################################

setup()
home()
abs_move(A=-5, B=-5, C=-5, D=-5)
set_home(A=(zero[0]-5), B=(zero[1]-5), C=(zero[2]-5), D=(zero[3]-5))
for i in range(8):
    
    feed(15)
    abs_move(*cantilever_position[i])
    set_pressure(pressure_box, base_pressure[i])
    meander_2tails(x=3.5, y=-6, z=base_height[i], spacing=base_over, orientation = 'y', tail = 1, speed=base_speed[i] )

for i in range(8,16):
    
    feed(15)
    abs_move(*cantilever_position[i])
    set_pressure(pressure_box, base_pressure[i])
    meander_2tails(x=3.5, y=6, z=base_height[i], spacing=base_over, orientation = 'y', tail = 1, speed=base_speed[i] )



nozzle_change('ab')
# Insert Posoffset code


# Code for top wires wires

for i in range(0,8,2):
    feed(15)
    j=i/2
    abs_move(*cantilever_position[i])
    set_pressure(pressure_box, wire_pressure[j])
    print_wires(z=wire_height[j], speed=wire_speed[j], extra = 1.5, tail = 1.5, width = 1.75, length=5.25, k=j)


for i in range(8,16,2):
    feed(15)
    j=i/2
    abs_move(*cantilever_position[i])
    set_pressure(pressure_box, wire_pressure[j])
    print_wires(z=wire_height[j], speed=wire_speed[j], extra = -1.5, tail = 1.5, width = 1.75, length=-5.25, k=j)


nozzle_change('ba')
#Insert Transition code
# move A back to where B was and Posoffset


# code for base tops

for i in range(8):
    
    feed(15)
    abs_move(*cantilever_position[i])
    set_pressure(pressure_box, basetop_pressure[i])
    meander_2tails(x=3.5, y=-6, z=basetop_height[i], spacing=base_over, orientation = 'y', tail = 1, speed=basetop_speed[i] )

for i in range(8,16):
    
    feed(15)
    abs_move(*cantilever_position[i])
    set_pressure(pressure_box, basetop_pressure[i])
    meander_2tails(x=3.5, y=6, z=basetop_height[i], spacing=base_over, orientation = 'y', tail = 1, speed=basetop_speed[i] )


#Insert Transition code
# move C back where A was and Posoffset.
nozzle_change('ac')


# code for alliged tops

for i in range(8):
    
    feed(15)
    abs_move(*cantilever_position[i])
    set_pressure(pressure_box, top_pressure[i])
    meander_tops(x=3.5, y=-6, spacing=top_over[i], z=top_height[i], speed=basetop_speed[i], orientation = 'y')

for i in range(8,16):
    
    feed(15)
    abs_move(*cantilever_position[i])
    set_pressure(pressure_box, top_pressure[i])
    meander_tops(x=3.5, y=6, spacing=top_over[i], z=top_height[i], speed=basetop_speed[i], orientation = 'y')



#Insert Transition code
# move D to where C was and Posoffset.
nozzle_change('cd')

#code for electrodes


for i in range(32):
    j=(i/2)
    if i%2==0:
       feed(15)
       abs_move(*pin_position[i]) 
       set_pressure(pressure_box, electrode_pressure)
       abs_move(D=electrode_height)
       write('DO0.3=1')
       dwell(0.25)
       feed(5)
       if  i>15:
           abs_move(x=(cantilever_position[j][0] + inset), y=(cantilever_position[j][1]-extra))
       else:
           abs_move(x=(cantilever_position[j][0] + inset), y=(cantilever_position[j][1]+extra))
       move(x=-0.5)
       abs_move(*pin_position[i]) 
       write('DO0.3=0')
       move(D=3)
    else:
       feed(15)
       abs_move(*pin_position[i]) 
       set_pressure(pressure_box, electrode_pressure)
       abs_move(D=electrode_height)
       write('DO0.3=1')
       dwell(0.25)
       feed(5)
       if  i>15:
           abs_move(x=(cantilever_position[j][0] + inset + wire_width), y=(cantilever_position[j][1]-extra))
       else:
           abs_move(x=(cantilever_position[j][0] + inset + wire_width), y=(cantilever_position[j][1]+extra))
       move(x=-0.5)
       abs_move(*pin_position[i]) 
       write('DO0.3=0')
       move(D=3)
           
       
       
       


