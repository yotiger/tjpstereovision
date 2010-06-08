#include <stdio.h>
#include <iostream>
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
#include <opencv/cv.hpp>

using namespace std;
using namespace cv;

void fatal(char *message) {
    printf("[!!] Error: %s\n", message);
    exit(1);
}

int main(int argc, char** argv){
	if (argc < 3)
		fatal("USAGE sgbm img1 img2");

	Mat m1(cvLoadImage(argv[1], 0));
	Mat m2(cvLoadImage(argv[2], 0));
	Mat disp(m1.rows,m1.cols,CV_16U);
	cout << "M1: \n\n" << "rows: " << m1.rows << "\ncols: " << m1.cols << "\ndepth: " << m1.depth() << "\nchannels: " << m1.channels() << "\n\n";
	cout << "M2: \n\n" << "rows: " << m2.rows << "\ncols: " << m2.cols << "\ndepth: " << m2.depth() << "\nchannels: " << m2.channels() << "\n\n";
	cout << "DISP: \n\n" << "rows: " << disp.rows << "\ncols: " << disp.cols << "\ndepth: " << disp.depth() << "\nchannels: " << disp.channels() << "\n\n";
	StereoSGBM sgbm(0,16,5);
	sgbm(m1,m2,disp);
	//disp = disp / 16;
	for( int i = 0; i < 100; i++){
		for ( int j = 0; j < 100; j++){
	//		cout << "DISP[" << i << "][" << j <<"]" << disp.at<long int>(i,j) << "\n";
		}
	}
	imwrite("sgbm.jpg",disp);
}
