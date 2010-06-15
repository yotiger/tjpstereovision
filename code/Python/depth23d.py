#!/usr/bin/python

import cv
import sys
from stereorectify import loadRectif

disp = cv.LoadImageM(sys.argv[1], cv.CV_LOAD_IMAGE_GRAYSCALE)

threedimg = cv.CreateMat(disp.rows, disp.cols, cv.CV_16SC1)

(R1, R2, P1, P2, Q) = loadRectif("../../dataset/owndataset1/rect")

disp.type = 3
print Q.type
print threedimg.type

cv.ReprojectImageTo3D(disp, threedimg, Q)

cv.SaveImage("3dimg.jpg", threedimg)
