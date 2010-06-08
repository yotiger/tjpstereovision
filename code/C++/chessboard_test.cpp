#include <stdio.h>
#include <cv.h>
#include <cxmisc.h>
#include <ctype.h>
#include <highgui.h>
#include <vector>
#include <string>

using namespace cv;
using namespace std;

int main(int argc, char* argv[]) {

  cvNamedWindow("Camera 1", CV_WINDOW_AUTOSIZE);
  cvNamedWindow("Result", CV_WINDOW_AUTOSIZE);
  int cam = 1;

  CvCapture *capture;
  capture = cvCaptureFromCAM(cam);

  cvSetCaptureProperty(capture, CV_CAP_PROP_FRAME_WIDTH, 320);
  cvSetCaptureProperty(capture, CV_CAP_PROP_FRAME_HEIGHT, 240);

  IplImage *frame;
  IplImage *resframe;
  vector<CvPoint2D32f> corners;
  corners.resize(70);
  int count = 0;

  while (1) {
    frame = cvQueryFrame(capture);
    if (!frame)
      break;
    cvShowImage("Camera 1", frame);
    int k = cvWaitKey(10);

    resframe = cvQueryFrame(capture);

    int found = cvFindChessboardCorners(frame, cvSize(10, 7), &corners[0], &count, CV_CALIB_CB_ADAPTIVE_THRESH | CV_CALIB_CB_NORMALIZE_IMAGE);

    if (found > 0) {
      cvDrawChessboardCorners(resframe, cvSize(10, 7), &corners[0], 70, found);
      cvShowImage("Result", resframe);
    }

    if (k == 0x1b) {
      printf("ESC pressed. Exiting...\n");
      break;
    }
  }
}
