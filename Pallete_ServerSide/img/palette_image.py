#!/usr/bin/env python3.2
import time
import serial
import sys
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img_path = sys.argv[1]
text = str(sys.argv[2])
num  = sys.argv[3]

ser = serial.Serial('/dev/ttyACM0', 3000000, timeout=1, writeTimeout=None)
image = open(img_path, "rb")

# start screen transmission
ser.write(('{"screen_write":' + str(num) + '}').encode('ascii'))

# skip header file
image.seek(54, 0)

# generate rgb colour table from srgb table
color_table_srgb = list(image.read(64))
del color_table_srgb[3::4]

# write colour table
ser.write(bytearray(color_table_srgb))

# write image matrix
ser.write(image.read(8192))

ser.close()
