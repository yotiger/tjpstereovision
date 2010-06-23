#!/usr/bin/python
# Depthmap Live: view live depthmap
# University of Amsterdam
# Stereo Vision project, June 2010

import cv
import sys
import os
from stereoheader import *
from stereo_bm_test import *

if __name__ == "__main__":

  CAM_LEFT  = 1
  CAM_RIGHT = 2

  # parse commandline args
  remove_background = False
  algoritm = "bm"
  sgbm_path = "../C++/sgbm ../Python/{0} ../Python/{1}"
  for i in range(1, len(sys.argv)):
    if sys.argv[i][:11] == "--remove-bg":
      remove_background = True
      background_threshold = 250
      if len(sys.argv[i]) > 11:
        background_image_old = cv.LoadImageM(sys.argv[i][12:])
        background_image = cv.CreateMat(480, 640, 18)
        cv.Convert(background_image_old, background_image)
      else:
        background_image = None
    elif sys.argv[i] == "--sgbm":
      algoritm = "sgbm"
      background_threshold = 70
    elif sys.argv[i] == "--rectify-only":
      algoritm = "rectify-only"
    elif sys.argv[i] == "--webcamviewer":
      algoritm = "none"

  # usage message
  print("Usage: " + sys.argv[0] + "[args]")
  print(" Possible arguments:")
  print("  --webcamviewer: show original images (don't do algoritms)")
  print("  --rectify-only: show rectified images")
  print("  --sgbm:         use sgbm instead of bm")
  print("  --remove-bg:    show original image for front object pixels")


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
    cv.GrabFrame(capture_left)
    cv.GrabFrame(capture_right)

    # i know, this is bad programming,
    # but seems to be the only way to drop 5 times the buffer
    # (to get live images, even when framerate drops to 1fps)
    frame_left_col  = cv.RetrieveFrame(capture_left)
    frame_left_col  = cv.RetrieveFrame(capture_left)
    frame_left_col  = cv.RetrieveFrame(capture_left)
    frame_left_col  = cv.RetrieveFrame(capture_left)
    frame_left_col  = cv.RetrieveFrame(capture_left)
    frame_left_col  = cv.RetrieveFrame(capture_left)
    frame_right_col = cv.RetrieveFrame(capture_right)
    frame_right_col = cv.RetrieveFrame(capture_right)
    frame_right_col = cv.RetrieveFrame(capture_right)
    frame_right_col = cv.RetrieveFrame(capture_right)
    frame_right_col = cv.RetrieveFrame(capture_right)
    frame_right_col = cv.RetrieveFrame(capture_right)

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


    if algoritm == "none":

      # webcamviewer: show original images
      cv.ShowImage("leftimage", frame_left_col)
      cv.ShowImage("rightimage", frame_right_col)

    else:

      # rectify frames
      rectim_left_col, rectim_right_col = rectifyImages(framem_left_col, framem_right_col, saveImages = False)
      
      rectim_left  = cv.CreateMat(480, 640, cv.CV_16UC1)
      rectim_right = cv.CreateMat(480, 640, cv.CV_16UC1)

      cv.CvtColor(rectim_left_col,  rectim_left,  cv.CV_BGR2GRAY)
      cv.CvtColor(rectim_right_col, rectim_right, cv.CV_BGR2GRAY)
      rectim8uc1_left  = cv.CreateMat(480, 640, cv.CV_8UC1)
      rectim8uc1_right = cv.CreateMat(480, 640, cv.CV_8UC1)
      cv.Convert(rectim_left, rectim8uc1_left)
      cv.Convert(rectim_right, rectim8uc1_right)

      if algoritm == "rectify-only":
        
        # show rectified images
        recti_left  = cv.CreateImage( (rectim_left_col.width, rectim_left_col.height), \
                                      frame_left_col.depth, 3)
        recti_right = cv.CreateImage( (framem_left_col.width, framem_left_col.height), \
                                      frame_left_col.depth, 3)
        cv.Convert(rectim_left_col,  recti_left)
        cv.Convert(rectim_right_col, recti_right)

        cv.ShowImage("leftimage", recti_left)
        cv.ShowImage("rightimage", recti_right)

      else:
      
        # first, do algoritm
        if algoritm == "bm":

          # use BlockMatching algoritm
          depthmat = findstereocorrespondence(rectim8uc1_left, rectim8uc1_right)
   
          # depthmat:
          depthimage  = cv.CreateImage( (framem_left.width, framem_left.height), \
                                         frame_left.depth, 1)
          cv.Convert(depthmat, depthimage)
  
        elif algoritm == "sgbm":

          imgurl_left  = "sgbm_left.jpg"
          imgurl_right = "sgbm_right.jpg"
          cv.SaveImage(imgurl_left,  rectim8uc1_left)
          cv.SaveImage(imgurl_right, rectim8uc1_right)

          os.system(sgbm_path.format(imgurl_left, imgurl_right))

          depthmat = cv.LoadImageM("sgbm.jpg", iscolor=cv.CV_LOAD_IMAGE_GRAYSCALE)
          depthimage  = cv.CreateImage( (framem_left.width, framem_left.height), \
                                         frame_left.depth, 1)
          cv.Convert(depthmat, depthimage)

        else:

          print("Algoritm not implemented yet: " + algoritm)
          sys.exit()


        # second, show depthmap
        cv.ShowImage("leftimage", depthimage)


        # third, do extra filters / functions
        # and if they exist, show as second image
          
        # no-background-map:
        if remove_background:
          
          foom = removeBackground(rectim_left_col, depthmat, threshold=background_threshold, background=background_image)
          foo  = cv.CreateImage( (frame_left_col.width, frame_left_col.height), \
                                  frame_left_col.depth, frame_left_col.nChannels)
          cv.Convert(foom, foo)
          # show image
          cv.ShowImage("rightimage", foo)


  
  
    # check for exit
    k = cv.WaitKey(33)
    if k == 0x1b:
      break

    

    #bar = cv.GetImage(foo) # <-- better! GetImage and GetMatrix
