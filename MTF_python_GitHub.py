from mecode import G
#from mecode.profilometer_parse import load_and_curate
import numpy as np

xdiff=(-0.75440, -0.2, 0.0145, -0.4)
ydiff=(-0.59385, -0.2,-1.81930, -0.4)
allignment_x=(483, 379, 275, 171)
allignment_y=(217, 217, 217, 217)
zero=(93.556, 93.920530, 60, 77.290805)

wire_width = 1.75
cantilever_width = 3.42
inset=(cantilever_width-wire_width)/2
pressure_box = 4
extra = 1.5

cantilever_position = ((11.93, -16.1), (17.68, -16.1), (25.43, -16.1), (31.18, -16.1), (38.93, -16.1), (44.68, -16.1), (52.43, -16.1), (58.18, -16.1),
                       (11.93, -34.45), (17.68, -34.45), (25.43, -34.45), (31.18, -34.45), (38.93, -34.45), (44.68, -34.45), (52.43, -34.45), (58.18, -34.45))
pin_position = ((6.6, -3), (12.6, -3), (12.6, -3), (18.6, -3), (24.6, -3), (30.6, -3), (30.6, -3), (36.6, -3),
                (42.6, -3), (48.6, -3), (48.6, -3), (54.6, -3), (60.6, -3), (66.6, -3), (66.6, -3), (72.6, -3),
                (3, -47.56), (9, -47.56), (9, -47.56), (15, -47.56), (21, -47.56), (27, -47.56), (27, -47.56),
                (33, -47.56), (39, -47.56), (45, -47.56), (45, -47.56), (51, -47.56), (57, -47.56), (63, -47.56), (63, -47.56), (69, -47.56))

well_position = ((10.5, -24.755), (24, -24.755),(37.5, -24.755),(51, -24.755), 
                       (10.5, -25.755), (24, -25.755),(37.5, -25.755),(51, -25.755))
             

cover_pressure=(12,)*8#(13,)*8#(21, 21, 21, 21, 21, 21, 21, 21,
               #21, 21, 21, 21, 21, 21, 21, 21)
               


base_height=(0.02,)*16#(0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
             #0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01)
base_pressure=(4.8,)*16#(5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2)*2#(6.2,)*8+(6.1,)*8#
               
base_speed=(4,)*16#(5, 5, 5, 5, 5, 5, 5, 5,
            #5, 5, 5, 5, 5, 5, 5, 5)
base_over = 0.38

wire_height=(0.035,)*4+(0.035,)*4#(0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04,
            # 0.03, 0.03, 0.03, 0.03, 0.02, 0.02, 0.02, 0.02)
wire_pressure=(51,)*8#(7.8,)*8#(68,)*16+(68,)*4+(68,)*4
wire_speed = (0.75,)*16#+(4,)*4+(3.75,)*4+(4,)*4 #(2, 2, 2, 2, 2, 2, 2, 2,
            #2, 2, 2, 2, 2, 2, 2, 2)

basetop_height=(0.034,)*16#(0.05, 0.045, 0.042, 0.04)*2 + (0.045, 0.042, 0.04, 0.038, 0.036, 0.034, 0.032, 0.03)
basetop_pressure=(4.2,)*16#(4.2, 4.3, 4.4, 4.5, 4.0, 4.0, 4.1, 4.1, 4.2, 4.3, 4.4, 4.5, 4.0, 4.0, 4.1, 4.1) #+(6.3,)*8#+(6.3,)*4+(6.4,)*4+(6.5,)*4
                    
basetop_speed=(4,)*16#(5, 5, 5, 5, 5, 5, 5, 5,
               #5, 5, 5, 5, 5, 5, 5, 5)

top_height=(0.046,)*16# + (0.11,)*4+(0.1,)*4+(0.12,)*4 #(0.075, 0.075, 0.075, 0.075, 0.075, 0.075, 0.09, 0.09,
            #0.065, 0.065, 0.065, 0.075, 0.075, 0.075, 0.09, 0.09)
top_over=(0.06,)*2 + (0.07,)*2 + (0.08,)*2+(0.09,)*2+(0.1,)*2 + (0.11,)*2 + (0.12,)*2 + (0.14,)*2#+(0.04,)*2+(0.04,)*2+(0.035,)*2+(0.05,)*2#(0.04, 0.04, 0.05, 0.05, 0.055, 0.065, 0.075, 0.085,
          #0.095, 0.1, 0.065, 0.065, 0.065, 0.065, 0.066, 0.065)
top_pressure=(17,)*16#(19, 18.5, 19, 18.5,)*4#+(16,)*4+(14,)*4+(16,)*4#(13, 13, 13, 13, 13, 13, 13, 13,
              #14, 14, 16, 16, 16, 16, 20, 25)
top_speed=(4,)*16#(6, 6, 6, 6, 6, 6, 6, 6,
           #6, 8, 8, 10, 10, 10, 10, 10)

base_init_pressure = 6
electrode_height=0.09
electrode_pressure = 4

calfile =  r"C:\Users\Lewis Group\Desktop\Busbee\profilometer_output_030214_1.txt"

# Robomama Outfile
outfile = r"C:\Users\Lewis Group\Documents\GitHub\Muscular-Thin-Films\MTF_out-new.pgm"

# Travis' Computer Outfile
#outfile = r"C:\Users\tbusbee\Documents\GitHub\Muscular-Thin-Films\MTF_out-testing.txt"
#outfile = r"/Users/busbees/Documents/Code/Muscular-Thin-Films\MTF_out-testing.txt"

alignment_file_1 = r"C:\Users\Lewis Group\Desktop\Alignment\alignment_values_1.txt"
alignment_file_2 = r"C:\Users\Lewis Group\Desktop\Alignment\alignment_values_2.txt"
alignment_file_3 = r"C:\Users\Lewis Group\Desktop\Alignment\alignment_values_3.txt"
alignment_file_4 = r"C:\Users\Lewis Group\Desktop\Alignment\alignment_values_4.txt"


