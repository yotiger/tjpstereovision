#include <stdio.h>
#include <opencv/cv.h>
#include <opencv/highgui.h>
#include <opencv/cvcompat.h>
#include <opencv/cvtypes.h>
#include <opencv/cvver.h>
#include <opencv/cvwimage.h>
#include <opencv/cxcore.h>
#include <opencv/cxerror.h>
#include <opencv/cxflann.h>
#include <opencv/cxmisc.h>
#include <opencv/cxtypes.h>

void fatal(char *message) {
    printf("[!!] Error: %s\n", message);
    exit(1);
}

int main(int argc, char* argv[]) {
    if (argc == 1)
        fatal("no imagefile specified (first argument)");

    IplImage *img = cvLoadImage(argv[1], CV_LOAD_IMAGE_COLOR);
    cvNamedWindow(argv[1], CV_WINDOW_AUTOSIZE);
    cvShowImage(argv[1], img);
    cvWaitKey(0);
    cvReleaseImage( &img );
    cvDestroyWindow(argv[1]);

    return 0;
}
