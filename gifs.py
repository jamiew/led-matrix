#!/usr/bin/python
 
# http://effbot.org/imagingbook/image.htm
# http://effbot.org/imagingbook/imagedraw.htm
 
import Image
import ImageDraw
import time
from rgbmatrix import Adafruit_RGBmatrix
 
# Rows and chain length are both required parameters:
matrix = Adafruit_RGBmatrix(32, 1)

# filename = "corgi.gif"
# filename = "togepi.gif"
# filename = "moogle.gif"
# filename = "raising.gif"
# filename = "duck.gif"
# filename = "mainframe.gif" # TODO need to resize to 32x32
# filename = "vhx-irondavy-smaller.gif"

filenames = ['corgi', 'togepi', 'moogle', 'raisin', 'duck']

file_index = 0

while True:
	filename = filenames[file_index % len(filenames)]
	print "Looping " + filename
	image = Image.open("img/" + filename + ".gif")	

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

