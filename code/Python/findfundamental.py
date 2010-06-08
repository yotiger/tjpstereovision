import cv
from camfunctions import *
from camconstants import *

def findFund(cam1, cam2, window):

  foundpoints1 = cv.CreateMat(1, COLS * ROWS, cv.CV_32FC2)
  foundpoints2 = cv.CreateMat(1, COLS * ROWS, cv.CV_32FC2)

  while 1:
    f1 = cv.QueryFrame(cam1)
    f2 = cv.QueryFrame(cam2)
    cv.ShowImage(window, f1)

    k = cv.WaitKey(10)
    if k == 0x1b:
      break
    if k == 0x20:
      cor1 = cv.FindChessboardCorners(f1, (10, 7))
      cor2 = cv.FindChessboardCorners(f2, (10, 7)) 

      if cor1[0] == 0 or cor2[0] == 0:
        print "Chessboard not found. Try again."
        continue

      for i in range(0, len(cor1)):
        cv.Set2D(foundpoints1, 0, i, (cor1[1][i][0], cor1[1][i][1]))
        cv.Set2D(foundpoints2, 0, i, (cor2[1][i][0], cor2[1][i][1]))

      print "Found chessboard."
      break

  print "Calculating fundamental matrix..."
  fund = cv.CreateMat(3, 3, cv.CV_32FC1)
  cv.FindFundamentalMat(foundpoints1, foundpoints2, fund)
  print "Fundamental matrix calculated."
  return (foundpoints1, foundpoints2, fund)

if __name__ == "__main__":
  (c1, c2) = genCamWindows("Cam 1", "Cam 2")
  findFund(c1, c2, "Cam 1")
