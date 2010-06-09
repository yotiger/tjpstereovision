import cv
from camfunctions import *
from camconstants import *
from stereorectify import *

def rectifyImages(im1, im2, calibdir="calib", rectdir="rect", f1="im1rect.png", f2="im2rect.png"):
  (CM1, CM2, D1, D2, R, T, E, F) = loadCalibration(calibdir)
  (R1, R2, P1, P2, Q) = loadRectif(rectdir)

  dst1 = cv.CloneMat(im1)
  dst2 = cv.CloneMat(im2)

  print "Rectifying images..."
  # CONTINUE WORK HERE
  cv.Undistort2(im1, dst1, CM1, D1, P1)
  cv.Undistort2(im2, dst2, CM2, D2, P2)
  print "Done."
  cv.SaveImage(f1, dst1)
  cv.SaveImage(f2, dst2)
  print "Saved images to '{0}' and '{1}'.".format(f1, f2)

if __name__ == "__main__":
  # HARDCODED DEBUG STATEMENTS
  im1 = cv.LoadImageM("im1.ppm"))
  im2 = cv.LoadImageM("im2.ppm")
  rectifyImages(im1, im2)
