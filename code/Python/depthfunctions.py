#!/usr/bin/env python
# University of Amsterdam
# Stereo Vision Project, June 2010
"""
Collection of functions that work with depthmaps
"""
import cv

# todo: or replace with pixel from other image
def removeBackground(image, depthmap, treshold=2.0e-304, background=None):
  """
  Remove all pixels with values less than a certain threshold value.

  image    - image to remove background from
  depthmap - depthmap of image
  threshold - threshold value
  background - DOE ER IETS MEE MARTIJN!
  """
  
  result = cv.CreateMat(image.height, image.width, image.type)

  # do a lot of conversions to use cv.Threshold and get 3C image back
  depthmap8u = cv.CreateMat(depthmap.height, depthmap.width, cv.CV_8UC1)
  cv.Convert(depthmap, depthmap8u)
  
  depthmap_binary = cv.CreateMat(depthmap8u.height, depthmap8u.width, \
                                 depthmap8u.type)
  cv.Threshold(depthmap8u, depthmap_binary, threshold, 1, cv.CV_THRESH_BINARY)

  depthmap_binary_16u = cv.CreateMat(depthmap.height, depthmap.width, \
                                     cv.CV_16UC1)
  depthmap_binary_c3  = cv.CreateMat(depthmap.height, depthmap.width, \
                                     cv.CV_16UC3)
  cv.Convert(depthmap_binary, depthmap_binary_16u)                    
  # make 3-channel image from 1-channel image
  cv.Merge(depthmap_binary_16u, depthmap_binary_16u, \
           depthmap_binary_16u, None, \
           depthmap_binary_c3)
  # multiply binary image with image (black out pixels far away)
  cv.Mul(image, depthmap_binary_c3, result)

  return result
