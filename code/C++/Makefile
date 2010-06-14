### Makefile --- 

## Author: xtroce@BhfMission.spuerwerk.net
## Version: $Id: Makefile,v 0.0 2010/06/08 15:05:25 xtroce Exp $
## Keywords: 
## X-URL: 

   TARGET1  := chesstest
   TARGET2  := sgbm
    SRCS1   := chessboard_test.cpp 
    SRCS2   := sgbm.cpp

    CCFLAGS = -O2 -Wall -ggdb 

    OPENCVFLAGS = `pkg-config --libs --cflags opencv`


#    .PHONY: all clean distclean 
    all:: clean ${TARGET1} ${TARGET2} 


    ${TARGET1}:  
	g++ ${CCFLAGS} ${OPENCVFLAGS} ${SRCS1} -o ${TARGET1}
    ${TARGET2}:  
	g++ ${CCFLAGS} ${OPENCVFLAGS} ${SRCS2} -o ${TARGET2}

    clean:: 
	-rm -f *~ *.o ${TARGET1} ${TARGET2} 

    distclean:: clean

### Makefile ends here
