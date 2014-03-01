from mecode import MeCode
from mecode.profilometer_parse import load_and_curate
import numpy as np

xdiff=(-0.75440, -0.2, 0.0145, -0.4)
ydiff=(-0.59385, -0.2,-1.81930, -0.4)
allignment_x=(483, 379, 275, 171)
allignment_y=(217, 217, 217, 217)
zero=(93.5373, 93.9792, 60, 93.852950)

wire_width = 1.75
cantilever_width = 3.5
inset=(cantilever_width-wire_width)/2
pressure_box = 9
extra = 1.5

cantilever_position = ((11.93, -16.1), (17.68, -16.1), (25.43, -16.1), (31.18, -16.1), (38.93, -16.1), (44.68, -16.1), (52.43, -16.1), (58.18, -16.1),
                       (11.93, -34.45), (17.68, -34.45), (25.43, -34.45), (31.18, -34.45), (38.93, -34.45), (44.68, -34.45), (52.43, -34.45), (58.18, -34.45))
pin_position = ((6.6, -3), (12.6, -3), (12.6, -3), (18.6, -3), (24.6, -3), (30.6, -3), (30.6, -3), (36.6, -3),
                (42.6, -3), (48.6, -3), (48.6, -3), (54.6, -3), (60.6, -3), (66.6, -3), (66.6, -3), (72.6, -3),
                (3, -47.56), (9, -47.56), (9, -47.56), (15, -47.56), (21, -47.56), (27, -47.56), (27, -47.56),
                (33, -47.56), (39, -47.56), (45, -47.56), (45, -47.56), (51, -47.56), (57, -47.56), (63, -47.56), (63, -47.56), (69, -47.56))

base_height=(0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
             0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01)
base_pressure=(8,)*16#(21, 21, 21, 21, 21, 21, 21, 21,
               #21, 21, 21, 21, 21, 21, 21, 21)
base_speed=(5, 5, 5, 5, 5, 5, 5, 5,
            5, 5, 5, 5, 5, 5, 5, 5)
base_over = 0.4

wire_height=(0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04,
             0.03, 0.03, 0.03, 0.03, 0.02, 0.02, 0.02, 0.02)
wire_pressure=(72, 72, 73, 73, 74, 74, 75, 75,
               75, 75, 75, 75, 75, 75, 75, 75)
wire_speed=(2, 2, 2, 2, 2, 2, 2, 2,
            2, 2, 2, 2, 2, 2, 2, 2)

basetop_height=(0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
                0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05)
basetop_pressure=(7, 7, 7, 7, 8, 8, 8, 8,
                  9, 9, 9, 9, 8, 8, 8, 8)
basetop_speed=(5, 5, 5, 5, 5, 5, 5, 5,
               5, 5, 5, 5, 5, 5, 5, 5)

top_height=(0.09,)*16#(0.075, 0.075, 0.075, 0.075, 0.075, 0.075, 0.09, 0.09,
            #0.065, 0.065, 0.065, 0.075, 0.075, 0.075, 0.09, 0.09)
top_over=(0.04,)*4+(0.06,)*4+(0.08,)*4+(0.1,)*4#(0.04, 0.04, 0.05, 0.05, 0.055, 0.065, 0.075, 0.085,
          #0.095, 0.1, 0.065, 0.065, 0.065, 0.065, 0.066, 0.065)
top_pressure=(20,)*16#(13, 13, 13, 13, 13, 13, 13, 13,
              #14, 14, 16, 16, 16, 16, 20, 25)
top_speed=(10,)*16#(6, 6, 6, 6, 6, 6, 6, 6,
           #6, 8, 8, 10, 10, 10, 10, 10)

electrode_height=0.05
electrode_pressure = 40

calfile =  r"C:\Users\Lewis Group\Desktop\Busbee\profilometer_output_10.000000.txt"
outfile = r"C:\Users\Lewis Group\Documents\GitHub\Muscular-Thin-Films\MTF_out-testing.pgm"

#cal_data = load_and_curate(calfile, reset_start=(2, -2))

g = MeCode(
    outfile=outfile,
    header=None,
    footer=None,
    #cal_data=cal_data,
    print_lines=False,
    )

g.cal_data = None #np.array([[2, -2, 0], [70, -2, -10], [70, -48, -20], [2, -48, -10]])




def meander_2tails(x, y, z, spacing, orientation, tail, speed):
    g.feed(15)
    g.move(x=-tail)
    g.abs_move(A=z)
    g.feed(speed)
    g.write('$DO0.0=1')
    g.dwell(0.25)
    g.move(x=tail)
    g.meander(x, y, spacing=0.4375, orientation='y')
    g.move(x=tail)
    g.write('$DO0.0=0')
    g.move(A=3)
    
