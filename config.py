"""
config.py: Program configuration.
"""

# ========================================================================== #
# PRINTER SETTINGS
# ========================================================================== #

# Height of the image (number of rows), in pixels
HEIGHT = 100

# Width of the image (number of columns), in pixels
WIDTH = 100

# Maximum number of times you can print to a single spot
MAX_INTENSITY = 5

# Number of nozzles
NOZZLES = 12

# Width of the nozzle set (mm) -- look this up in InkShield docs
NOZZLE_SPREAD = 3.175

# Speed at which the printer head is to move (F argument in G01 Gcode)
FEEDRATE = 1000

# Size of a pixel along the x direction
X_STEP = 0.300

# Size of 12 pixels along the y direction (width of the write head)
Y_STEP = 3.175


# ========================================================================== #
# SERIAL PORT SETTINGS
# ========================================================================== #

# Baud rate for the serial port (must match Arduino code)
SERIAL_BAUD = 19200

# USB port to which the Arduino is connected (str)
SERIAL_PORT = '/dev/ttyUSB0'

# Serial read timeout (float)
SERIAL_TIMEOUT = 0.01


# ========================================================================== #
# ADDITIONAL OUTPUT SETTINGS
# ========================================================================== #

# Do you wish to save a heatmap comparing the input PNG to the PNG that will
# actually be printed?  (The difference is the normalization to MAX_INTENSITY.)
# Used by `image_to_csv.py`.
HEATMAP_OUTPUT = True

# Do you wish to save a CSV representation of the PNG that will be printed?
# Used by `image_to_csv.py`.
CSV_OUTPUT = True