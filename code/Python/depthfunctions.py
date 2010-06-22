#!/usr/bin/env python
# Functions for depthmaps
# University of Amsterdam
# Stereo Vision Project, June 2010

import cv


# removeBackground: remove all pixels with value's less than treshold
# todo: or replace with pixel from other image
def removeBackground(image, depthmap, treshold=2.0e-304, background=None):
  result = cv.CreateMat(image.height, image.width, image.type)
  
  # do all pixels
  for i in range(0, image.height):
    for j in range(0, image.width):
      cv.mSet(result, i, j, cv.mGet(image, i, j))

  return result

