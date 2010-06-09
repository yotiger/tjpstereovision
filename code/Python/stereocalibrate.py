import cv
from camfunctions import *
from camconstants import *
from chessboard_data import *

def stereoCalibrate(nboards, filename="chessboards.txt"):
  objectPoints = cv.CreateMat(1, COLS * ROWS * nboards, cv.CV_64FC3)
  nPoints = cv.CreateMat(1, nboards, cv.CV_32S)

  (imagePoints1, imagePoints2) = getChessboards(nboards)

  for i in range(nboards):
    for j in range(ROWS):
      for k in range(COLS):
        cv.Set1D(objectPoints, i * ROWS * COLS + j * COLS + k, (k * SQSIZE, j * SQSIZE, 0))

  for i in range(nboards):
    cv.Set1D(nPoints, i, COLS * ROWS)

  # the intrinsic camera matrices
  CM1 = cv.CreateMat(3, 3, cv.CV_64F)
  CM2 = cv.CreateMat(3, 3, cv.CV_64F)
  # the distortion coefficients of both cameras
  D1 = cv.CreateMat(1, 5, cv.CV_64F)
  D2 = cv.CreateMat(1, 5, cv.CV_64F)

  # matrices governing the rotation and translation from camera 1 to camera 2
  R = cv.CreateMat(3, 3, cv.CV_64F)
  T = cv.CreateMat(3, 1, cv.CV_64F)

  # the essential and fundamental matrices
  E = cv.CreateMat(3, 3, cv.CV_64F)
  F = cv.CreateMat(3, 3, cv.CV_64F)

  print "Running stereo calibration..."

  cv.StereoCalibrate(objectPoints, imagePoints1, imagePoints2, nPoints, CM1, D1, CM2, D2, IMSIZE, R, T, E, F,
  flags=cv.CV_CALIB_ZERO_TANGENT_DIST |
        cv.CV_CALIB_SAME_FOCAL_LENGTH)

  print "Done."
  return (CM1, CM2, D1, D2, R, T, E, F)

if __name__ == "__main__":
  stereoCalibrate(8)