cal_data = None#load_and_curate(calfile, reset_start=(2, -2))

g = G(
    outfile=outfile,
    header=None,
    footer=None,
    #cal_data=cal_data,
    print_lines=False,
    )

g.cal_data = None #np.array([[2, -2, 0], [70, -2, -10], [70, -48, -20], [2, -48, -10]])


def pressure_purge(delay, valve = None):
    g.toggle_pressure(pressure_box)
    g.write('$DO6.0=1')
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(delay)
    g.write('$DO6.0=0')
    if valve is not None:
        g.set_valve(num = valve, value = 0)
    g.toggle_pressure(pressure_box)
    g.dwell(0.5)

def meander_2tails(x, y, z, spacing, orientation, tail, speed, clip_direction, nozzle, valve, dwell = 0.5):
    g.feed(15)
    g.move(x=-tail)
    g.abs_move(**{nozzle:z})
    g.feed(1)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(x=tail)
    g.feed(speed)
    g.meander(x=x, y=y, spacing=spacing, orientation='y', tail = False)
    g.move(x=tail)
    if valve is not None:
        g.set_valve(num = valve, value = 0)
        
    g.dwell(0.3)
    g.clip(axis=nozzle, direction=clip_direction, height=5)
    #g.move(A=3)

def meander_2tails_nostop(x, y, z, spacing, orientation, tail, speed, clip_direction, nozzle, valve, dwell = 0.5):
    g.feed(15)
    g.abs_move(**{nozzle:z})
    g.feed(1)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    #g.dwell(dwell)
    g.move(x=tail)
    g.feed(speed)
    g.meander(x=x, y=y, spacing=spacing, orientation='y', tail = False)
    g.move(x=tail)
    #if valve is not None:
    #    g.set_valve(num = valve, value = 0)
        
    #g.dwell(0.3)
    #g.clip(axis=nozzle, direction=clip_direction, height=5)
    #g.move(A=3)
    
def meander_2tails_2(x, y, z, spacing, orientation, tail, speed, slow_speed, clip_direction, nozzle, valve, dwell = 0.5):
    g.feed(15)
    g.move(x=-tail)
    g.abs_move(**{nozzle:z})
    g.feed(1)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(x=tail)
    g.feed(slow_speed)
    g.move(y=y)
    g.move(x=spacing)
    g.move(y=-y)
    g.move(x=spacing)
    g.feed(speed)
    g.meander(x=(x-2*spacing), y=y, spacing=spacing, orientation='y', tail = False)
    g.move(x=tail)
    if valve is not None:
        g.set_valve(num = valve, value = 0)
        
    g.dwell(0.3)
    g.clip(axis=nozzle, direction=clip_direction, height=5)
    #g.move(A=3)        
def meander_tops(x, y, spacing, z, speed, nozzle, clip_direction, valve, orientation = 'y'):   
    g.feed(15)
    g.abs_move(D=z)
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.25)
    g.meander(x=x, y=y, spacing=spacing, orientation = 'y', tail = False)
    g.set_valve(num = valve, value = 0)
    g.clip(axis=nozzle, direction=clip_direction, height=5) 

def stacked_rectangle(x, y, layer_height, layers, nozzle = 'A'):
    
    for i in range(layers):
        g.move(x=x)
        g.move(y=-y)
        g.move(x=-x)
        g.move(y=y)
        g.move(**{nozzle:layer_height})
    

def y_staple(x, y, nozzle, z, speed, orientation = 'CW'):
    g.feed(15)
    g.abs_move(A=z)
    g.feed(speed)
    g.set_valve(0,1)

    y_move = y - 0.5*nozzle
    x_move = x - nozzle
    
    if  orientation == 'CW':
        g.move(y=y_move)
        g.move(x=x_move)
        g.move(y=-y_move)
    else:
        g.move(y=y_move)
        g.move(x=-x_move)
        g.move(y=-y_move)
        
    g.set_valve(0,0)   

    
def print_double_well(x, y, z, speed, pressure, filament = 1, valve = 0):
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.move(y=-y)
    g.move(x=-x)
    g.move(y=y+filament)
    g.move(x=2*x+filament)
    g.move(y=-(y+filament))
    g.move(x=-x)
    g.move(y=y) 
    g.set_valve(num = valve, value = 0)
    g.move(x=-filament, A=z) 
    
def print_single_well(x, y, layer_height, layers, speed, pressure, filament = 1, valve = 0, nozzle = 'A'):
    g.feed(speed)
    g.set_pressure(com_port = pressure_box, value = pressure)
    pressure_purge(delay = 1)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.25)
    stacked_rectangle(x=x, y=y, layer_height = layer_height, layers = layers, nozzle = nozzle)
    g.set_valve(num=valve, value = 0)
    

def print_cover(z, height, length, over, speed, pressure, valve = 1):
    g.feed(speed)    
    g.set_pressure(com_port=pressure_box, value=pressure)
    pressure_purge(delay = 1)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.25)
    g.meander(x=length, y=height, spacing = over, orientation = 'x', tail = True)
    g.set_valve(num = valve, value = 0)          

def print_cover2(z, height, length, over, speed, pressure, valve = 1):
    g.feed(speed)    
    g.set_pressure(com_port=pressure_box, value=pressure)
    pressure_purge(delay = 1)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.25)
    g.meander(x=length, y=height, spacing = over, orientation = 'x', tail = True)
    