def meander_tops(x, y, spacing, z, speed, orientation = 'y'):   
    g.feed(15)
    g.abs_move(C=z)
    g.feed(speed)
    g.write('$DO2.0=1')
    g.dwell(0.25)
    g.meander(x, y, spacing, orientation = 'y')
    g.write('$DO2.0=0')
    g.move(C=3) 

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
                           
def print_wires(z, speed, extra, tail, width, length, k):
    #inset= (3.5-width)/2
    inset = 0.875
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
        g.write('G1 X($Bx-$Ax-($Bx_dif-$Ax_dif))  Y($Ay-$By+($Ay_dif-$By_dif))')
    elif nozzles=='ac':
        g.abs_move(A=50)
        g.write('G1 X($Cx-$Ax-($Cx_dif-$Ax_dif))  Y($Ay-$Cy+($Ay_dif-$Cy_dif))')    
    elif nozzles=='ad':
        g.abs_move(A=50)
        g.write('G1 X($Dx-$Ax-($Dx_dif-$Ax_dif))  Y($Ay-$Dy+($Ay_dif-$Dy_dif))')
    elif nozzles=='ba':
        g.abs_move(B=50)
        g.write('G1 X($Ax-$Bx-($Ax_dif-$Bx_dif))  Y($By-$Ay+($By_dif-$Ay_dif))')  
    elif nozzles=='bc':
        g.abs_move(B=50)
        g.write('G1 X($Cx-$Bx-($Cx_dif-$Bx_dif))  Y($By-$Cy+($By_dif-$Cy_dif))')
    elif nozzles=='bd':
        g.abs_move(B=50)
        g.write('G1 X($Dx-$Bx-($Dx_dif-$Bx_dif))  Y($By-$Dy+($By_dif-$Dy_dif))')
    elif nozzles=='ca':
        g.abs_move(C=50)
        g.write('G1 X($Ax-$Cx-($Ax_dif-$Cx_dif))  Y($Cy-$Ay+($Cy_dif-$Ay_dif))')
    elif nozzles=='cb':
        g.abs_move(C=50)
        g.write('G1 X($Bx-$Cx-($Bx_dif-$Cx_dif))  Y($Cy-$By+($Cy_dif-$By_dif))')
    elif nozzles=='cd':
        g.abs_move(C=50)
        g.write('G1 X($Dx-$Cx-($Dx_dif-$Cx_dif))  Y($Cy-$Dy+($Cy_dif-$Dy_dif))')
    elif nozzles=='da':
        g.abs_move(D=50)
        g.write('G1 X($Ax-$Dx-($Ax_dif-$Dx_dif))  Y($Dy-$Ay+($Dy_dif-$Ay_dif))')
    elif nozzles=='db':
        g.abs_move(D=50)
        g.write('G1 X($Bx-$Dx-($Bx_dif-$Dx_dif))  Y($Dy-$By+($Dy_dif-$By_dif))')
    elif nozzles=='dc':
        g.abs_move(D=50)
        g.write('G1 X($Cx-$Dx-($Cx_dif-$Dx_dif))  Y($Dy-$Cy+($Dy_dif-$Cy_dif))')
    else:
        g.write('; ---------- input a real nozzle change input...ya idiot--------')   
    if cal_off == False:
        g.cal_data=load_and_curate(calfile, reset_start=(2, -2))       
        g.cal_axis = nozzles[1].upper()         
                                
def print_bottom_layer():
    for i in range(8):
        
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.set_pressure(pressure_box, base_pressure[i])
        meander_2tails(x=3.5, y=-6, z=base_height[i], spacing=base_over, orientation = 'y', tail = 1, speed=base_speed[i] )
    
    for i in range(8,16):
        
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.set_pressure(pressure_box, base_pressure[i])
        meander_2tails(x=3.5, y=6, z=base_height[i], spacing=base_over, orientation = 'y', tail = 1, speed=base_speed[i] )

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
        
def print_all_wires():
    for i in range(0,8,2):
        g.feed(15)
        j=i/2
        g.abs_move(*cantilever_position[i])
        g.set_pressure(pressure_box, wire_pressure[j])
        print_wires(z=wire_height[j], speed=wire_speed[j], extra = 1.5, tail = 1.5, width = 1.75, length=5.125, k=j)
        g.feed(30)
        g.move(B=50)
        g.dwell(1)   
    
    for i in range(8,16,2):
        g.feed(15)
        j=i/2
        g.abs_move(*cantilever_position[i])
        g.set_pressure(pressure_box, wire_pressure[j])
        print_wires(z=wire_height[j], speed=wire_speed[j], extra = -1.5, tail = 1.5, width = 1.75, length=-5.125, k=j)
        g.feed(30)
        g.move(B=50)
        g.dwell(1)

def print_all_wire_insulation(extra, inset, tail, width, length):
    for i in range(0,8,2):
        g.feed(15)
        j=i/2
        g.abs_move(*cantilever_position[i])
        g.set_pressure(pressure_box, base_pressure[j])
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
                        
