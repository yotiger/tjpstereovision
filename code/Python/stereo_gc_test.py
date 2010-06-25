#!/usr/bin/python

import sys
import cv
from stereorectify import loadRectif

def findstereocorrespondence(image_left, image_right):
    """
    Generate disparity depth map from set of stereo images
    using graph cut technique.
    """
    # image_left and image_right are the input 8-bit single-channel images
    # from the left and the right cameras, respectively
    (r, c) = (image_left.rows, image_left.cols)
    disparity_left = cv.CreateMat(r, c, cv.CV_32F)
    disparity_right = cv.CreateMat(r, c, cv.CV_32F)
    #state = cv.CreateStereoGCState(20, 8)
    state = cv.CreateStereoGCState(30,8)
    state.minDisparity = -5
    cv.FindStereoCorrespondenceGC(image_left, image_right, disparity_left, disparity_right, state, 0)
    return (disparity_left, disparity_right)


if __name__ == '__main__':
    # SEBASTIAN KIJK HIER NAAR 

    print "Load image"
    (l, r) = [cv.LoadImageM(f, cv.CV_LOAD_IMAGE_GRAYSCALE) for f in sys.argv[1:]]
    print "searching for stereo correspondence..."
    (disparity_left, disparity_right) = findstereocorrespondence(l, r)
    print "stereocorrespondence found"
    disparity_left_visual = cv.CreateMat(l.rows, l.cols, cv.CV_8U)
    cv.ConvertScale(disparity_left, disparity_left_visual, -16)

    cv.SaveImage("disparity.jpg", disparity_left_visual)

    print "starting 3D representation, loading values..."
    dispmat = cv.CreateMat(disparity_left_visual.rows, disparity_left_visual.cols, cv.CV_16SC1)
    cv.Convert(disparity_left_visual, dispmat)
    
    #threedimg = cv.CreateMat(dispmat.rows, dispmat.cols, cv.CV_16SC3)
    #(R1, R2, P1, P2, Q) = loadRectif("../../dataset/owndataset2/rect")
    #print "values loaded, reprojecting..."
    #cv.ReprojectImageTo3D(dispmat, threedimg, Q)
    #cv.SaveImage("3dimg.jpg", threedimg)
    
