#include <stdio.h>
#include <opencv/cv.h>
#include <opencv/highgui.h>

void fatal(char *message) {
    printf("[!!] Error: %s\n", message);
    exit(1);
}

void usage(char *progname) {
    printf("Usage: %s <effect> [avifile]\n", progname);
    printf(" effect could be: 'none', 'smooth', 'chessboard'\n");
    exit(1);
}

int slider_pos = 0;
CvCapture *capture;

// callback for relocation
void onTrackbarSlide(int pos) {
    slider_pos = pos;
    cvSetCaptureProperty(
        capture,
        CV_CAP_PROP_POS_FRAMES,
        pos
    );
}


int main(int argc, char* argv[]) {

    cvNamedWindow("foo", CV_WINDOW_AUTOSIZE);

    int file_capture;
    int smoothing = 0, chessboard = 0;

    if (argc < 2)
        usage(argv[0]);

    if (strcmp(argv[1], "none") == 0)
        printf("Using original frames.\n");
    else if (strcmp(argv[1], "smooth") == 0) {
        smoothing = 1;
        printf("Using Gaussian smoothing.\n");
    } else if (strcmp(argv[1], "chessboard") == 0) {
        chessboard = 1;
        printf("Searching for chessboard.\n");
    } else {
        printf("Invalid effect: %s\n", argv[1]);
        usage(argv[0]);
    }

    if (argc > 2) {
        printf("Using avi file: %s\n", argv[2]);
        capture = cvCreateFileCapture(argv[2]);
        file_capture = 1;
        
        // slider
        int frames = (int) cvGetCaptureProperty(
                                capture, CV_CAP_PROP_FRAME_COUNT);
        if (frames != 0) {
            cvCreateTrackbar(
                "Position",
                "foo",
                &slider_pos,
                frames,
                onTrackbarSlide
            );
        }
    } else {
        printf("Using webcam\n");
        capture = cvCreateCameraCapture(-1);
        file_capture = 0;
    }

    assert (capture != NULL);

    IplImage *frame;

    while (1) {
        frame = cvQueryFrame(capture);
        if (!frame)
            break;

        /* effects */
        if (smoothing) {
            /* gaussian */
            cvSmooth(frame, frame, CV_GAUSSIAN, 15, 15, 5, 5);
        }
        if (chessboard) {
            /* search for chessboard */
            CvPoint2D32f points[70];
            int cornercount = -1;
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

        cvShowImage("foo", frame);


        slider_pos++;
        if (file_capture && slider_pos % 100 == 0)
            // set trackbar position
            cvSetTrackbarPos("Position", "foo", slider_pos);

        char c = cvWaitKey(33);
        if (c == 27)
            break;
    }

    cvReleaseCapture(&capture);
    cvDestroyWindow("foo");

    return 0;
}