def print_all_covers(nozzle = 'A', valve = 0):
    for i in range(0,4):
        
        g.feed(15)
        g.abs_move(x=well_position[i][0], y=(well_position[i][1] + 14))
        g.move(x=0.5, y=-0.5)
        g.abs_move(**{nozzle:0.2})
        print_cover(z=0.2, height=-4.9, length = 11.5, over = 0.41, speed = 8, pressure = cover_pressure[i], valve = 0)
        g.clip(axis=nozzle, direction='-y', height=5)
    #    #g.move(A=3)
    
    
    for i in range(4,8):
        
        g.feed(15)
        g.abs_move(x=well_position[i][0], y=(well_position[i][1] -14))
        g.move(x=0.5, y=0.5)
        g.abs_move(**{nozzle:0.2})
        print_cover(z=0.2, height=4.9, length = 11.5, over = 0.41, speed = 8, pressure = cover_pressure[i], valve = 0)
        g.clip(axis=nozzle, direction='+y', height=5)
        #g.move(A=3)                          
                                                                                 
                                                                                 
def print_all_single_wells(layer_height, layer_increments, total_increments, pressure, speed, nozzle, valve):
    
    for i in range(0,4):      
        g.feed(15)
        g.abs_move(*well_position[i])
        g.abs_move(**{nozzle:0.15})
        print_single_well(x = 12.5, y = -14, layer_height = layer_height ,  layers = layer_increments, speed = speed, pressure = pressure, filament = 1, valve = 0, nozzle = nozzle)
        g.clip(axis=nozzle, direction='+y', height=3)
        #g.move(A=3)
    
    for i in range(4,8):      
        g.feed(15)
        g.abs_move(*well_position[i])
        g.abs_move(**{nozzle:0.15})
        print_single_well(x = 12.5, y = 14, layer_height = layer_height ,  layers = layer_increments, speed = speed, pressure = pressure, filament = 1, valve = 0, nozzle = nozzle)
        g.clip(axis=nozzle, direction='-y', height=3)
        #g.move(A=3) 
    count = 0
    repeats = (total_increments)-1     
    
    
    for i in range(repeats-1):
        
        count = count + layer_increments
        for i in range(4):
            g.feed(15)
            g.abs_move(*well_position[i])
            g.abs_move(**{nozzle:0.15+count*layer_height})
            print_single_well(x = 12.5, y = -14, layer_height = layer_height ,  layers = layer_increments, speed = speed, pressure = pressure, filament = 1, valve = 0, nozzle = nozzle)
            g.clip(axis=nozzle, direction='+y', height=3)
            #g.move(A=3)
        for i in range(4,8):      
            g.feed(15)
            g.abs_move(*well_position[i])
            g.abs_move(**{nozzle:0.15+count*layer_height})
            print_single_well(x = 12.5, y = 14, layer_height = layer_height ,  layers = layer_increments, speed = speed, pressure = pressure, filament = 1, valve = 0, nozzle = nozzle)
            g.clip(axis=nozzle, direction='-y', height=3)
            #g.move(A=3) 

         
def print_confinement_wells(length, overhang, height, pressure, speed, nozzle, valve):
    for i in range(1,8,2):
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.move(x=-(overhang))
        g.set_pressure(pressure_box, pressure)
        g.abs_move(**{nozzle:height})
        g.set_valve(num = valve, value = 1)
        g.feed(speed)
        g.dwell(0.25)
        g.move(y=-length)
        g.move(x=(2*overhang + cantilever_width))
        g.move(y=length)
        g.set_valve(num = valve, value = 0)
        g.clip(axis=nozzle, direction='+y', height=3)
           
    
    for i in range(9,16,2):
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.move(x=-(overhang))
        g.set_pressure(pressure_box, pressure)
        g.abs_move(**{nozzle:height})
        g.set_valve(num = valve, value = 1)
        g.feed(speed)
        g.dwell(0.25)
        g.move(y=length)
        g.move(x=(2*overhang + cantilever_width))
        g.move(y=-length)
        g.set_valve(num = valve, value = 0)
        g.clip(axis=nozzle, direction='+y', height=3)    




def print_test_wires(pressure, speed, length, spacing, height, valve, nozzle):
    
    g.set_pressure(pressure_box, pressure)
    for i in range(5):
        g.feed(15)
        g.abs_move(**{nozzle:height})
        g.feed(speed)
        g.set_valve (num = valve, value = 1)
        g.dwell(0.25)
        g.move(x=length)
        g.set_valve (num = valve, value = 0)
        g.feed(15)
        g.move(**{nozzle:3})
        g.move(x=-length, y=spacing)
        
        


def print_wires(z, speed, extra, tail, width, length, valve, nozzle, clip_direction, arc_direction, k):
    inset= (cantilever_width-width)/2
    #inset = 0.875
    g.feed(15)
    g.move(x=(-tail+inset), y=extra)
    g.feed(15)
    g.abs_move(**{nozzle:z})
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.25)
    g.move(x=tail)
    g.move(y=-(length+extra))
    g.arc(x = width, y=0, direction = arc_direction , radius = (width/2))
    #g.move(x=width)
    g.move(y=(length+extra))
    space = cantilever_position[1][0] - cantilever_position[0][0]
    g.move(x=(space-width))
    g.move(y=-(length+extra))
    #g.move(x=width)
    g.arc(x = width, y=0, direction = arc_direction , radius = (width/2))
    g.move(y=(length+extra))
    g.move(x=tail)
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, direction=clip_direction, height=3)
    g.abs_move(**{nozzle:20})

def print_wires_insulation(z, speed, extra, tail, width, length, inset):
    #inset= (3.5-width)/2
    #inset = 0.875
    inset = inset
    g.feed(15)
    g.move(x=(-tail+inset), y=extra)
    g.feed(15)
    g.abs_move(A=z)
    g.feed(speed)
    g.write('$DO0.0=1')
    g.dwell(0.25)
    g.move(x=tail)
    g.move(y=-(length+extra))
    g.move(x=width)
    g.move(y=(length+extra))
    space = cantilever_position[1][0] - cantilever_position[0][0]
    g.move(x=(space-3.5+(2*inset)))
    g.move(y=-(length+extra))
    g.move(x=width)
    g.move(y=(length+extra))
    g.move(x=tail)
    g.write('$DO0.0=0')
    g.move(A=3)    
        
                
