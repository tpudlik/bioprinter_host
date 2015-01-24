import sys
from csv_import import csv_import
from array_to_gcode import array_to_gcode
# from gcode_to_arduino import gcode_to_arduino

if __name__ == '__main__':
    filename_in = sys.argv[1]
    filename_out = sys.argv[2]

    print "Importing CSV..."
    array = csv_import(filename_in)

    print "Computing G-CODE..."
    gcode = array_to_gcode(array)

    with open(filename_out, 'w') as f:
        f.write(gcode)

    print "Done!"
