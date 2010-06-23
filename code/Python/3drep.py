#!/usr/bin/python
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import cv
from OpenGL.GL.ARB.vertex_buffer_object import *
from VertexBuffer import *
import numpy


#some colors
colRed= (1, 0, 0)
colGreen = (0, 1, 0)
colBlue = (0, 0, 1)
colYellow = (1, 1, 0)
colDarkGray= (0.2, 0.2, 0.2)
colGray = (0.5, 0.5, 0.5)
colLightGray = (0.8, 0.8, 0.8)
colBlack = (0, 0, 0) 


CameraPos = [0.0, 20.0, 20.0]
lp = [0.0, 0.0]
pos = []
vert = None
color = []


def BuildVBOs (m_pVertices):
    """ // Generate And Bind The Vertex Buffer """
    m_nVBOVertices = int(glGenBuffersARB( 1));						# // Get A Valid Name
    glBindBufferARB( GL_ARRAY_BUFFER_ARB, m_nVBOVertices );	# // Bind The Buffer
			# // Load The Data
    glBufferDataARB( GL_ARRAY_BUFFER_ARB, m_pVertices, GL_STATIC_DRAW_ARB );





def initGL():
    mat_emission = (0.7, 0.7, 0.7, 0.0)
    lightPos = ( 5.0, 5.0, 10.0, 1.0 )
    spotpos = ( 0.0,0.0,0.0 )
    mat_specular = ( 1.0, 0.55, 1.0, 1.0 )
    mat_shininess = ( 30.0 )
    light_ambience = (0.0, 0.0, 0.5, 0.8)
    light_diffusion = (0.5, 0.0, 0.5, 0.8)
    light_specular = (0.0, 0.5, 0.0, 0.8) 
    
    
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glMaterialfv(GL_FRONT, GL_EMISSION, mat_emission)
    
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, spotpos)
    glLightfv(GL_LIGHT0, GL_POSITION, lightPos)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambience)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffusion)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glEnable(GL_NORMALIZE)
    glEnable(GL_POINT_SMOOTH)



def display():
    glutSetWindow(window)
#    glClearColor (0.0, 0.0, (time.time()%1.0)/1.0, 0.0)
    glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#    drawText( 'hello', 20,20, size[0],size[1] )
