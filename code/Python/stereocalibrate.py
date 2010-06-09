import cv
import os.path
from optparse import OptionParser
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

def saveCalibration(cal, dir="calib"):
  filenames = ("CM1.txt", "CM2.txt", "D1.txt", "D2.txt", "R.txt", "T.txt", "E.txt", "F.txt")
  if not os.path.isdir(dir):
    print "Error: Dir {0} doesn't exist. Exiting.".format(dir)
    sys.exit(1)
  assert(len(filenames) == 8)
  (CM1, CM2, D1, D2, R, T, E, F) = cal
  cv.Save("{0}/{1}".format(dir, filenames[0]), CM1)
  cv.Save("{0}/{1}".format(dir, filenames[1]), CM2)
  cv.Save("{0}/{1}".format(dir, filenames[2]), D1)
  cv.Save("{0}/{1}".format(dir, filenames[3]), D2)
  cv.Save("{0}/{1}".format(dir, filenames[4]), R)
  cv.Save("{0}/{1}".format(dir, filenames[5]), T)
  cv.Save("{0}/{1}".format(dir, filenames[6]), E)
  cv.Save("{0}/{1}".format(dir, filenames[7]), F)
  print "Calibration parameters written to directory '{0}'.".format(dir)

def loadCalibration(dir="calib"):
  filenames = ("CM1.txt", "CM2.txt", "D1.txt", "D2.txt", "R.txt", "T.txt", "E.txt", "F.txt")
  for fn in ["{0}/{1}".format(dir, f) for f in filenames]:
    if not os.path.exists(fn):
      print "Error: File {0} doesn't exists. Exiting.".format(fn)
      sys.exit(1)
  CM1 = cv.Load("{0}/{1}".format(dir, filenames[0]))
  CM2 = cv.Load("{0}/{1}".format(dir, filenames[1]))
  D1 = cv.Load("{0}/{1}".format(dir, filenames[2]))
  D2 = cv.Load("{0}/{1}".format(dir, filenames[3]))
  R = cv.Load("{0}/{1}".format(dir, filenames[4]))
  T = cv.Load("{0}/{1}".format(dir, filenames[5]))
  E = cv.Load("{0}/{1}".format(dir, filenames[6]))
  F = cv.Load("{0}/{1}".format(dir, filenames[7]))
  print "Calibration files loaded from dir '{0}'.".format(dir)
  return (CM1, CM2, D1, D2, R, T, E, F)

if __name__ == "__main__":
  parses = OptionParser()

  parses.add_option("-c", "--chessboards", dest="chessboards", help="use chessboards in file CHESSBOARDS", metavar="CHESSBOARDS", default="chessboards.txt")
  parses.add_option("-n", "--numboards", dest="n", help="use N chessboards for calibration", metavar="N", default="8")
  parses.add_option("-d", "--dir", dest="dir", help="store calibration in DIR", metavar="DIR", default="calib")

  (options, args) = parses.parse_args()

  saveCalibration(stereoCalibrate(int(options.n), options.chessboards), options.dir)