def print_wires_in_grooves(z, speed, extra, tail, width, length, k):
    inset= (3.5-width)/2
    g.feed(15)
    g.move(x=(-tail+inset), y=extra)
    g.feed(15)
    g.abs_move(B=z)
    g.feed(speed)
    g.write('$DO1.0=1')
    g.dwell(0.25)
    g.move(x=tail)
    g.move(y=-(length+extra))
    g.move(x=width)
    g.move(y=(length+extra))
    space = cantilever_position[1][0] - cantilever_position[0][0]
    g.move(x=(space-3.5+(2*inset)))
    g.move(y=-(length+extra))
    g.move(x=width)
    g.move(y=(length+extra))
    g.move(x=tail)
    g.write('$DO1.0=0')
    g.move(B=3)   
    
            
def nozzle_change(nozzles = 'ab'):
    g.feed(40)
    g.home()
    g.dwell(0.25)
    g.write(';----------nozzle change------------')
    if nozzles=='ab':
        g.abs_move(A=50)
        g.move(x=(allignment_x[1]-allignment_x[0]-(xdiff[1]-xdiff[0])), y=(allignment_y[0]-allignment_y[1]+(ydiff[0]-ydiff[1])))
    elif nozzles=='ac':
        g.abs_move(A=50)
        g.move(x=(allignment_x[2]-allignment_x[0]-(xdiff[2]-xdiff[0])), y=(allignment_y[0]-allignment_y[2]+(ydiff[0]-ydiff[2])))    
    elif nozzles=='ad':
        g.abs_move(A=50)
        g.move(x=(allignment_x[3]-allignment_x[0]-(xdiff[3]-xdiff[0])), y=(allignment_y[0]-allignment_y[3]+(ydiff[0]-ydiff[3])))
    elif nozzles=='ba':
        g.abs_move(B=50)
        g.move(x=(allignment_x[0]-allignment_x[1]-(xdiff[0]-xdiff[1])), y=(allignment_y[1]-allignment_y[0]+(ydiff[1]-ydiff[0])))
    elif nozzles=='bc':
        g.abs_move(B=50)
        g.move(x=(allignment_x[2]-allignment_x[1]-(xdiff[2]-xdiff[1])), y=(allignment_y[1]-allignment_y[2]+(ydiff[1]-ydiff[2])))
    elif nozzles=='bd':
        g.abs_move(B=50)
        g.move(x=(allignment_x[3]-allignment_x[1]-(xdiff[3]-xdiff[1])), y=(allignment_y[1]-allignment_y[3]+(ydiff[1]-ydiff[3])))
    elif nozzles=='ca':
        g.abs_move(C=50)
        g.move(x=(allignment_x[0]-allignment_x[2]-(xdiff[0]-xdiff[2])), y=(allignment_y[2]-allignment_y[0]+(ydiff[2]-ydiff[0])))
    elif nozzles=='cb':
        g.abs_move(C=50)
        g.move(x=(allignment_x[1]-allignment_x[2]-(xdiff[1]-xdiff[2])), y=(allignment_y[2]-allignment_y[1]+(ydiff[2]-ydiff[1])))
    elif nozzles=='cd':
        g.abs_move(C=50)
        g.move(x=(allignment_x[3]-allignment_x[2]-(xdiff[3]-xdiff[2])), y=(allignment_y[2]-allignment_y[3]+(ydiff[2]-ydiff[3])))
    elif nozzles=='da':
        g.abs_move(D=50)
        g.move(x=(allignment_x[0]-allignment_x[3]-(xdiff[0]-xdiff[3])), y=(allignment_y[3]-allignment_y[0]+(ydiff[3]-ydiff[0])))
    elif nozzles=='db':
        g.abs_move(D=50)
        g.move(x=(allignment_x[1]-allignment_x[3]-(xdiff[1]-xdiff[3])), y=(allignment_y[3]-allignment_y[1]+(ydiff[3]-ydiff[1])))
    elif nozzles=='dc':
        g.abs_move(D=50)
        g.move(x=(allignment_x[2]-allignment_x[3]-(xdiff[2]-xdiff[3])), y=(allignment_y[3]-allignment_y[2]+(ydiff[3]-ydiff[2])))
    else:
        g.write('; ---------- input a real nozzle change input...ya idiot--------')

        
