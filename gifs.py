#!/usr/bin/python

# http://effbot.org/imagingbook/image.htm
# http://effbot.org/imagingbook/imagedraw.htm

import Image
import ImageDraw
import time
import sys
import os
import glob
import random
from rgbmatrix import Adafruit_RGBmatrix

# Rows and chain length are both required parameters:
matrix = Adafruit_RGBmatrix(32, 1)

if len(sys.argv) > 1:
	gifs_dir = sys.argv[1]
else:
	gifs_dir = "img5"

dir = os.path.dirname(os.path.realpath(__file__)) + "/" + gifs_dir
print dir
filenames = glob.glob(dir + "/*.gif")
random.shuffle(filenames)

file_index = 0
# size = 32, 32
# image.thumbnail() not behaving - dynamic resizing
speed = 0.12

while True:
	filename = filenames[file_index % len(filenames)]
	print "Looping " + filename
	image = Image.open(filename)

	loops = 0
	frame = 0

	matrix.Fill(0x000000)

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
		print image.im.id
		matrix.SetImage(image.im.id, 0, 0)
		time.sleep(speed)

	file_index += 1

matrix.Clear()

