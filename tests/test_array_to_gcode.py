"""
test_array_to_gcode.py
"""

import sys
sys.path.append('..')

import unittest
import numpy as np
from array_to_gcode import *
from config import FEEDRATE

class test_salvo_integer(unittest.TestCase):

    def test_empty(self):
        in_column = np.array([0,]*12).T
        pattern, column = salvo_integer(in_column)
        assert pattern == 0
        assert np.array_equal(in_column, column)

    def test_one_shot(self):
        in_column = np.array([1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1]).T
        pattern, column = salvo_integer(in_column)
        assert pattern == int('101110011101', 2)
        assert np.array_equal(np.array([0,]*12).T, column)

    def test_many_shots(self):
        in_column = np.array([1, 0, 2, 1, 1, 0, 0, 1, 1, 3, 0, 1]).T
        pattern, column = salvo_integer(in_column)
        assert pattern == int('101110011101', 2)
        assert np.array_equal(np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0]).T,
                              column)

    def test_short_column(self):
        in_column = np.array([5, 0, 2, 1]).T
        pattern, column = salvo_integer(in_column)
        assert pattern == int('101100000000', 2)
        assert np.array_equal(np.array([4, 0, 1, 0]).T, column)

class test_fire_nozzles(unittest.TestCase):

    def test_empty(self):
        in_column = np.array([0,]*12).T
        assert '' == fire_nozzles(in_column)

    def test_one_shot(self):
        in_column = np.array([1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1]).T
        gcode = "M700 P0 S" + str(int('101110011101', 2)) + ";\n"
        assert gcode == fire_nozzles(in_column)

    def test_two_shot(self):
        in_column = np.array([1, 0, 2, 1, 1, 0, 0, 1, 1, 2, 0, 1]).T
        gcode  = "M700 P0 S" + str(int('101110011101', 2)) + ";\n"
        gcode += "M700 P0 S" + str(int('001000000100', 2)) + ";\n"
        assert gcode == fire_nozzles(in_column)

    def test_short_column(self):
        in_column = np.array([5, 0, 2, 1])
        gcode  = "M700 P0 S" + str(int('101100000000', 2)) + ";\n"
        gcode += "M700 P0 S" + str(int('101000000000', 2)) + ";\n"
        gcode += "M700 P0 S" + str(int('100000000000', 2)) + ";\n"
        gcode += "M700 P0 S" + str(int('100000000000', 2)) + ";\n"
        gcode += "M700 P0 S" + str(int('100000000000', 2)) + ";\n"
        assert gcode == fire_nozzles(in_column)

class test_move(unittest.TestCase):

    def test_no_move(self):
        gcode  = "G1X0Y0F" + str(FEEDRATE) + ';\n'
        gcode += "M400;\n"
        assert gcode == move(0, 0)

    def test_move_X(self):
        gcode  = "G1X1.5Y0F" + str(FEEDRATE) + ';\n'
        gcode += "M400;\n"
        assert gcode == move(1.5, 0)

    def test_move_Y(self):
        gcode  = "G1X0Y4.2F" + str(FEEDRATE) + ';\n'
        gcode += "M400;\n"
        assert gcode == move(0, 4.2)

#class test_array_to_gcode(unittest.TestCase):
#
#    def test_empty(self):
#        array = np.zeros()