def nozzle_change_vars(nozzles = 'ab'):
    g.feed(40)
    g.home()
    if g.cal_data == None:
        cal_off = True
    else:
        cal_off = False
    g.cal_data=None
    g.dwell(0.25)
    g.write(';----------nozzle change------------')
    if nozzles=='ab':
        g.abs_move(A=50)
        g.write('G1 X($Bx-$Ax-($Bx_dif-$Ax_dif))  Y(-($Ay-$By)+($Ay_dif-$By_dif))')
    elif nozzles=='ac':
        g.abs_move(A=50)
        g.write('G1 X($Cx-$Ax-($Cx_dif-$Ax_dif))  Y(-($Ay-$Cy)+($Ay_dif-$Cy_dif))')    
    elif nozzles=='ad':
        g.abs_move(A=50)
        g.write('G1 X($Dx-$Ax-($Dx_dif-$Ax_dif))  Y(-($Ay-$Dy)+($Ay_dif-$Dy_dif))')
    elif nozzles=='ba':
        g.abs_move(B=50)
        g.write('G1 X($Ax-$Bx-($Ax_dif-$Bx_dif))  Y(-($By-$Ay)+($By_dif-$Ay_dif))')  
    elif nozzles=='bc':
        g.abs_move(B=50)
        g.write('G1 X($Cx-$Bx-($Cx_dif-$Bx_dif))  Y(-($By-$Cy)+($By_dif-$Cy_dif))')
    elif nozzles=='bd':
        g.abs_move(B=50)
        g.write('G1 X($Dx-$Bx-($Dx_dif-$Bx_dif))  Y(-($By-$Dy)+($By_dif-$Dy_dif))')
    elif nozzles=='ca':
        g.abs_move(C=50)
        g.write('G1 X($Ax-$Cx-($Ax_dif-$Cx_dif))  Y(-($Cy-$Ay)+($Cy_dif-$Ay_dif))')
    elif nozzles=='cb':
        g.abs_move(C=50)
        g.write('G1 X($Bx-$Cx-($Bx_dif-$Cx_dif))  Y(-($Cy-$By)+($Cy_dif-$By_dif))')
    elif nozzles=='cd':
        g.abs_move(C=50)
        g.write('G1 X($Dx-$Cx-($Dx_dif-$Cx_dif))  Y(-($Cy-$Dy)+($Cy_dif-$Dy_dif))')
    elif nozzles=='da':
        g.abs_move(D=50)
        g.write('G1 X($Ax-$Dx-($Ax_dif-$Dx_dif))  Y(-($Dy-$Ay)+($Dy_dif-$Ay_dif))')
    elif nozzles=='db':
        g.abs_move(D=50)
        g.write('G1 X($Bx-$Dx-($Bx_dif-$Dx_dif))  Y(-($Dy-$By)+($Dy_dif-$By_dif))')
    elif nozzles=='dc':
        g.abs_move(D=50)
        g.write('G1 X($Cx-$Dx-($Cx_dif-$Dx_dif))  Y(-($Dy-$Cy)+($Dy_dif-$Cy_dif))')
    else:
        g.write('; ---------- input a real nozzle change input...ya idiot--------')   
    if cal_off == False:
        g.cal_data=load_and_curate(calfile, reset_start=(2, -2))       
        g.cal_axis = nozzles[1].upper()         
                                
def print_bottom_layer(nozzle, valve):
    g.set_pressure(pressure_box, base_pressure[0])
    pressure_purge(delay = 1.5, valve = 0)
    for i in range(0,8):
        
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.set_pressure(pressure_box, base_pressure[i])
        meander_2tails_2(x=cantilever_width, y=-5.75, z=base_height[i], spacing=base_over, slow_speed = 1, orientation = 'y', tail = 1, speed=base_speed[i], clip_direction = '+y', nozzle = nozzle, valve = valve, dwell = 3 )
    
    for i in range(8,16):
        
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.set_pressure(pressure_box, base_pressure[i])
        meander_2tails_2(x=cantilever_width, y=5.75, z=base_height[i], spacing=base_over, slow_speed = 1, orientation = 'y', tail = 1, speed=base_speed[i], clip_direction = '-y', nozzle = nozzle, valve = valve, dwell = 3 )

def celltest_bottom_layer(nozzle, valve):
    g.set_pressure(pressure_box, base_pressure[0])
    pressure_purge(delay = 1.5, valve = 0)
    for i in range(1,8,2):
        
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.set_pressure(pressure_box, base_pressure[i])
        meander_2tails_2(x=cantilever_width, y=-5.75, z=base_height[i], spacing=base_over, slow_speed = 1, orientation = 'y', tail = 1, speed=base_speed[i], clip_direction = '+y', nozzle = nozzle, valve = valve, dwell = 3 )
    
    for i in range(9,16,2):
        
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.set_pressure(pressure_box, base_pressure[i])
        meander_2tails_2(x=cantilever_width, y=5.75, z=base_height[i], spacing=base_over, slow_speed = 1, orientation = 'y', tail = 1, speed=base_speed[i], clip_direction = '-y', nozzle = nozzle, valve = valve, dwell = 3 )


def print_bottom_layer_2(nozzle, valve):
    g.set_pressure(pressure_box, base_init_pressure)
    pressure_purge(delay = 1.5, valve = 0)
    g.abs_move(x=well_position[0][0], y=(well_position[0][1] + 14))
    g.abs_move(**{nozzle:base_height[0]})
    g.feed(base_speed[0])
    g.move(x=0.5, y=-0.5)
    g.set_valve(num = valve, value = 1)
    print_cover(z=base_height[0], height=-4.9, length = 11.5, over = 0.41, speed = base_speed[0], pressure = base_init_pressure, valve = 0)
    
    for i in range(0,8):
        
        
        g.set_pressure(pressure_box, base_pressure[i])
        g.abs_move(x=(cantilever_position[i][0]-1), y=cantilever_position[i][1])
        meander_2tails_nostop(x=cantilever_width, y=-5.75, z=base_height[i], spacing=base_over, orientation = 'y', tail = 1, speed=base_speed[i], clip_direction = '+y', nozzle = nozzle, valve = valve, dwell = 1 )
    
    g.set_valve(num = valve, value = 0)
    g.move(**{nozzle:3})
    g.set_pressure(pressure_box, base_init_pressure)
    pressure_purge(delay = 1.5, valve = 0)
    g.feed(15)
    g.abs_move(x=well_position[4][0], y=(well_position[4][1] - 14))
    g.abs_move(**{nozzle:base_height[0]})
    g.feed(base_speed[8])
    g.move(x=0.5, y=-0.5)
    g.set_valve(num = valve, value = 1)
    print_cover(z=base_height[8], height=4.9, length = 11.5, over = 0.41, speed = base_speed[8], pressure = base_init_pressure, valve = 0)
    for i in range(8,16):
        g.set_pressure(pressure_box, base_pressure[i])
        g.abs_move(x=(cantilever_position[i][0]-1), y=cantilever_position[i][1])       
        meander_2tails_nostop(x=cantilever_width, y=5.75, z=base_height[i], spacing=base_over, orientation = 'y', tail = 1, speed=base_speed[i], clip_direction = '-y', nozzle = nozzle, valve = valve, dwell = 1 )
    g.set_valve(num = valve, value = 0)
    g.move(**{nozzle:3})
