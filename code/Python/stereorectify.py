import cv
from camfunctions import *
from camconstants import *

def stereoRectify():
  name1 = "Camera 1"
  name2 = "Camera 2"

  (cam1, cam2) = genCamWindows(name1, name2)
  (fp1, fp2, fund) = findFund(cam1, cam2, name1)

  h1 = cv.CreateMat(3, 3, cv.CV_32FC1)
  h2 = cv.CreateMat(3, 3, cv.CV_32FC1)

  cv.StereoRectifyUncalibrated(fp1, fp2, fund, IMSIZE, h1, h2)
  print "Created homography matrices for stereo rectifying."
  cv.DestroyAllWindows()
  return (h1, h2)
