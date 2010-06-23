"""
Defines functions used to get chessboard data from stereo cams,
saving this to a file and reloading it
"""
from stereoheader import *
import errors
import os

def getChessboards(n, fname="chessboards.txt"):
  """
  Load chessboard point coordinates from file.

  n - number of boards to load from file
  fname - filename of file to load coordinates from
  """
  p1 = cv.CreateMat(1, n * COLS * ROWS, cv.CV_64FC2)
  p2 = cv.CreateMat(1, n * COLS * ROWS, cv.CV_64FC2)

  errors.checkexists(fname)
  f = open(fname, 'r')
  lr = 0
  for j in range(n):
    for i in range(COLS * ROWS):
      c1 = f.readline()
      c2 = f.readline()
      c1 = c1.split()
      c2 = c2.split()

      cv.Set1D(p1, j * COLS * ROWS + i, cv.Scalar(float(c1[0]), float(c1[1])))
      cv.Set1D(p2, j * COLS * ROWS + i, cv.Scalar(float(c2[0]), float(c2[1])))
    f.readline()
  return (p1, p2)

def writeChessboards(cap1, cap2, n1, n2, n=8, fname="chessboards.txt"):
  f = open(fname, 'w')

  count = 0
  while 1:
    f1 = cv.QueryFrame(cap1)
    f2 = cv.QueryFrame(cap2)
    cv.ShowImage(n1, f1)
    cv.ShowImage(n2, f2)

    k = cv.WaitKey(10)
    if k == 0x1b: # esc
      print "ESC pressed. Exiting. WARNING: NOT ENOUGH CHESSBOARDS FOUND YET"
      break
    if k == 0x20 or k == 0x73: # space or s (show)
      cor1 = cv.FindChessboardCorners(f1, (10, 7))
      cor2 = cv.FindChessboardCorners(f2, (10, 7))

      if cor1[0] == 0 or cor2[0] == 0:
        print "Chessboard not found. Try again."
        continue
      
      # write to file
      for i in range(0, len(cor1[1])):
        f.write("{0} {1}\n".format(cor1[1][i][0], cor1[1][i][1]))
        f.write("{0} {1}\n".format(cor2[1][i][0], cor2[1][i][1]))

      count += 1

      # show chessboard if user pressed 's'
      if k == 0x73:
        cv.DrawChessboardCorners(f1, (10,7), cor1[1], 1)
        cv.DrawChessboardCorners(f2, (10,7), cor2[1], 1)
        cv.ShowImage(n1, f1)
        cv.ShowImage(n2, f2)
        cv.WaitKey(2000) # wait some time

      if count == n:
        print "Found {0} chessboards. Exiting.".format(n)
        f.close()
        break
        
      f.write("---\n")
      print "Found and wrote chessboard."



if __name__ == "__main__":
  (c1, c2) = genCamWindows("Camera 1", "Camera 2")
  writeChessboards(c1, c2, "Camera 1", "Camera 2")
