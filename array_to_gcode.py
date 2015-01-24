import numpy as np
from config import FEEDRATE, X_STEP, Y_STEP

def array_to_gcode(array):
    """Convert numpy array into a sequence of gcodes, saved to file."""

    assert isinstance(array, np.ndarray)

    height = array.shape[0]
    width = array.shape[1]

    strip_number = int(np.ceil(height/12))

    gcode = ""
    x_pos = 0
    y_pos = 0
    for strip_idx in xrange(strip_number):
        for column_idx in xrange(width):
            nozzles_gcode = fire_nozzles(array[12*strip_idx:12*(strip_idx+1), column_idx])
            if nozzles_gcode: # Only print if there's any non-white pixels
                gcode += move(x_pos, y_pos)
                gcode += nozzles_gcode
                
            x_pos + X_STEP
        y_pos + Y_STEP

    return gcode

def move(x_pos, y_pos):
    """Return the G-CODE describing motion to x_pos, y_pos."""
    out = ""
    out += "G1X"+str(move_x)+"Y"+str(move_z)+"F"+str(FEEDRATE)+"\n"
    out += "M400\n"
    return out

def fire_nozzles(firing_column):
    """REturn the G-CODE describing the printing sequence.  If there
    is nothing to be printed, return an empty string.

    """
    if np.all(firing_column == 0):
        return ''
    else:

        out += "M700 P0"+" S"+str(firingVal)+"\n"