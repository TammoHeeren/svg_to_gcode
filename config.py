''' Configuration file for SVG to GCODE converter
    Date: 26 Oct 2016
    Author: Peter Scriven
    Updated: Nov 2020
    Author: Tammo Heeren
'''

X_OFFSET = 8
Y_OFFSET = 53.5
Z_OFFSET = 36

LASER_ON = 'M106 S255'
LASER_OFF = 'M106 S000'

CUTRATE = 200
MOVERATE = 2000


'''G-code emitted at the start of processing the SVG file'''
PREAMBLE = f'G28\n' \
           f'G1 X{X_OFFSET} Y{Y_OFFSET} Z{Z_OFFSET}\n' \
           f'{LASER_OFF}'

'''G-code emitted at the end of processing the SVG file'''
POSTAMBLE = "G28"

'''G-code emitted before processing a SVG shape'''
shape_preamble = "G4 P0.2"

'''G-code emitted after processing a SVG shape'''
shape_postamble = f'G4 P0.2\n' \
                  f'{LASER_OFF}'

# A4 area:               210mm x 297mm
# Printer Cutting Area: ~178mm x ~344mm
# Testing Area:          150mm x 150mm  (for now)
'''Print bed width in mm'''
bed_max_x = 210

'''Print bed height in mm'''
bed_max_y = 297

''' Used to control the smoothness/sharpness of the curves.
    Smaller the value greater the sharpness. Make sure the
    value is greater than 0.1'''
smoothness = 0.2
