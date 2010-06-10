#!/usr/bin/python

import cv
from camfunctions import *
from camconstants import *
from chessboard_data import *

def stereoCalibrate(nboards, filename="chessboards.txt"):
  objectPoints = cv.CreateMat(1, COLS * ROWS * nboards, cv.CV_32FC3)
  nPoints = cv.CreateMat(1, nboards, cv.CV_32S)

  (imagePoints1, imagePoints2) = getChessboards(nboards)

  for i in range(nboards):
    for j in range(ROWS):
      for k in range(COLS):
        cv.Set1D(objectPoints, i * ROWS * COLS + j * COLS + k, (k * SQSIZE, j * SQSIZE, 0))
# DEBUG STATEMENTS
#        print cv.Get1D(objectPoints, i * ROWS * COLS  + j * COLS + k)
#        print cv.Get1D(imagePoints1, i * ROWS * COLS  + j * COLS + k)
#        print cv.Get1D(imagePoints2, i * ROWS * COLS  + j * COLS + k)

  for i in range(nboards):
    cv.Set1D(nPoints, i, COLS * ROWS)

  CM1 = cv.CreateMat(3, 3, cv.CV_64F)
  CM2 = cv.CreateMat(3, 3, cv.CV_64F)
  D1 = cv.CreateMat(1, 5, cv.CV_64F)
  D2 = cv.CreateMat(1, 5, cv.CV_64F)
  R = cv.CreateMat(3, 3, cv.CV_64F)
  T = cv.CreateMat(3, 3, cv.CV_64F)
  E = cv.CreateMat(3, 3, cv.CV_64F)
  F = cv.CreateMat(3, 3, cv.CV_64F)

  print "Running stereo calibration..."

  cv.StereoCalibrate(objectPoints, imagePoints1, imagePoints2, nPoints, CM1, D1, CM2, D2, IMSIZE, R, T, E, F,
  flags=cv.CV_CALIB_ZERO_TANGENT_DIST |
        cv.CV_CALIB_SAME_FOCAL_LENGTH)

  print "Done."

if __name__ == "__main__":
  stereoCalibrate(8)
