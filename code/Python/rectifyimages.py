#!/usr/bin/python
import cv
import sys
from camfunctions import *
from camconstants import *
from stereorectify import *

def rectifyImages(im1, im2, calibdir="calib", rectdir="rect", f1="im1rect.bmp", f2="im2rect.bmp", saveImages=True):
  (CM1, CM2, D1, D2, R, T, E, F) = loadCalibration(calibdir)
  (R1, R2, P1, P2, Q, roi) = loadRectif(rectdir)

  dst1 = cv.CloneMat(im1)
  dst2 = cv.CloneMat(im2)
  print cv.GetSize(dst1)

  map1x = cv.CreateMat(480, 640, cv.CV_32FC1)
  map2x = cv.CreateMat(480, 640, cv.CV_32FC1)
  map1y = cv.CreateMat(480, 640, cv.CV_32FC1)
  map2y = cv.CreateMat(480, 640, cv.CV_32FC1)

  print "Rectifying images..."

  cv.InitUndistortRectifyMap(CM1, D1, R1, P1, map1x, map1y)
  cv.InitUndistortRectifyMap(CM2, D2, R2, P2, map2x, map2y)

  cv.Remap(im1, dst1, map1x, map1y)
  cv.Remap(im2, dst2, map2x, map2y)

  # CONTINUE WORK HERE
  print "Done."
  if saveImages:
    cv.SaveImage(f1, dst1)
    cv.SaveImage(f2, dst2)
    print "Saved images to '{0}' and '{1}'.".format(f1, f2)

  return dst1, dst2

if __name__ == "__main__":
  im1f = sys.argv[1] + ".bmp"
  im2f = sys.argv[2] + ".bmp"
  im1 = cv.LoadImageM(im1f)
  im2 = cv.LoadImageM(im2f)
  rectifyImages(im1, im2, f1 = sys.argv[1] + "rect.bmp", f2 = sys.argv[2] + "rect.bmp")
