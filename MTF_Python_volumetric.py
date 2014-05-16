from mecode.devices.keyence_profilometer import KeyenceProfilometer
from mecode.devices.keyence_micrometer import KeyenceMicrometer
from mecode.devices.efd_pressure_box import EFDPressureBox
from mecode import G

g = G(
    outfile=outfile,
    header=None,
    footer=None,
    #cal_data=cal_data,
    print_lines=False,
    )
    
xdiff=(-0.75440, -0.2, 0.0145, -0.4)
ydiff=(-0.59385, -0.2,-1.81930, -0.4)
allignment_x=(483, 379, 275, 171)
allignment_y=(217, 217, 217, 217)
zero=(93.7464, 93.920530, 60, 77.290805)

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
    
    