#!/usr/bin/env python2.7

import csv
import numpy as np

from config import *

import pdb

################## TODO ##################
#1) Dealing with newline endings
#2) catch potential numpy errors in conversion to int


def check_csv_file(filename):
	fh_csv = open(filename, 'rb')
	try:
		dialect = csv.Sniffer().sniff(fh_csv.read(1024))
		fh_csv.seek(0) # reset the read position back to the start of file
	except csv.Error:
		# File appears not to be in CSV format; move along
		pass
	return dialect # FIX THIS

def read_csv_file(filename, dialect):
	#with open(filename, 'rb') as fh_csv: # _csv.Error: new-line character seen in unquoted field - do you need to open the file in universal-newline mode?
	with open(filename, 'rU') as fh_csv: # TODO
		csv_array = csv.reader(fh_csv, dialect=dialect) # reference to csv reader
		#csv_array_list = list(csv_array) # gives a list of list, e.g [['1', '6', '11'], ['2', '7', '12'], ['3', '8', '13'], ['4', '9', '14'], ['5', '10', '15']]
		csv_numpy = np.array(list(csv_array)).astype('int') # float
			### --> TODO: error check for conversion
	return csv_numpy

def check_dimensions(array):
	dim = array.shape
	if not ((dim[0] == HEIGHT) and (dim[1] == WIDTH)):
		raise Exception("Dimension does not agree with config file. Input dimensions: {}. Config dimensions: ({},{})".format(dim, HEIGHT, WIDTH))


def normalize_intensity(array):
	max_val = np.amax(array) # Maximum of the flattened array ---> returns float!
	array_norm = array * MAX_INTENSITY/max_val
	array_norm = array_norm.astype(int) # solve
	return array_norm


def csv_import(file_csv):
	#file_csv = "example_files/test_excel.csv"
	dialect = check_csv_file(file_csv)
	csv_numpy = read_csv_file(file_csv, dialect)
	#print csv_numpy

	### valdation
	check_dimensions(csv_numpy)

	csv_numpy_norm = normalize_intensity(csv_numpy)
	#print csv_numpy_norm

	return csv_numpy_norm





