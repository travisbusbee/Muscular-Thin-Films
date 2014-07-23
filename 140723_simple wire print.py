from mecode import G
import numpy as np

# Cell allignment lines on 22mm slides

g = G(
    direct_write=False,
    #outfile=outfile,
    header=None,
    footer=None,
    #print_lines=False,
    )

#building array
start_x = 0
start_y = 0

array_centerpoints = np.zeros((2,2,2))

increment = 10

for i in range(0,2,1):
    for j in range(0,2,1):
        for k in range(0,2,1):
            if k:
                array_centerpoints[i, j, k] =+ increment*j +start_x
            else:
                array_centerpoints[i, j, k] =+ increment*i +start_y

array_centerpoints = np.reshape(array_centerpoints,(4,2))

#Somehow get surface center points
array_centerpoints_surface = (0.0, 0.0, 0.0, 0.0)


#Settings

pressure_box = 4

area_width = 4

area_length = 4

wire_height=(0.005,0.010,0.025, 0.050)

wire_pressure=(4.8,)*4

wire_speed=(4,)*4

wire_spacing = 1


                                                                                                
def meander_tail(x, y, z, spacing, orientation, tail, speed, clip_direction, nozzle, valve, dwell = 0.5):
    g.feed(30)
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
    


def wire_all (nozzle, valve):
    
    for i in range(0,4):
        g.feed(30)
        g.abs_move(*array_centerpoints[i])
        g.move(x=-2,y=-2)
        g.set_pressure(pressure_box, wire_pressure[i])
        meander_tail (x=area_width, y=-area_length, z=(wire_height[i]+array_centerpoints_surface[i]), spacing=wire_spacing, orientation = 'y', tail = 1, speed=wire_speed[i], clip_direction = '+y', nozzle = nozzle, valve = valve, dwell = 0.75 )


#lets go

wire_all(nozzle= 'A', valve = 0)

