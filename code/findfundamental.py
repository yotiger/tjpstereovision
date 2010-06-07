import cv
from camfunctions import *
from camconstants import *

n1 = "Cam 1"
n2 = "Cam 2"
(c1, c2) = genCamWindows(n1, n2)

foundpoints1 = cv.CreateMat(8 * COLS * ROWS, 2, cv.CV_32FC1)
foundpoints2 = cv.CreateMat(8 * COLS * ROWS, 2, cv.CV_32FC1)
count = 0

while 1:
  f1 = cv.QueryFrame(c1)
  f2 = cv.QueryFrame(c2)
  cv.ShowImage(n1, f1)

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
      cv.Set2D(foundpoints1, count * 8 + i, 0, cor1[1][i][0])
      cv.Set2D(foundpoints1, count * 8 + i, 1, cor1[1][i][1])
      cv.Set2D(foundpoints2, count * 8 + i, 0, cor2[1][i][0])
      cv.Set2D(foundpoints2, count * 8 + i, 1, cor2[1][i][1])

    count += 1
    print "Found {0} chessboards.".format(count)
    if count == 8:
      break

print "Calculating fundamental matrix..."
fund = cv.CreateMat(3, 3, cv.CV_32FC1)
cv.FindFundamentalMat(foundpoints1, foundpoints2, fund)
print "Fundamental matrix calculated."
