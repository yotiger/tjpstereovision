#include <stdio.h>
#include <opencv/highgui.h>

void fatal(char *message) {
    printf("[!!] Error: %s\n", message);
    exit(1);
}

int main(int argc, char* argv[]) {

    cvNamedWindow("foo", CV_WINDOW_AUTOSIZE);
    CvCapture *capture;

    if (argc > 1) {
        printf("Using avi file: %s\n", argv[1]);
        capture = cvCreateFileCapture(argv[1]);
    } else {
        printf("Using webcam\n");
        capture = cvCreateCameraCapture(-1);
    }

    assert (capture != NULL);

    IplImage *frame;

    while (1) {
        frame = cvQueryFrame(capture);
        if (!frame)
            break;
        cvShowImage("foo", frame);
        char c = cvWaitKey(33);
        if (c == 27)
            break;
    }

    cvReleaseCapture(&capture);
    cvDestroyWindow("foo");

    return 0;
}
