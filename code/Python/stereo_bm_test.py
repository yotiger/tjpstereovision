#!/usr/bin/python

import sys
import cv

def findstereocorrespondence(image_left, image_right):
    # image_left and image_right are the input 8-bit single-channel images
    # from the left and the right cameras, respectively
    (r, c) = (image_left.rows, image_left.cols)
    disparity = cv.CreateMat(r, c, cv.CV_16S)
    state = cv.CreateStereoBMState(cv.CV_STEREO_BM_BASIC)
    cv.FindStereoCorrespondenceBM(image_left, image_right, disparity, state)
    return disparity


if __name__ == '__main__':
    (l, r) = [cv.LoadImageM(f, cv.CV_LOAD_IMAGE_GRAYSCALE) for f in sys.argv[1:]]
    disparity = findstereocorrespondence(l, r)
    disparity_visual = cv.CreateMat(l.rows, l.cols, cv.CV_8U)
    cv.ConvertScale(disparity, disparity_visual, -16)
    cv.SaveImage("disparityBM.jpg", disparity_visual)
