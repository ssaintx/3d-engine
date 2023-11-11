# INSPIRED BY CODER SPACE: https://youtu.be/M_Hx0g5vFko?si=a3qCuOlAjv3A_fQn
# ORIGINAL GIHUB REPO: https://github.com/StanislavPetrovV/Software_3D_engine

# importing dependecies
from object_3d import *
from camera import *
from projection import *
import pygame as pg
import math

# creating class to handle primitives, camera, and so on
class SoftwareRender:
    # setting the size, fps while our file initializing
    def __init__(self):
        pg.init() 
        self.RES = self.WIDTH, self.HEIGHT = 1600, 900
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.create_objects()
    # this function lets us to create objects
    def create_objects(self):
        self.camera = Camera(self, [-5, 6, -55])
        self.projection = Projection(self)
        self.object = self.get_object_from_file() # enter the path to your 3d object. 
       # If you don't have you can download for free here https://free3d.com/3d-models/obj
        self.object.rotate_y(-math.pi / 4) # rotating the object to the left

    # getting our object to output it
    def get_object_from_file(self, filename):
        vertex, faces = [], []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    vertex.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
        return Object3D(self, vertex, faces) 
    
    # draw background
    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))
        self.object.draw()
    # run scene
    def run(self):
        while True:
            self.draw()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    app = SoftwareRender()
    app.run()