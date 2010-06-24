#!/usr/bin/python

import sys
import cv
from stereorectify import loadRectif

def findstereocorrespondence(image_left, image_right,minDisparity=-5,maxDisparity=20):
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
    state = cv.CreateStereoGCState(maxDisparity,8)
    state.minDisparity = minDisparity
    print "Searching for correspondance from <",minDisparity,",",maxDisparity,">"
    cv.FindStereoCorrespondenceGC(image_left, image_right, disparity_left, disparity_right, state, 0)
    return (disparity_left, disparity_right)


if __name__ == '__main__':
    # SEBASTIAN KIJK HIER NAAR 
    if len(sys.argv) != 3 and len(sys.argv) != 5:
        print "Usage stereo_gc_only_test imLeft imRight [minDispariy maxDisparity]"
    else:
        print "Load image"
        (l, r) = [cv.LoadImageM(f, cv.CV_LOAD_IMAGE_GRAYSCALE) for f in sys.argv[1:3]]
        print "searching for stereo correspondence..."
        if len(sys.argv) == 5:
            (disparity_left, disparity_right) = findstereocorrespondence(l, r,int(sys.argv[3]),int(sys.argv[4]))
        else: 
            (disparity_left, disparity_right) = findstereocorrespondence(l, r)
        print "stereocorrespondence found"
        disparity_left_visual = cv.CreateMat(l.rows, l.cols, cv.CV_8U)
        cv.ConvertScale(disparity_left, disparity_left_visual, -16)
        cv.SaveImage("disparity.jpg", disparity_left_visual)