def print_spacer_layer(x, y, nozzle):
    for i in range(8):
        
        g.feed(15)
        g.abs_move(*cantilever_position[i])    
        g.move(x=nozzle/2)
        g.set_pressure(pressure_box, basetop_pressure[i])
        y_staple(x=x, y=-y, nozzle = nozzle, z = basetop_height[i], speed = basetop_speed[i], orientation = 'CW')
        g.move(A=1)
        x_over= ((x/2)-nozzle)
        y_height = (y-nozzle-0.875)

        g.move(x=-x_over)
        g.move(A=-1)
        y_staple(x=2*nozzle, y=-y_height, nozzle = nozzle, z = basetop_height[i], speed = basetop_speed[i], orientation = 'CCW')
        g.move(A=3)
        
        
        
        
    for i in range(8,16):
        
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.move(x=nozzle/2)
        g.set_pressure(pressure_box, basetop_pressure[i])
        y_staple(x=x, y=y, nozzle = nozzle, z = basetop_height[i], speed = basetop_speed[i], orientation = 'CW')
        g.move(A=1)
        x_over= (((x-nozzle)/2)-0.5*nozzle)
        y_height = (y-nozzle-0.85)
        g.move(x=-x_over)
        g.move(A=-1)
        y_staple(x=2*nozzle, y=y_height, nozzle = nozzle, z = basetop_height[i], speed = basetop_speed[i], orientation = 'CCW')
        g.move(A=3)
        
def print_all_wires(valve, nozzle):
    for i in range(0,8,2):
        g.feed(15)
        j=i/2
        g.abs_move(*cantilever_position[i])
        g.set_pressure(pressure_box, wire_pressure[j])
        print_wires(z=wire_height[j], speed=wire_speed[j], extra = 1.5, tail = 1.5, width = 1.55, length=5.2, valve = valve, nozzle = nozzle, clip_direction = '+y', k=j, arc_direction = 'CCW')
        g.feed(30)
        g.abs_move(**{nozzle:60})
        g.dwell(1)   
    
    for i in range(8,16,2):
        g.feed(15)
        j=i/2
        g.abs_move(*cantilever_position[i])
        g.set_pressure(pressure_box, wire_pressure[j])
        print_wires(z=wire_height[j], speed=wire_speed[j], extra = -1.5, tail = 1.5, width = 1.55, length=-5.2, valve = valve, nozzle = nozzle, clip_direction = '-y', k=j, arc_direction = 'CW')
        g.feed(30)
        g.abs_move(**{nozzle:60})
        g.dwell(1)

def print_all_wire_insulation(extra, inset, tail, width, length):
    for i in range(0,8,2):
        g.feed(15)
        j=i/2
        g.abs_move(*cantilever_position[i])
        g.set_pressure(pressure_box, base_pressure[j])
        pressure_purge(delay = 1)
        print_wires_insulation(z=basetop_height[j], speed=base_speed[j], inset = inset, extra = extra, tail = tail, width = width, length=length)
        g.feed(30)
        g.move(A=50)
        g.dwell(1)   
    
    for i in range(8,16,2):
        g.feed(15)
        j=i/2
        g.abs_move(*cantilever_position[i])
        g.set_pressure(pressure_box, base_pressure[j])
        print_wires_insulation(z=basetop_height[j], speed=base_speed[j], inset = inset, extra = -extra, tail = tail, width = width, length=-length)
        g.feed(30)
        g.move(A=50)
        g.dwell(1)        
                        
def print_insulating_tops(nozzle, valve):
    g.set_pressure(pressure_box, basetop_pressure[1])
    pressure_purge(delay = 1.5)
   
    for i in range(0,8):
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.set_pressure(pressure_box, basetop_pressure[i])
        pressure_purge(delay = 0.5)
        meander_2tails(x=cantilever_width, y=-6.75, z=basetop_height[i], spacing=base_over, orientation = 'y', tail = 1, speed=basetop_speed[i], clip_direction = '+y', nozzle = nozzle, valve = valve, dwell = 0.75 )
        
            
    for i in range(8,16):
        
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.set_pressure(pressure_box, basetop_pressure[i])
        pressure_purge(delay = 0.5)
        meander_2tails(x=cantilever_width, y=6.75, z=basetop_height[i], spacing=base_over, orientation = 'y', tail = 1, speed=basetop_speed[i], clip_direction = '-y', nozzle = nozzle, valve = valve, dwell = 0.75 )
        
def print_all_alligned_tops(nozzle, valve):
    g.set_pressure(pressure_box, top_pressure[1])
    pressure_purge(delay = 1.5)
    for i in range(1,8,2):
        j=i/2
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.move(x=-0.1)
        g.set_pressure(pressure_box, top_pressure[i])
        pressure_purge(delay = 0.5)
        meander_tops(x=(cantilever_width + 0.1), y=-5.75, spacing=top_over[i], z=top_height[i], speed=top_speed[i], orientation = 'y', nozzle = nozzle, clip_direction = '+y', valve = valve)
    
    for i in range(9,16,2):
        j=i/2
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.move(x=-0.1)
        g.set_pressure(pressure_box, top_pressure[i])
        pressure_purge(delay = 0.5)
        meander_tops(x=(cantilever_width + 0.1), y=5.75, spacing=top_over[i], z=top_height[i], speed=top_speed[i], orientation = 'y', nozzle = nozzle, clip_direction = '+y', valve = valve)
        
def print_sacrificial(trace_speed, height, over, nozzle, overhang = 0.85):
    for i in range(1,8,2):
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.move(x=-overhang)
        meander_2tails(x=(cantilever_width + 2*overhang), y=-7.9, spacing=over, z=height, tail = 1, clip_direction = '+y', speed=trace_speed, orientation = 'y', nozzle = nozzle, valve = None)
    
    for i in range(9,16,2):
        
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.move(x=-overhang)
        meander_2tails(x=(cantilever_width + 2*overhang), y=7.9, spacing=over, z=height, tail = 1, clip_direction = '-y', speed=trace_speed, orientation = 'y', nozzle = nozzle, valve = None)

