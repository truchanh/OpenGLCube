import pygame as pg
from OpenGL.GL import *
from OpenGL.GLU import *

pg.init()

##basic setup video modes
FPS = 30
WINW = 640
WINH = 480
DIMS = WINW, WINH
FLAGS = pg.DOUBLEBUF|pg.OPENGL
BPP = pg.display.mode_ok(DIMS, FLAGS)
WIN = pg.display.set_mode(DIMS, FLAGS, BPP)
FOV_Y = 60
ASPECT_RATIO = WINW/WINH

n = 1.0
triangle_vertices = (##total: 12x3=36 vertices, format (x,y,z) each vertex
############# front ##############  -z (go backward to see the front)
(-n, n,-n), ( n,-n,-n), (-n,-n,-n),
(-n, n,-n), ( n, n,-n), ( n,-n,-n),
############# back ##############   +z (go forward to see the back)
(-n, n, n), ( n,-n, n), (-n,-n, n),
(-n, n, n), ( n, n, n), ( n,-n, n),
############# top ##############    +y
(-n, n, n), ( n, n, n), ( n, n,-n),
(-n, n, n), ( n, n,-n), (-n, n,-n),
############# bottom ############## -y
(-n,-n, n), ( n,-n, n), ( n,-n,-n),
(-n,-n, n), ( n,-n,-n), (-n,-n,-n),
############# left ##############   -x
(-n, n, n), (-n, n,-n), (-n,-n, n),
(-n, n,-n), (-n,-n,-n), (-n,-n, n),
############# right ##############  +x 
( n, n, n), ( n, n,-n), ( n,-n, n),
( n, n,-n), ( n,-n,-n), ( n,-n, n),
    )


def solid_colored_cube():
    glBegin(GL_TRIANGLES)
    for vertex in triangle_vertices:
        glColor3f(*vertex)  ##applying rgb color for each vertex
        glVertex3f(*vertex)  ##unpacking vertex tuple data into individual x, y, z coordinate
    glEnd()


def main():
    gluPerspective(FOV_Y,ASPECT_RATIO,.1,50.)

    glTranslatef(0,0,-5)

    glEnable(GL_DEPTH_TEST)
    
    done: bool = 0
    while not done:
        pg.time.Clock().tick(FPS)
        for e in pg.event.get():
            if e.type in (pg.QUIT, pg.WINDOWCLOSE):
                done = 1
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT|GL_STENCIL_BUFFER_BIT)
        glClearColor(.3,.3,.3,1)
        solid_colored_cube()
        glRotatef(1,1,0,1)
        pg.display.flip()
    pg.quit()
if __name__ == '__main__':
    main()
