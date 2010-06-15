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
    cv.Convert(frame_left, framem_left)
    cv.Convert(frame_right, framem_right)


    # rectify frames
    rectim_left, rectim_right = rectifyImages(framem_left, framem_right, saveImages = False)
    
    rectim8uc1_left  = cv.CreateMat(480, 640, cv.CV_8UC1)
    rectim8uc1_right = cv.CreateMat(480, 640, cv.CV_8UC1)
    #cv.Cvt(rectim_left,  rectim8uc1_left)
    cv.Convert(rectim_left, rectim8uc1_left)
    cv.Convert(rectim_right, rectim8uc1_right)
    
    depthmap = findstereocorrespondence(rectim8uc1_left, rectim8uc1_right)

    

    #cv.Convert(foo, bar)
    #foo = removeBackground(framem_left, depthmap)
    foo = depthmap
    bar  = cv.CreateImage( (framem_left.width, framem_left.height), \
                          cv.IPL_DEPTH_8S, 1)

    cv.Convert(foo, bar)
    cv.ShowImage("leftimage", bar)
    #cv.ShowImage("rightimage", bar)

    #maxi = 0
    #for i in range(0, 480):
    #  for j in range(0, 640):
    #    item = cv.mGet(depthmap, i, j)
    #    if not item == "nan" and item > maxi:
    #      maxi = item
    #print "max = " + str(maxi)

    # check for exit
    k = cv.WaitKey(10)
    if k == 0x1b:
      break

    

