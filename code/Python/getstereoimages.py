#!/usr/bin/python
from stereoheader import *

def getStereoImages():
  (c1, c2) = genCamWindows("Cam 1", "Cam 2")

  print "Press <space> to get stereo image pair."

  count = 1
  while 1:
    frame1 = cv.QueryFrame(c1)
    frame2 = cv.QueryFrame(c2)

    cv.ShowImage("Cam 1", frame1)
    cv.ShowImage("Cam 2", frame2)

    k = cv.WaitKey(10)

    if k == 0x20:
      print "Image pair saved."
      cv.SaveImage("im{0}.bmp".format(count), frame1)
      cv.SaveImage("im{0}.bmp".format(count + 1), frame2)
      count += 2
    
    if k == 0x1b:
      print "ESC pressed. Exiting..."
      break

if __name__ == "__main__":
  getStereoImages()
