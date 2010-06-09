import cv
from camfunctions import *
from stereorectify import *

def getStereoImages():
  (h1, h2) = stereoRectify()
  (c1, c2) = genCamWindows("Cam 1", "Cam 2")
  M1 = cv.CreateMat(3, 3, cv.CV_64F)
  D1 = cv.CreateMat(1, 5, cv.CV_64F)
  H1 = cv.CreateMat(3, 3, cv.CV_64F)
  H2 = cv.CreateMat(3, 3, cv.CV_64F)
  cv.SetIdentity(M1)
  cv.Zero(D1)
  map1x = cv.CreateMat(640, 480, cv.CV_32FC1)
  map1y = cv.CreateMat(640, 480, cv.CV_32FC1)
  map2x = cv.CreateMat(640, 480, cv.CV_32FC1)
  map2y = cv.CreateMat(640, 480, cv.CV_32FC1)
  cv.InitUndistortRectifyMap(M1, D1, H1, M1, map1x, map1y)
  cv.InitUndistortRectifyMap(M1, D1, H2, M1, map2x, map2y)

  print "Press <space> to get stereo image pair."

  while 1:
    frame1 = cv.QueryFrame(c1)
    frame2 = cv.QueryFrame(c2)

    cv.ShowImage("Cam 1", frame1)
    cv.ShowImage("Cam 2", frame2)

    k = cv.WaitKey(10)

    if k == 0x20:
      cv.Remap(frame1, frame1, map1x, map1y)
      cv.Remap(frame2, frame2, map2x, map2y)
      print frame1
      print frame2
    
    if k == 0x1b:
      print "ESC pressed. Exiting..."
      break


if __name__ == "__main__":
  getStereoImages()
