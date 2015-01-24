"""
config.py
"""

HEIGHT = 5 # rows
WIDTH = 3 # columns

# Maximum number of times you can print to a single spot
MAX_INTENSITY = 10

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


