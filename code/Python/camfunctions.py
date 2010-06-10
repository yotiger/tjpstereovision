from stereoheader import *

def genCamWindows(n1, n2):
  cv.NamedWindow(n1, cv.CV_WINDOW_AUTOSIZE)
  cv.NamedWindow(n2, cv.CV_WINDOW_AUTOSIZE)

  cam1 = 1
  cam2 = 2
  capture1 = cv.CaptureFromCAM(cam1)
  capture2 = cv.CaptureFromCAM(cam2)

  cv.SetCaptureProperty(capture1, cv.CV_CAP_PROP_FRAME_WIDTH, 640)
  cv.SetCaptureProperty(capture1, cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
  cv.SetCaptureProperty(capture2, cv.CV_CAP_PROP_FRAME_WIDTH, 640)
  cv.SetCaptureProperty(capture2, cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

  if not capture1:
      print "Error opening cam {0}".format(cam1)
      sys.exit(1)

  if not capture2:
      print "Error opening cam {0}".format(cam2)
      sys.exit(1)

  return (capture1, capture2)

def showCam(capture, window):
  while 1:
    frame = cv.QueryFrame(capture)
    if frame == None:
      break

    cv.ShowImage(window, frame)
    k = cv.WaitKey(10)

    if k == 0x1b:
      print "ESC pressed. Exiting..."
      break
