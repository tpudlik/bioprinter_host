import numpy as np
from config import FEEDRATE, X_STEP, Y_STEP, HEIGHT, WIDTH

# TO DO:
#   *   We assume that the head's nozzles extend along the Y direction.
#       (This is apparently the case.)

def array_to_gcode(array):
    """Convert numpy array into a sequence of gcodes, saved to file."""

    assert isinstance(array, np.ndarray)

    height = array.shape[0]
    #assert height == HEIGHT
    width = array.shape[1]
    #assert width == WIDTH

    strip_number = int(np.ceil(height/12.0))

    gcode = ""
    x_pos = 0
    y_pos = 0
    for strip_idx in xrange(strip_number):
        x_pos = 0
        for column_idx in xrange(width):
            nozzles_gcode = fire_nozzles(array[12*strip_idx:12*(strip_idx+1),
                                               column_idx])
            if nozzles_gcode: # Only print and move if there's any non-white
                              # pixels
                gcode += move(x_pos, y_pos)
                gcode += nozzles_gcode
            x_pos + X_STEP
        y_pos + Y_STEP

    return gcode

def move(x_pos, y_pos):
    """Return the G-CODE describing motion to x_pos, y_pos."""
    out = ""
    out += "G1X"+str(x_pos)+"Y"+str(y_pos)+"F"+str(FEEDRATE)+";\n"
    out += "M400;\n"
    return out

def fire_nozzles(firing_column):
    """Return the G-CODE describing the printing sequence.  If there
    is nothing to be printed, return an empty string.

    """
    out = ''
    if np.all(firing_column == 0):
        return out
    else:
        while np.any(firing_column != 0):
            firing_pattern, firing_column = salvo_integer(firing_column)
            out += "M700 P0 S"+str(firing_pattern)+";\n"
    return out

def salvo_integer(firing_column):
    """Given a column from a numpy array, return the decimal firing pattern
    and a new firing column ()

    The decimal firing pattern is a decimal integer which, written in binary,
    designates the nozzles that ought to be fired.  It is a component of the
    firing G-CODE.

    """
    pattern = ''
    for idx, entry in enumerate(firing_column):
        if entry > 0:
            pattern += '1'
            firing_column[idx] -= 1
        else:
            pattern += '0'

    # Pad with zeroes
    pattern += '0'*(12 - len(pattern))
    return int(pattern, 2), firing_column
