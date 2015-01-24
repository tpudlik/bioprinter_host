#!/usr/bin/env python2.7

import numpy as np
import re

from config import *

def read_gcode(filename):
	""" function to read gcode as raw text """
	##TODO: parse/read file line by line for memory considerations
	with open(filename, 'r') as fh_in:
		gcode_raw = fh_in.readlines()
		gcode_raw = [gcode.rstrip(';\n') for gcode in gcode_raw] # stripping off trailing semicolon and newlines
	return gcode_raw


def convert_gcode_to_array(gcode_raw):
	""" 
	function to iterate over gcode text file
	input: a iterable containing gcode text, e.g. a list of strings
	"""
	dim = (HEIGHT, WIDTH)
	array = np.zeros(dim, dtype=int)
	(x,y) = (0,0)
	for gcode_command in gcode_raw:
		letter_address = gcode_command[0:2]
		if letter_address == "G1":
			(x, y) = get_xy_position(gcode_command)
		elif letter_address == "M4":
			continue
		elif letter_address == "M7":
			firing_pattern = parse_gcode_M7(gcode_command)
			strip_array = np.array(list(firing_pattern), dtype=int)
			#print strip_array

			try:
				array[x:x+13, y] += strip_array
			except ValueError: # ValueError: operands could not be broadcast together with shapes XXX
				len_array = len(array[x:x+13, y])
				array[x:x+13, y] += strip_array[:len_array]
		else:
			raise Exception("Encountered unexpected gcode letter address: [{}]".format(letter_address))
		#print (x,y)
	return array

def parse_gcode_M7(gcode_command):
	""" 
	firing pattern is a 1-4 digit number. 
	max(firing_pattern): 4095
	min(firing_pattern): 0 [although we should never see this]
	
	Example input: [M700 P0 S1920] (without square brackets)
	"""
	command_parts = gcode_command.split(" ")
	assert len(command_parts) == 3
	firing_pattern_base_10 = command_parts[-1].lstrip('S') # last element
	try:
		firing_pattern_base_10 = int(firing_pattern_base_10)
	except:
		raise Exception("Could not convert firing_pattern_base_10 to int. firing_pattern_base_10={}".format(firing_pattern_base_10))
	firing_pattern_base_2 = bin(firing_pattern_base_10).lstrip("0b") # convert to binary
	return firing_pattern_base_2


def get_xy_position(gcode_command):
	""" extract X and Y position from gcode "G" letter address 
	Example input: [G1X0Y0F1000]"""
	pattern = re.compile(r"^G\dX(\d+(?:\.\d*)?|\.\d+)Y(\d+(?:\.\d*)?|\.\d+)F(\d+)$") # using non-capturing groups
	m = pattern.match(gcode_command) # no need for re.search() because we have a complete pattern
	(x, y) = m.group(1,2)
	try:
		x = float(x)
		y = float(y)
	except:
		raise Exception("Could not convert X and Y to floats. X={}, Y={}".format(x,y))
	x_pixel = round(x/X_STEP) # round to nearest int
	y_pixel = round(y/Y_STEP*12)
	return (x_pixel, y_pixel)


def gcode_interpreter(file_gcode):
	""" this is the main function in this module """
	gcode_raw = read_gcode(file_gcode)

	array = convert_gcode_to_array(gcode_raw)

	print array


def main():
	file_gcode = "example_files/test_excel.gcode"
	gcode_interpreter(file_gcode)

if __name__ == "__main__":
	main()
