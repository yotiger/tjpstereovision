import cv
from camfunctions import *
from camconstants import *
from stereorectify import *

name1 = "Camera 1"
name2 = "Camera 2"

(cam1, cam2) = genCamWindows(name1, name2)
(fp1, fp2, fund) = findFund(cam1, cam2, name1)

h1 = cv.CreateMat(3, 3, cv.CV_32FC1)
h2 = cv.CreateMat(3, 3, cv.CV_32FC1)

cv.StereoRectifyUncalibrated(fp1, fp2, fund, IMSIZE, h1, h2)

print "Press <space> to generate rectified image pair."

#while 1:
#    f1 = cv.QueryFrame(cam1)
#    f2 = cv.QueryFrame(cam2)
#    cv.ShowImage(window, f1)
#
#    k = cv.WaitKey(10)
#    if k == 0x1b:
#      break
#    if k == 0x20:
