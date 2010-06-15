#!/usr/bin/python 
from stereoheader import *

def stereoRectify(calibdir="calib"):
  (CM1, CM2, D1, D2, R, T, E, F) = loadCalibration(calibdir)
  R1 = cv.CreateMat(3, 3, cv.CV_64F)
  R2 = cv.CreateMat(3, 3, cv.CV_64F)
  P1 = cv.CreateMat(3, 4, cv.CV_64F)
  P2 = cv.CreateMat(3, 4, cv.CV_64F)
  Q = cv.CreateMat(4, 4, cv.CV_64F)

  print "Running stereo rectification..."
  (leftroi, rightroi) = cv.StereoRectify(CM1, CM2, D1, D2, IMSIZE, R, T, R1, R2, P1, P2, Q)
  roi = []
  roi.append(max(leftroi[0], rightroi[0]))
  roi.append(max(leftroi[1], rightroi[1]))
  roi.append(min(leftroi[2], rightroi[2]))
  roi.append(min(leftroi[3], rightroi[3]))
  print "Done."
  return (R1, R2, P1, P2, Q, roi)

def saveRectif(rect, dir="rect"):
  filenames = ("R1.txt", "R2.txt", "P1.txt", "P2.txt", "Q.txt", "ROI.txt")
  if not os.path.isdir(dir):
    print "Error: Dir {0} doesn't exist. Exiting.".format(dir)
    sys.exit(1)
  (R1, R2, P1, P2, Q, roi) = rect

  cv.Save("{0}/{1}".format(dir, filenames[0]), R1)
  cv.Save("{0}/{1}".format(dir, filenames[1]), R2)
  cv.Save("{0}/{1}".format(dir, filenames[2]), P1)
  cv.Save("{0}/{1}".format(dir, filenames[3]), P1)
  cv.Save("{0}/{1}".format(dir, filenames[4]), Q)

  f = open("{0}/{1}".format(dir, filenames[5]), 'w')
  f.write("{0}\n".format(' '.join([str(c) for c in roi])))
  f.close()

  print "Rectification parameters written to directory '{0}'.".format(dir)

def loadRectif(dir="rect"):
  filenames = ("R1.txt", "R2.txt", "P1.txt", "P2.txt", "Q.txt", "ROI.txt")
  for fn in ["{0}/{1}".format(dir, f) for f in filenames]:
    if not os.path.exists(fn):
      print "Error: File {0} doesn't exists. Exiting.".format(fn)
      sys.exit(1)
  R1 = cv.Load("{0}/{1}".format(dir, filenames[0]))
  R2 = cv.Load("{0}/{1}".format(dir, filenames[1]))
  P1 = cv.Load("{0}/{1}".format(dir, filenames[2]))
  P2 = cv.Load("{0}/{1}".format(dir, filenames[3]))
  Q = cv.Load("{0}/{1}".format(dir, filenames[4]))

  f  = open("{0}/{1}".format(dir, filenames[5]))
  roi = tuple([int(x) for x in f.readline().split()])

  print "Rectification parameters loaded from dir '{0}'.".format(dir)
  return (R1, R2, P1, P2, Q, roi)

if __name__ == "__main__":
  saveRectif(stereoRectify())
