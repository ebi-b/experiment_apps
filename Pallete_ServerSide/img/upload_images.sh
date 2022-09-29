#!/bin/bash

./palette_timeout.py 1

./palette_image.py Palette_16.bmp "" 0 && echo palette
sleep 0.1
./palette_image.py PS_16.bmp "" 1 && echo ps
sleep 0.1
./palette_image.py LR_16.bmp "" 2 && echo lr
sleep 0.1
./palette_image.py AE_16.bmp "" 3 && echo ae
sleep 0.1
./palette_image.py MIDI_16.bmp "" 4 && echo MIDI
sleep 0.1
./palette_image.py Keyboard_16.bmp "" 5 && echo key
sleep 0.1
./palette_image.py Ai_16.bmp "" 6 && echo ai
sleep 0.1
./palette_image.py joystick_16.bmp "" 7 && echo joystick 
sleep 0.1
./palette_image.py FCC_16.bmp "" 8 && echo FCC
sleep 0.1
./palette_image.py ID_16.bmp "" 9 && echo ID
sleep 0.1
./palette_image.py PR_16.bmp "" 10 && echo PR

./palette_timeout.py 0
