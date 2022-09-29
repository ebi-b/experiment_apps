#!/usr/bin/env python3.3
import time
import serial
import sys
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img_path = "red-16.bmp"
#text = str(sys.argv[2])
#num  = sys.argv[3]
img = Image.open(img_path)
img = img.convert('RGB')

img.save("RED_temp.bmp")

#command = "convert palette_temp.bmp -colors 16 BMP3:" + os.path.splitext(img_path)[0] + "_16.bmp"

#os.system(command);
