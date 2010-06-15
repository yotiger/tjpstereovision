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
//#include "optparse.h"


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
	Mat disp(m1.rows,m1.cols,CV_8U);

	//output of the matrices
	cout << "M1: \n\n" << "rows: " << m1.rows << "\ncols: " << m1.cols << "\ndepth: " << m1.depth() << "\nchannels: " << m1.channels() << "\n\n";
	cout << "M2: \n\n" << "rows: " << m2.rows << "\ncols: " << m2.cols << "\ndepth: " << m2.depth() << "\nchannels: " << m2.channels() << "\n\n";
	cout << "DISP: \n\n" << "rows: " << disp.rows << "\ncols: " << disp.cols << "\ndepth: " << disp.depth() << "\nchannels: " << disp.channels() << "\n\n";

	//configuration of the algorithm
	int mindisp = 0;
	int maxdisp = disp.cols / 8;
	int channels = m1.channels();

	//prefilter values
	int SADsize = 9;
	int Pground = channels*SADsize*SADsize;

	//postfiltervalues
	int disp12MaxDiff = 2;
	int preFilterCap = 63;
	int uniqueness = 10;
	int speckleWS = 100;
	int speckleSize = 32;
	bool orig=true;
		//, disp12MaxDiff, 
	StereoSGBM sgbm(mindisp, maxdisp, SADsize, 8*Pground, 16*Pground, disp12MaxDiff, \  
			preFilterCap, uniqueness, speckleWS, speckleSize, orig);
	sgbm(m1,m2,disp);

	Mat disp8;
	disp.convertTo(disp8, CV_8U, 255/(maxdisp*16.));
	
	// for( int i = 0; i < 100; i++){
	// 	for ( int j = 0; j < 100; j++){
	// //		cout << "DISP[" << i << "][" << j <<"]" << disp.at<long int>(i,j) << "\n";
	//	}
	//}
	imwrite("sgbm.jpg",disp8);
}
