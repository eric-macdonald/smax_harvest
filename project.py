from collections import deque
import sys
sys.path.append('/home/pi/.virtualenvs/cv4/lib/python2.7/site-packages')
import struct
import numpy as np
import time
from matplotlib import pyplot as plt
import datetime
import re
import cv2
import math
import datetime
import itertools 

filelist = open('/home/pi/projection/file.list', 'r')
height = 500
width = 900
layer_names = []

cv2.namedWindow('Outwindow', cv2.WND_PROP_FULLSCREEN) #create display window
cv2.setWindowProperty('Outwindow', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

for idx1, jpg in enumerate(filelist):
    layer_names.append(jpg)

layer_index = 0
previous_layer_index = 1

while True:
    if(layer_index != previous_layer_index):
        previous_layer_index = layer_index 
        #print layer_names[layer_index]
        frame = cv2.imread(layer_names[layer_index].rstrip())
        #frame = cv2.imread(layer_names[layer_index])
        #print frame.shape
        #frame = cv2.resize(frame, (width, height))
        #print frame.shape
        cv2.imshow('Outwindow', frame)
        key = cv2.waitKey(0) #Activates the window and reads any key inputs
        if(key != -1): #Key inputs
            if(key == 27): #Esc
                quit #Exit loop
            elif(key == 113): #Up arrow key
                quit
            elif(key == 65362): #Up arrow key
                layer_index = layer_index + 1 
            elif(key == 65364): #Down arrow key
                layer_index = layer_index - 1 
            elif(key == 119): #W key
                layer_index = layer_index + 5 
            elif(key == 115): #S key
                layer_index = layer_index - 5 

cv2.destroyAllWindows() #closes all open windows
    
