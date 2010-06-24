#!/usr/bin/python

import sys
import cv

def findstereocorrespondence(image_left, image_right, fn="disparityBM.jpg", saveImage=False):
    """
    Generate a disparity map from two rectified stereoimages.

    image_left, image_right - the pair of stereoimages
    fn                      - filename for saving
    saveImage               - if set, the disparity map is saved to a file
    """
    # image_left and image_right are the input 8-bit single-channel images
    # from the left and the right cameras, respectively
    (r, c) = (image_left.rows, image_left.cols)
    disparity = cv.CreateMat(r, c, cv.CV_16S)
    state = cv.CreateStereoBMState()
    state.SADWindowSize = 17
    state.preFilterType = 1
    state.preFilterSize = 9
    state.preFilterCap = 63
    state.minDisparity = 0
    state.numberOfDisparities = 64
    state.textureThreshold = 15
    state.speckleRange = 32
    state.speckleWindowSize = 150
#    state.disp12MaxDiff = 1
    cv.FindStereoCorrespondenceBM(image_left, image_right, disparity, state)
    if saveImage:
      cv.SaveImage(fn, disparity)

    return disparity

if __name__ == '__main__':
    (l, r) = [cv.LoadImageM(f, cv.CV_LOAD_IMAGE_GRAYSCALE) for f in sys.argv[1:]]
    disparity = findstereocorrespondence(l, r, saveImage=True)
