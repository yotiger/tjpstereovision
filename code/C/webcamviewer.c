#include <stdio.h>
#include <opencv/cv.h>
#include <opencv/highgui.h>

/* left and right seen from the computers eyes */
#define CAM_LEFT  1
#define CAM_RIGHT 2
#define SCREEN_WIDTH 200

void fatal(char *message) {
    printf("[!!] Error: %s\n", message);
    exit(1);
}


/* search for chessboard */
void chessboard_finder(IplImage *frame) {
    CvPoint2D32f points[70];
    int cornercount;
    if (cvFindChessboardCorners(frame,
                                cvSize(10,7),
                                points,
                                &cornercount,
                                0)) {
        /* found chessboard */
        cvDrawChessboardCorners(frame,
                                cvSize(10,7),
                                points,
                                cornercount,
                                1);
    }    
}



int main(int argc, char* argv[]) {

    int chessboard_search = 0;

    cvNamedWindow("leftimage",  CV_WINDOW_AUTOSIZE);
    cvNamedWindow("rightimage", CV_WINDOW_AUTOSIZE);
    CvCapture *capture_left, *capture_right;

    printf("Using webcam\n");
    capture_left  = cvCreateCameraCapture(CAM_LEFT );
    capture_right = cvCreateCameraCapture(CAM_RIGHT);
/*    cvSetCaptureProperty(capture_left, 
            CV_CAP_PROP_FRAME_WIDTH, SCREEN_WIDTH/2);
    cvSetCaptureProperty(capture_right, 
            CV_CAP_PROP_FRAME_WIDTH, SCREEN_WIDTH/2);
*/

    if (capture_left == NULL)
      fatal("can't find left webcam (seen from computers eyes)");
    if (capture_right == NULL)
      fatal("can't find right webcam (seen from computers eyes)");

    IplImage *frame_left, *frame_right;

    /* process frames */
    while (1) {
        /* get next frame */
        frame_left  = cvQueryFrame(capture_left);
        frame_right = cvQueryFrame(capture_right);

        if (!frame_left || !frame_right)
            break;

        /* search for chessboard */
        if (chessboard_search) {
            chessboard_finder(frame_left);
            chessboard_finder(frame_right);
        }

        /* show frames in window */
        cvShowImage("leftimage", frame_left);
        cvShowImage("rightimage", frame_right);

        char c = cvWaitKey(33);
        if (c == 27)
            break;
        if (c == 99) { /* pushed c */
            chessboard_search = !(chessboard_search);
            printf("Chessboard search is turned %s.\n",
                    (chessboard_search) ? "on" : "off");
        }
    }

    cvReleaseCapture(&capture_left);
    cvReleaseCapture(&capture_right);
    cvDestroyWindow("leftimage");
    cvDestroyWindow("rightimage");

    return 0;
}
