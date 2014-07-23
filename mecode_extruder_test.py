from mecode import G
#from mecode.profilometer_parse import load_and_curate
import numpy as np



calfile =  r"C:\Users\Lewis Group\Desktop\Busbee\profilometer_output_030214_1.txt"

# Robomama Outfile
outfile = r"C:\Users\Lewis Group\Documents\GitHub\Muscular-Thin-Films\MTF_out-new.pgm"

# Travis' Computer Outfile
#outfile = r"C:\Users\tbusbee\Documents\GitHub\Muscular-Thin-Films\MTF_out-testing.txt"
#outfile = r"/Users/busbees/Documents/Code/Muscular-Thin-Films\MTF_out-testing.txt"




cal_data = None#load_and_curate(calfile, reset_start=(2, -2))

g = G(
    #outfile=outfile,
    header=None,
    footer=None,
    #cal_data=cal_data,
    print_lines=True,
    extrude = True,
    )

g.cal_data = None #np.array([[2, -2, 0], [70, -2, -10], [70, -48, -20], [2, -48, -10]])


def calc_extrude_rate(x, y, extrude=True, relative = True, extrusion_width = 0.4, 
                    layer_height = 0.22, multiplier = 1, filament_diameter = 1.75):
    if relative is not True:
        g.absolute()
    
    #area = 3.14159*(layer_height**2)/4 + (layer_height * extrusion_width - layer_height)
    area = layer_height*(extrusion_width-layer_height) + 3.14159*(layer_height/2)**2
    speed = g.speed
    if g.is_relative is not True:
        current_x_pos = g.current_position['x']
        current_y_pos = g.current_position['y']
        print g.current_position['x']
        x_distance = abs(x-current_x_pos)
        y_distance = abs(y-current_y_pos)
        g.abs_move(x=x, y=y)
    else:
        x_distance = x
        y_distance = y
        g.move(x=x, y=y)
           
    line_length = np.sqrt(x_distance**2 + y_distance**2)
    volume = line_length*area
    filament_length = (4*volume)/(3.14149*filament_diameter**2)
    time = line_length/speed
    flow_rate = (area*line_length)/time
    
    print filament_length
    print line_length
    print area
    

#calc_extrude_rate(x = 30, y = 30, extrude=True, relative = False, extrusion_width = 0.4, 
#                    layer_height = 0.22, multiplier = 1, filament_diameter = 1.75)
g.meander(x=10, y=10, spacing = 0.5)
g.move(x=10.3, y=10)
g.teardown()