def print_underwires(height, nozzle, length, width):
    inset = (cantilever_width-width)/2
    underspeed = 5
    for i in range(1,8,2):
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.move(x=(inset))
        g.abs_move(**{nozzle:height})
        g.feed(underspeed)
        g.move(y=-(length))
        g.arc(x = width, y=0, direction = 'CCW' , radius = (width/2))
        #g.move(x=width)
        g.move(y=(length))
        g.move(**{nozzle:3})

    for i in range(9,16,2):
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.move(x=(inset))
        g.abs_move(**{nozzle:height})
        g.feed(underspeed)
        g.move(y=(length))
        g.arc(x = width, y=0, direction = 'CW' , radius = (width/2))
        #g.move(x=width)
        g.move(y=(-length))
        g.move(**{nozzle:3})

def print_underwire_double(height, nozzle, length, width, over_space, extra):
    inset = (cantilever_width-width)/2
    underspeed = 5
    g.feed(15)
    g.abs_move(x=5, y=-25)
    g.abs_move(**{nozzle:height})
    g.feed(underspeed)
    g.move(y=-10)
    g.move(**{nozzle:3})
    for i in range(1,8,2):
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.move(x=(inset - 0.5*over_space), y=extra)
        g.abs_move(**{nozzle:height})
        g.feed(underspeed)
        g.move(y=-(length + extra))
        g.arc(x = (width + over_space), y=0, direction = 'CCW' , radius = ((width+over_space)/2))
        g.move(y=(length + extra))
        g.move(x=-over_space)
        g.move(y=-(length+ extra))
        g.arc(x = -(width - over_space), y=0, direction = 'CW' , radius = ((width-over_space)/2))
        g.move(y=(length + extra))
        g.clip(axis=nozzle, direction='+y', height=3)

    for i in range(9,16,2):
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.move(x=(inset - 0.5*over_space), y=-extra)
        g.abs_move(**{nozzle:height})
        g.feed(underspeed)
        g.move(y=(length + extra))
        g.arc(x = (width + over_space), y=0, direction = 'CW' , radius = ((width+over_space)/2))
        g.move(y=-(length + extra))
        g.move(x=-over_space)
        g.move(y=(length+extra))
        g.arc(x = -(width - over_space), y=0, direction = 'CCW' , radius = ((width-over_space)/2))
        g.move(y=-(length+extra))
        g.clip(axis=nozzle, direction='-y', height=3)                              
                                                                                                
def print_electrodes(valve, nozzle):
    for i in range(8,16):
        j=(i/2)
        if i%2==0:
            g.feed(15)
            g.abs_move(*pin_position[i]) 
            g.set_pressure(pressure_box, electrode_pressure)
            g.abs_move(**{nozzle:electrode_height})
            g.set_valve(num = valve, value = 1)
            g.dwell(0.25)
            g.feed(5)
            if  i>15:
                g.abs_move(x=(cantilever_position[j][0] + inset), y=(cantilever_position[j][1]-extra))
            else:
                g.abs_move(x=(cantilever_position[j][0] + inset), y=(cantilever_position[j][1]+extra))
            g.move(x=-0.5)
            g.abs_move(*pin_position[i]) 
            g.set_valve(num = valve, value = 0)
            g.move(**{nozzle:3})
        else:
            g.feed(15)
            g.abs_move(*pin_position[i]) 
            g.set_pressure(pressure_box, electrode_pressure)
            g.abs_move(**{nozzle:electrode_height})
            g.set_valve(num = valve, value = 1)
            g.dwell(0.25)
            g.feed(5)
            if  i>15:
                g.abs_move(x=(cantilever_position[j][0] + inset + wire_width), y=(cantilever_position[j][1]-extra))
            else:
                g.abs_move(x=(cantilever_position[j][0] + inset + wire_width), y=(cantilever_position[j][1]+extra))
            g.move(x=-0.5)
            g.abs_move(*pin_position[i]) 
            g.set_valve(num = valve, value = 0)
            g.move(**{nozzle:3})
            

            
def calculate_relative_z(reference_nozzle = 'A'):
    if reference_nozzle == 'A':
        g.write('$zA = -{}' .format(zero[0]))
        g.write('$zB = $zA + ($zMeasureB - $zMeasureA) + ($Az_dif-$Bz_dif)')
        g.write('$zC = $zA + ($zMeasureC - $zMeasureA) + ($Az_dif-$Cz_dif)')
        g.write('$zD = $zA + ($zMeasureD - $zMeasureA) + ($Az_dif-$Dz_dif)')
    elif reference_nozzle == 'B':
            g.write('$zB = -{}' .format(zero[1]))
            g.write('$zA = $zB + ($zMeasureA - $zMeasureB) + ($Bz_dif-$Az_dif)')
            g.write('$zC = $zB + ($zMeasureC - $zMeasureB) + ($Bz_dif-$Cz_dif)')
            g.write('$zD = $zB + ($zMeasureD - $zMeasureB) + ($Bz_dif-$Dz_dif)')
    elif reference_nozzle == 'C':
            g.write('$zC = -{}' .format(zero[2]))
            g.write('$zA = $zC + ($zMeasureA - $zMeasureC) + ($Cz_dif-$Az_dif)')
            g.write('$zB = $zC + ($zMeasureB - $zMeasureC) + ($Cz_dif-$Bz_dif)')
            g.write('$zD = $zC + ($zMeasureD - $zMeasureC) + ($Cz_dif-$Dz_dif)')
    elif reference_nozzle == 'D':
            g.write('$zD = -{}' .format(zero[3]))
            g.write('$zA = $zD + ($zMeasureA - $zMeasureD) + ($Dz_dif-$Az_dif)')
            g.write('$zB = $zD + ($zMeasureB - $zMeasureD) + ($Dz_dif-$Bz_dif)')
            g.write('$zC = $zD + ($zMeasureC - $zMeasureD) + ($Dz_dif-$Cz_dif)')