#    glutBitmapCharacter( GLUT_BITMAP_8_BY_13, ord('a'))
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    glFrustum(-1.0, +1.0, -1.0, 1.0, 5.0, 60.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(CameraPos[0],CameraPos[1],CameraPos[2],2,2,0,0,-1,0)
    glPushMatrix()

#    glMatrixMode(GL_MODELVIEW)
    draw_stuff()
    glPopMatrix()
    
    glFlush ()
    glutSwapBuffers()


def coordinateSystem( x,  y,  z):
	
    glBegin(GL_LINES)
    glColor3fv(colRed)
    glVertex3d(-x, 0, 0)
    glVertex3d(x, 0, 0)
    glColor3fv(colGreen)
    glVertex3d(0, -y, 0)
    glVertex3d(0, y, 0)
    glColor3fv(colBlue)
    glVertex3d(0, 0, z)
    glVertex3d(0, 0, -z)
    glEnd()

    h=0.05

    glBegin(GL_TRIANGLES) # Arrow at the end of the x-Axis
    glColor3fv(colRed)
    glVertex3d(x-h, h, 0)
    glVertex3d(x, 0, 0)
    glVertex3d(x-h, -h, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3fv(colGreen)
    glVertex3d(+h,y-h, 0)
    glVertex3d(0, y, 0)
    glVertex3d(-h,y-h, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3fv(colBlue)
    glVertex3d(0,+h, z-h)
    glVertex3d(0, 0, z)
    glVertex3d(0,-h, z-h)
    glEnd()

def reshape( *args ):
    global size 
    size = args
    glViewport( *( (0,0)+args) )
    display()

def draw_stuff():

    global pos, pos2
    #coordinateSystem(5,5,5)
    #glPushMatrix()
    
    # glBegin(GL_POINTS)
    # for i in pos:
    #     print i
    #     glColor3fv((1.0, 0.0, i[2]))
    #     glVertex(i)
    # glEnd()

    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, pos)
    glDrawArrays(GL_POINTS, 0, len(pos))
    glDisableClientState(GL_VERTEX_ARRAY)

#    glutSolidTeapot( 2 )
#    glColor(255,0,0)
#    glRectd(0,0,2,3) 
#    glPopMatrix()

def idle():
        glutSetWindow(window)
        glutPostRedisplay()

def printFunction( name ):
    def onevent( *args ):
        print '%s -> %s'%(name, ", ".join( [str(a) for a in args ]))
    return onevent

def zoomFunc():
    def onevent( *args ):
        global CameraPos
        if args[0] is 3:
            CameraPos[0] *= 0.8
            CameraPos[1] *= 0.8
            CameraPos[2] *= 0.8
#            print "Zoom in"
        elif args[0] is 4:
            CameraPos[0] *= 1.2
            CameraPos[1] *= 1.2
            CameraPos[2] *= 1.2
#            print "Zoom out"
    return onevent

def motionFunc(window):
    def onevent( *args ):
        global CameraPos, lp, size
        DX = args[0] - lp[0]
        DY = args[1] - lp[1]
        lp = args
        Alpha = (360.0 / (size[0] * 100.0)) * DX
        Beta = (360.0 / (size[1] * 100.0)) * DY
        

        #RotX	
        Ytemp = math.cos(Beta) * CameraPos[1] - math.sin(Beta) * CameraPos[2]
        Ztemp = math.sin(Beta) * CameraPos[1] + math.cos(Beta) * CameraPos[2]
    
        CameraPos[1] = Ytemp
        CameraPos[2] = Ztemp
        
        #RotY
        Xtemp = math.cos(Alpha) * CameraPos[0] + math.sin(Alpha) * CameraPos[2]
        Ztemp = - math.sin(Alpha) * CameraPos[0] + math.cos(Alpha) * CameraPos[2]
    
        CameraPos[2] = Ztemp
        CameraPos[0] = Xtemp

    return onevent


def passiveFunc( *args ):
    global lp
    lp = args
#    print "new lp is: ", lp, "args", args


def img2depth(im):
    scale = 0.01
    global pos, vert, color
    img = cv.LoadImageM(im, cv.CV_LOAD_IMAGE_GRAYSCALE)

    vert = numpy.zeros ((img.cols*img.rows, 3), 'f')
    index = 0
    

    print "Image loaded"
    for i in range(0, img.cols, 5):
        for j in range(0, img.rows, 5):
             pos += [[i*scale, j*scale, img[j,i]*scale]]
             vert [index, 0] = i*scale
             vert [index, 1] = j*scale
             vert [index, 2] = img[j,i]*scale
             index += 1

    #BuildVBOs(vert)
    print "succeeded in setting over images in vertices"

    

if __name__ == "__main__":
    import sys

    newArgv = glutInit(sys.argv)
    print 'newArguments', newArgv

    #create the depth vertex array
    print "image ", newArgv[1], "loaded"

    #glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
    #glutInitWindowSize(250, 250)
    #glutInitWindowPosition(100, 100)
    window = glutCreateWindow("hello")
    print 'window', repr(window)
    img2depth(newArgv[1])



    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMouseFunc(zoomFunc())
    glutMotionFunc(motionFunc(window))
    glutPassiveMotionFunc(passiveFunc)

    glutEntryFunc(printFunction( 'Entry' ))
    glutKeyboardFunc( printFunction( 'Keyboard' ))
    glutKeyboardUpFunc( printFunction( 'KeyboardUp' ))
    glutVisibilityFunc( printFunction( 'Visibility' ))
    glutWindowStatusFunc( printFunction( 'WindowStatus' ))
    glutSpecialFunc( printFunction( 'Special' ))
    glutSpecialUpFunc( printFunction( 'SpecialUp' ))
#    glutTimerFunc( 1000, ontimer, 23 )
    
    glutIdleFunc( idle )
    glutMainLoop()
