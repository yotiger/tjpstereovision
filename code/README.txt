Authors:
 Sebastian Droppelmann
 Moos Hueting
 Sander Latour
 Martijn van der Veen

Last edited: 25 june 2010

To get all the software working, you will need:

* OpenCV library 2.1 or higher
* OpenCV Python bindings
* OpenGL

Most of the code is written in Python.
Some interesting scripts are:
* C++/sgbm.cpp              - the sgbm algoritm not yet available in Python
* Python/calibrate.sh       - calibration wizard: runs chessboard capture
                              program and calibrates / rectificates.
                              Use this before running demo prog
* Python/depthmap_live.py   - the demo program which uses the result of the
                              calibration wizard to show live rectified images,
                              live depthmap (bm or sgbm) or background-removal.
                              Run with option -h to see options.
* Python/3drep.py           - demo program that gives 3d representation of
                              depth map image file (uses opengl).