def set_home_in_aerotech():
    g.write('G92 A(-$zA-5) B(-$zB-5) C(-$zC - 5) D(-$zD - 5)')   
    
def recall_alignment(nozzle = 'A'):
   if nozzle=='A':
        g.write(open(alignment_file_1).read()) 
   elif nozzle=='B':
        g.write(open(alignment_file_2).read()) 
   elif nozzle=='C':
        g.write(open(alignment_file_3).read())
   elif nozzle=='D':
        g.write(open(alignment_file_4).read())
   elif nozzle =='all':
        g.write(open(alignment_file_1).read())
        g.write(open(alignment_file_2).read())
        g.write(open(alignment_file_3).read())
        g.write(open(alignment_file_4).read())   
        
def pressure_test(nozzle, valve, length, space, z, speed, dwell, start_pressure, pressure_step, repeats):    
    g.feed(15)
    g.abs_move(**{nozzle:z})
    g.set_pressure(pressure_box, start_pressure)
    pressure_purge(delay = 1)
    count = 0
    for i in range(repeats):
        pressure_set = start_pressure + count * pressure_step
        g.set_pressure(pressure_box, pressure_set)
        g.feed(speed)
        g.abs_move(**{nozzle:z})
        g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.move(y=-length)
        g.move(x=space)
        g.move(y=length)
        g.set_valve(num = valve, value = 0)
        g.feed(15)
        g.move(**{nozzle:3})
        g.move(x=2)
        count = count + 1    
                                       

           

###################################################################
# Generates Code for first layer of cantilevers
#########################################################

#g.setup()


#
recall_alignment(nozzle = 'all')
#
#
#g.align_zero_nozzle(nozzle='A', floor=-49.25, deltafast=0.85, deltaslow=0.1, start=-15)
#g.align_zero_nozzle(nozzle='B', floor=-49.25, deltafast=0.85, deltaslow=0.1, start=-15)
#g.align_zero_nozzle(nozzle='C', floor=-49.25, deltafast=0.85, deltaslow=0.1, start=-15)
#g.align_zero_nozzle(nozzle='D', floor=-49.25, deltafast=0.85, deltaslow=0.1, start=-15)
g.save_alignment(nozzle = 'all')
g.toggle_pressure(pressure_box)
#
g.feed(30)
g.abs_move(A=-1, B=-1, C=-1, D=-1)
#g.abs_move(x=(350.469 -0.75), y=129.9315 +11)#197.96
#g.write('G1 X$Ax_dif  Y$Ay_dif')
#g.set_home(x=0, y=0)
#

calculate_relative_z(reference_nozzle = 'A')
#
g.abs_move(A=-5, B=-5, C=-5, D=-5)

set_home_in_aerotech()

g.clip(axis='A', direction= '+x', height=5) 

#
g.abs_move(x=369.1, y=44.5)
g.set_home(x=0, y=0)
g.move(y=1)
#print_test_wires(pressure = 30, speed = 2, length = 30, spacing = 2, height = 0.015, valve = 0, nozzle = 'A')

#pressure_test(nozzle = 'A', valve = 0, length= 10, space = 0.385, z = 0.02, speed = 4, dwell = 0.35, start_pressure = 4.8, pressure_step = 0.2, repeats = 12)

#
##
#nozzle_change_vars('ab')
#g.set_home(x=0, y=0)

#g.abs_move(x=5, y=-20)
#pressure_test(nozzle = 'D', valve = 3, length= 10, space = 0.075, z = 0.023, speed = 4, dwell = 0.35, start_pressure = 16, pressure_step = 0.5, repeats = 16)

#
#print_sacrificial(trace_speed = 5, height = -0.15, over = 0.75, nozzle = 'B', overhang = 0.5)
#
#
#
#nozzle_change_vars('ba')
#g.set_home(x=0, y=0)

#print_underwire_double(height=-0.1, nozzle = 'D', length = 5.2, width = 1.55, over_space = 0.7, extra = 0.5)

#
#print_bottom_layer_2(nozzle = 'A', valve = 0)
#celltest_bottom_layer(nozzle = 'A', valve = 0)

#nozzle_change_vars('ab')
#g.set_home(x=0, y=0)
#
#
#print_all_wires(nozzle = 'B', valve = 1)
####
#nozzle_change_vars('ba')
#g.set_home(x=0, y=0)
#
#print_insulating_tops(nozzle = 'A', valve = 0)
##



#nozzle_change_vars('ab')
#g.set_home(x=0, y=0)
###
#print_all_alligned_tops(nozzle = 'D', valve = 3)
#
#
#
#nozzle_change_vars('da')
#g.set_home(x=0, y=0)

#print_electrodes(valve=1, nozzle='B')
#
#print_all_covers(nozzle = 'B', valve = 0)
#print_confinement_wells(length = 7.8, overhang = 1.5, height=0.2, pressure = 11, speed = 8, nozzle = 'B', valve = 0)
#print_all_single_wells(layer_height = 0.35, layer_increments=5, total_increments=6, pressure=28.5, speed=15, nozzle = 'B', valve = 0)




#print_spacer_layer(x=3.5, y = 6, nozzle = 0.45)
#print_all_wire_insulation(extra= -0.21875, inset= 0.65625, tail = 1.5, width = 2.1875, length = 5.34375 
#g.cal_axis = 'B'
##g.set_home(A=(zero[0]-5), B=(zero[1]-5), C=(zero[2]-5), D=(zero[3]-5))
#g.cal_data=load_and_curate(calfile, reset_zero=True)  

g.write('POSOFFSET CLEAR X Y U A B C D')
g.feed(30)
g.abs_move(A=-5, B=-5, C=-5, D=-5) 
g.move(x=75)
g.toggle_pressure(pressure_box)
g.teardown()