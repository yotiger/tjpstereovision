
import cv
import sys

disp = cv.LoadImageM(sys.argv[1], cv.CV_LOAD_IMAGE_GRAYSCALE)

3dimg = cv.createMat(disp.rows, disp.cols, CV_16S)

