import sys, argparse
from csv_import import csv_import
from array_to_gcode import array_to_gcode
from gcode_to_arduino import gcode_to_arduino

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert csv files into G-CODEs")
    parser.add_argument("input_file", help="The csv file containing the pattern to be printed.")
    parser.add_argument("-t", "--csv_input", action="store_true",
                        help="Sets input to CSV file.")
    parser.add_argument("-c", "--codes_file",
                        help="Write the gcodes out to the file instead of sending them.")
    parser.add_argument("-r", "--response_file",
                        help="Write the Arduino's responses to the file.")
    args = parser.parse_args()

    
    if args.csv_input:
        print "Importing CSV..."
        array = csv_import(args.input_file)
    else:
        pass
        # array = image_import(args.input_file)
        # image_import returns the numpy array, but also writes out a csv 
        # representation of the input image.

    print "Computing G-CODE..."
    gcode = array_to_gcode(array)

    if args.codes_file:
        print "Printing out G-CODE..."
        with open(args.codes_file, 'w') as f:
            f.write(gcode)
    else:
        print "Sending G-CODE..."
        responses = gcode_to_arduino(gcode)
        if args.response_file:
            with open(args.response_file, 'w') as f:
                f.write(responses)
    
    print "Done!"
