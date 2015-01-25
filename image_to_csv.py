#!/usr/bin/env python2.7

import os

import numpy as np
from scipy import misc


from config import *

################## TODO ##################
# 1)	Consider converting the image array to int dtype. In this way we are sure that the image always are written as integers
#		However, we do not need to only accept ints for the csv file


def read_image(filename):
	""" 
	Documentation for .imread(): https://docs.scipy.org/doc/scipy-0.14.1/reference/generated/scipy.misc.imread.html
	Note we use the "flatten=True" option.
	The different colour bands/channels are stored in the third dimension, such that a grey-image is MxN, an RGB-image MxNx3 and an RGBA-image MxNx4. 
	"""
	try:
		img_array = misc.imread(filename, flatten=True)
	except: #TODO: find exception class
		raise Exception("Could not read image file: {}".format(filename))
	return img_array

def check_dimensions(array):
	dim = array.shape
	assert dim[0] == HEIGHT
	assert dim[1] == WIDTH

def write_csv_file(array, filename):
	""" write image array to a specified path """
	np.savetxt(filename, array, delimter=",")


def image_to_csv(filename):
	""" main function """
	filename = os.path.abspath(filename)

	array = read_image(filename)
	check_dimensions(array)

	csv_path = os.path.dirname(filename)
	csv_filename = "{path}/{basename}.{ext}".format(path=csv_path, basename=os.path.splitext(os.path.basename(filename))[0], ext="csv")
	write_csv_file(array, csv_filename)

	return array
	





