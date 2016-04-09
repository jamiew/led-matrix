#!/usr/bin/python

# http://effbot.org/imagingbook/image.htm
# http://effbot.org/imagingbook/imagedraw.htm

import Image
import ImageDraw
import time
import os
import glob
import random
from rgbmatrix import Adafruit_RGBmatrix

# Rows and chain length are both required parameters:
matrix = Adafruit_RGBmatrix(32, 1)

filenames = glob.glob("img/*.gif")
random.shuffle(filenames)

file_index = 0
# size = 32, 32
# image.thumbnail() not behaving - dynamic resizing

while True:
	filename = filenames[file_index % len(filenames)]
	print "Looping " + filename
	image = Image.open(filename)

	loops = 0
	frame = 0

	while loops < 5:
		print "Frame: " + str(frame)
		try:
			image.seek(frame)
			frame += 1
		except EOFError:
			frame = 0
			loops += 1
			print 'EOFError ' + filename + ' loops = ' + str(loops)
			continue

		image.load()
		matrix.SetImage(image.im.id, 0, 0)
		time.sleep(0.1)

	file_index += 1

matrix.Clear()

