#!/usr/bin/env python2.7

import os

import numpy as np
from scipy import misc

import csv_import

from config import *


import matplotlib
matplotlib.use('Agg') #Agg backend and not an X-using backend that required an X11 connection. Call use BEFORE importing pyplot!
# REF: http://stackoverflow.com/questions/4931376/generating-matplotlib-graphs-without-a-running-x-server
import matplotlib.pyplot as plt # needed for plotting


################## TODO ##################
# 1)	Consider converting the image array to int dtype. In this way we are sure that the image always are written as integers
#		However, we do not need to only accept ints for the csv file

# write out image/heatmap file?
# 


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
	
	img_array_int = img_array.astype(int)

	return img_array

def check_dimensions(array):
	dim = array.shape
	assert dim[0] == HEIGHT
	assert dim[1] == WIDTH

def write_csv_file(array, filename):
	""" write image array to a specified path """
	np.savetxt(filename, array, delimiter=",")


def plot_1x2_heatmap(array, array_norm, filename):
	# .imshow(): http://matplotlib.org/api/pyplot_api.html?highlight=imshow#matplotlib.pyplot.imshow
	# .pcolor(): http://matplotlib.org/api/image_api.html?highlight=pcolor#matplotlib.image.pcolor
	
	cmap = matplotlib.cm.get_cmap('gray')

	plt.subplot(1, 2, 1)
	#plt.imshow(array)
	plt.imshow(array, cmap=cmap)
	plt.title('array')

	plt.subplot(1, 2, 2)
	#plt.imshow(array_norm)
	plt.imshow(array_norm, cmap=cmap)
	plt.title('array_norm')

	# # or what ever color map you want
	#plt.show()
	
	plt.savefig(filename) # Most backends support png, pdf, ps, eps and svg.

	#Change color map
	#plt.pcolor(data,cmap=plt.cm.Reds,edgecolors='k')

def image_to_csv(filename):
	""" main function """
	filename = os.path.abspath(filename)

	array = read_image(filename)
	check_dimensions(array)

	### Call normalize function from "csv_import" module
	#array_norm = csv_import.normalize_intensity(array)
	array_norm = array

	path_out = os.path.dirname(filename)
	csv_filename = "{path}/{basename}.{ext}".format(path=path_out, basename=os.path.splitext(os.path.basename(filename))[0], ext="csv")
	#write_csv_file(array, csv_filename)
	write_csv_file(array_norm, csv_filename)

	### plot it.
	plot_filename = "{path}/{basename}.arrayplot.{ext}".format(path=path_out, basename=os.path.splitext(os.path.basename(filename))[0], ext="png")
	plot_1x2_heatmap(array, array_norm, plot_filename) # the extension of the filename determines the output format of the image

	return array_norm
	