def print_insulating_tops():
    for i in range(8):
        
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.set_pressure(pressure_box, basetop_pressure[i])
        meander_2tails(x=3.5, y=-6, z=basetop_height[i], spacing=base_over, orientation = 'y', tail = 1, speed=basetop_speed[i] )
    
    for i in range(8,16):
        
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.set_pressure(pressure_box, basetop_pressure[i])
        meander_2tails(x=3.5, y=6, z=basetop_height[i], spacing=base_over, orientation = 'y', tail = 1, speed=basetop_speed[i] )
        
def print_all_alligned_tops():
    for i in range(8):
        
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.set_pressure(pressure_box, top_pressure[i])
        meander_tops(x=3.5, y=-6, spacing=top_over[i], z=top_height[i], speed=top_speed[i], orientation = 'y')
    
    for i in range(8,16):
        
        g.feed(15)
        g.abs_move(*cantilever_position[i])
        g.set_pressure(pressure_box, top_pressure[i])
        meander_tops(x=3.5, y=6, spacing=top_over[i], z=top_height[i], speed=top_speed[i], orientation = 'y')
        
def print_electrodes():
    for i in range(32):
        j=(i/2)
        if i%2==0:
            g.feed(15)
            g.abs_move(*pin_position[i]) 
            g.set_pressure(pressure_box, electrode_pressure)
            g.abs_move(D=electrode_height)
            g.write('$DO0.3=1')
            g.dwell(0.25)
            g.feed(5)
            if  i>15:
                g.abs_move(x=(cantilever_position[j][0] + inset), y=(cantilever_position[j][1]-extra))
            else:
                g.abs_move(x=(cantilever_position[j][0] + inset), y=(cantilever_position[j][1]+extra))
            g.move(x=-0.5)
            g.abs_move(*pin_position[i]) 
            g.write('$DO0.3=0')
            g.move(D=3)
        else:
            g.feed(15)
            g.abs_move(*pin_position[i]) 
            g.set_pressure(pressure_box, electrode_pressure)
            g.abs_move(D=electrode_height)
            g.write('$DO0.3=1')
            g.dwell(0.25)
            g.feed(5)
            if  i>15:
                g.abs_move(x=(cantilever_position[j][0] + inset + wire_width), y=(cantilever_position[j][1]-extra))
            else:
                g.abs_move(x=(cantilever_position[j][0] + inset + wire_width), y=(cantilever_position[j][1]+extra))
            g.move(x=-0.5)
            g.abs_move(*pin_position[i]) 
            g.write('$DO0.3=0')
            g.move(D=3)
            
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
###################################################################
# Generates Code for first layer of cantilevers
#########################################################

g.setup()
g.align_zero_nozzle(nozzle='A', floor=-49.25, deltafast=0.85, deltaslow=0.1, start=-15)
g.align_zero_nozzle(nozzle='B', floor=-49.25, deltafast=0.85, deltaslow=0.1, start=-15)
g.feed(30)
g.abs_move(x=340.65, y=73.88)#197.96
g.write('$DO6.0=1')
g.dwell(1.5)
g.write('$DO6.0=0')
g.toggle_pressure(pressure_box)

#calculate_relative_z(reference_nozzle = 'A')

g.abs_move(A=-5, B=-5, C=-5, D=-5)
g.set_home(A=(zero[0]-5), B=(zero[1]-5), C=(zero[2]-5), D=(zero[3]-5))
#set_home_in_aerotech()

g.feed(25)
g.abs_move(x=349.65, y=73.88)
g.set_home(x=0, y=0)
### Start first layer ###

print_bottom_layer()

print_spacer_layer(x=3.5, y = 6, nozzle = 0.45)

nozzle_change_vars('ab')
g.set_home(x=0, y=0)

print_all_wires()

nozzle_change_vars('ba')
g.set_home(x=0, y=0)

print_all_wire_insulation(extra= -0.21875, inset= 0.65625, tail = 1.5, width = 2.1875, length = 5.34375)

print_all_wire_insulation(extra= 0.21875, inset= 1.0925, tail = 1.5, width = 1.3125, length = 4.9075)







#nozzle_change_vars('ad')
#g.set_home(x=0, y=0)



#nozzle_change_vars('db')
#g.set_home(x=0, y=0)
#g.cal_axis = 'B'



# Code for top wires wires




#nozzle_change_vars('ba')
#g.set_home(x=0, y=0)
#g.cal_axis = 'A'




# code for base tops
#print_insulating_tops()



# move C back where A was and Posoffset.
#nozzle_change_vars('ac')
#g.set_home(x=0, y=0)


#print_all_alligned_tops()


#nozzle_change_vars('cd')
#set_home(x=0, y=0)

#code for electrodes

#print_electrodes()


g.toggle_pressure(pressure_box)  
#g.cal_axis = 'B'
#g.cal_data=load_and_curate(calfile, reset_zero=True)   
g.teardown()