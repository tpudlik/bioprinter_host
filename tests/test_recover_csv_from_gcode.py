#!/usr/bin/env python2.7

"""
test_recover_csv_from_gcode.py

PASCALS work. UNFINISHED!
"""

import os, sys
sys.path.append('..')

abspath = os.path.abspath(__file__)
testdir = os.path.dirname(abspath)

import unittest
import numpy as np
from array_to_gcode import *
from gcode_interpreter import gcode_interpreter
from config import FEEDRATE, HEIGHT, WIDTH


### Design:
# 1) call gcode_interpreter.py: read gcode and generate normalized csv.
# 2) read original csv
# 3) normalized original csv

# 4) test the identity of the interpretated csv and normalized original csv.


class test_recover_csv_from_gcode(unittest.TestCase):

    def test_ones(self):
        array = np.ones((15, 4))
        with open(os.path.join(testdir, "ones_15_4.gcode"), 'r') as f:
            gcode = f.read()
        assert gcode == array_to_gcode(array)

