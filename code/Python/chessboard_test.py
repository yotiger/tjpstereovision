import cv
import sys

cv.NamedWindow("Camera 1", cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow("Result", cv.CV_WINDOW_AUTOSIZE)

cam = 1
capture = cv.CaptureFromCAM(cam)

cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH, 640)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

if not capture:
    print "Error opening cam {0}".format(cam1)
    sys.exit(1)

while 1:
    frame = cv.QueryFrame(capture)
    if frame == None:
        break

    cv.ShowImage('Camera 1', frame)
    k = cv.WaitKey(10)

    resframe = cv.QueryFrame(capture)
    corners = cv.FindChessboardCorners(frame, (10, 7))
    if corners[0]:
        cv.DrawChessboardCorners(resframe, (10, 7), corners[1], corners[0])
        cv.ShowImage('Result', resframe)

    if k == 0x1b:
        print "ESC pressed. Exiting..."
        break
