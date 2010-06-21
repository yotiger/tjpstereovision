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
  
  # do all pixels
  for i in range(0, image.height):
    for j in range(0, image.width):
      cv.mSet(result, i, j, cv.mGet(image, i, j))

  return result
