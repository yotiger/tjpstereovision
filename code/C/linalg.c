#include <stdio.h>
#include <cv.h>

void fillMatrix(CvMat *m, int ver, int hor, float *points) {
    int i, j;
    for (i=0; i<ver; i++)
        for (j=0; j<hor; j++)
            cvmSet(m, i, j, points[i*2+j]);
}

int main() {
    /* make some matrices */
    CvMat *m1 = cvCreateMat(2, 3, CV_32FC1);
    CvMat *m2 = cvCreateMat(3, 3, CV_32FC1);
    CvMat *m3 = cvCreateMat(3, 2, CV_32FC1);
    float arr1[] = {1, 2, 3, 4, 5, 6};
    float arr2[] = {8, 4, 3, 9, 2, 1, 4, 2, 9};
    fillMatrix(m1, 2, 3, arr1);
    fillMatrix(m2, 3, 3, arr2);

    cvGEMM(m1, m2, 0, m3, 0);

    return 0;
}
