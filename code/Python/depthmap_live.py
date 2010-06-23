#!/usr/bin/python
# Depthmap Live: view live depthmap
# University of Amsterdam
# Stereo Vision project, June 2010

import cv
import sys
from stereoheader import *
from stereo_bm_test import *

if __name__ == "__main__":

  CAM_LEFT  = 1
  CAM_RIGHT = 2

  # parse commandline args
  if len(sys.argv) > 1 and sys.argv[1] == "remove-bg":
    remove_background = True
  else:
    remove_background = False

  # init vars
  capture_left  = cv.CaptureFromCAM(CAM_LEFT)
  capture_right = cv.CaptureFromCAM(CAM_RIGHT)
  cv.SetCaptureProperty(capture_left,  cv.CV_CAP_PROP_FRAME_WIDTH,  640)
  cv.SetCaptureProperty(capture_left,  cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
  cv.SetCaptureProperty(capture_right, cv.CV_CAP_PROP_FRAME_WIDTH,  640)
  cv.SetCaptureProperty(capture_right, cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

  cv.NamedWindow("leftimage", cv.CV_WINDOW_AUTOSIZE)
  cv.NamedWindow("rightimage", cv.CV_WINDOW_AUTOSIZE)

  while 1:

    # get frames
    frame_left_col  = cv.QueryFrame(capture_left)
    frame_right_col = cv.QueryFrame(capture_right)

    frame_left  = cv.CreateImage( (frame_left_col.width, frame_left_col.height), \
                          frame_left_col.depth, 1)
    frame_right = cv.CreateImage( (frame_right_col.width, frame_right_col.height), \
                          frame_right_col.depth, 1)
    cv.CvtColor(frame_left_col,  frame_left,  cv.CV_BGR2GRAY)
    cv.CvtColor(frame_right_col, frame_right, cv.CV_BGR2GRAY)

    framem_left  = cv.CreateMat(480, 640, cv.CV_16UC1)
    framem_right = cv.CreateMat(480, 640, cv.CV_16UC1)
    framem_left_col  = cv.CreateMat(480, 640, cv.CV_16UC3)
    framem_right_col = cv.CreateMat(480, 640, cv.CV_16UC3)
    cv.Convert(frame_left,  framem_left)
    cv.Convert(frame_right, framem_right)
    cv.Convert(frame_left_col,  framem_left_col)
    cv.Convert(frame_right_col, framem_right_col)


    # rectify frames
    rectim_left, rectim_right = rectifyImages(framem_left, framem_right, saveImages = False)
    
    rectim8uc1_left  = cv.CreateMat(480, 640, cv.CV_8UC1)
    rectim8uc1_right = cv.CreateMat(480, 640, cv.CV_8UC1)
    #cv.Cvt(rectim_left,  rectim8uc1_left)
    cv.Convert(rectim_left, rectim8uc1_left)
    cv.Convert(rectim_right, rectim8uc1_right)
    
    depthmat = findstereocorrespondence(rectim8uc1_left, rectim8uc1_right)

    

    # depthmat:
    depthimage  = cv.CreateImage( (framem_left.width, framem_left.height), \
                          frame_left.depth, 1)
    cv.Convert(depthmat, depthimage)

    # show image
    cv.ShowImage("leftimage", depthimage)


    # Extra functions
    # no-background-map:
    if remove_background:
      foo = removeBackground(framem_left_col, depthmat)
      bar = cv.CreateImage( (frame_left_col.width, frame_left_col.height), \
                            frame_left_col.depth, frame_left_col.nChannels)
      cv.Convert(foo, bar)
      cv.ShowImage("rightimage", bar)

      #foo2 = removeBackground(framem_right_col, depthmat)
      #bar2 = cv.CreateImage( (frame_left_col.width, frame_left_col.height), \
      #                      frame_left_col.depth, frame_left_col.nChannels)
      #cv.Convert(foo2, bar2)
      #cv.ShowImage("rightimage", bar2)

    # check for exit
    k = cv.WaitKey(33)
    if k == 0x1b:
      break

    

    #bar = cv.GetImage(foo) # <-- better! GetImage and GetMatrix
