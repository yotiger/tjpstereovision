### Makefile --- 

## Author: xtroce@BhfMission.spuerwerk.net
## Version: $Id: Makefile,v 0.0 2010/06/08 15:05:25 xtroce Exp $
## Keywords: 
## X-URL: 

   TARGET1  := webcamviewer
   TARGET2  := mart_test1
   TARGET3  := mart_test0
    SRCS1   := webcamviewer.c
    SRCS2   := mart_test1.c
    SRCS3   := mart_test0.c

    CCFLAGS = -O2 -Wall -ggdb 

    OPENCVFLAGS = `pkg-config --libs --cflags opencv`


    .PHONY: all clean distclean 
    all:: ${TARGET1} ${TARGET2} ${TARGET3}

    ${TARGET1}:  
	gcc ${CCFLAGS} ${OPENCVFLAGS} ${SRCS1} -o ${TARGET1}
    ${TARGET2}:  
	gcc ${CCFLAGS} ${OPENCVFLAGS} ${SRCS2} -o ${TARGET2}
    ${TARGET3}:  
	gcc ${CCFLAGS} ${OPENCVFLAGS} ${SRCS3} -o ${TARGET3}

    clean:: 
	-rm -f *~ *.o ${TARGET1} ${TARGET2} ${TARGET3}

    distclean:: clean

### Makefile ends here
