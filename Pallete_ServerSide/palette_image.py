#!/usr/bin/env python3.3
import time
import sys
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


img_path = "red.bmp"
text = "MAMAD"
num  = 23
img = Image.open(img_path)
img = img.convert('RGB')

#12--red
#13--Yellow
#14--Green
#15--White
#16--blue
#17--Black
#18--red-command
#19--Yellow-command
#20--Green-command
#21--White-command
#22--blue-command
#23--Black-command



#draw = ImageDraw.Draw(img)
#font = ImageFont.truetype('/usr/share/fonts/truetype/cwoldeng.ttf', 48)
#draw.text((64-len(text)*12, 30), text, fill="white")
#img.save("palette_temp.bmp")


#command = "convert palette_temp.bmp -resize 128x128\! -dither FloydSteinberg -colors 16 BMP3:" + os.path.splitext(img_path)[0] + "_16.bmp"
#os.system(command);
#os.system("convert palette_temp.bmp -resize 128x128\! -colors 16 BMP3:palette_temp_16.bmp")
#os.system("convert palette_temp.bmp -resize 128x128\! -dither FloydSteinberg -colors 16 BMP3:palette_temp_16.bmp")

ser = serial.Serial('COM5', 3000000, timeout=1, writeTimeout=None)
image = open("black-command.bmp", "rb")

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
