#!/usr/local/bin/python
import sys 
import cli_cracker 
import cv2 
import os

fileinput =  sys.argv[1]

if not os.path.exists('file.list'):
    print("Creating file.list")
    with open('file.list', 'w'): pass
else:
    print("Removing and creating file.list")
    os.remove("file.list")
    with open('file.list', 'w'): pass

layers, layer_directions = cli_cracker.cli_readerbinary(fileinput)

numlayers = len(layers)
print("number of layer = " + str(numlayers))

for i in range(0,numlayers,1):
    frame = cli_cracker.draw_layer(i, layers, layer_directions)
    height, width, bob = frame.shape
    revlayer = numlayers - i - 1
    print("layer = " + str(i) + ", reverse layer number = " + str(revlayer))
    jpeg_name = "layer_" + format(revlayer,'05') + ".jpg"
    jpeg_line = "layer_" + format(revlayer,'05') + ".jpg\n"
    frame[:10, :] = [0, 255, 0] 
    frame[height - 10:, :] = [0, 255, 0] 
    frame[:, :10] =  [0, 255, 0] 
    frame[:, width - 10:] = [0, 255, 0] 
    text_string1 = "YSU Humtown " + fileinput
    text_string2 = "layer = " + str(revlayer)
    cv2.putText(frame, text_string1, (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 4)
    cv2.putText(frame, text_string2, (40, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 4)
    cv2.imwrite(jpeg_name, frame)
    with open("file.list", 'r') as original: data = original.read()
    with open("file.list", 'w') as modified: modified.write(jpeg_line + data)
print "Done!"

